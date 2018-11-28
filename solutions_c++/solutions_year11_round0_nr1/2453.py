#include <iostream>
#include <cstdio>

#define floop(i,a,b) for(int i=(a);i<(b);i++)
#define rloop(i,a,b) for(int i=(a);i>=(b);i--)

int pos[2],hops[2];
int move[200];
char bot[200];

int abs(int i){
	int num=(i>=0)?i:-i;
	return num;
}

void _init(){
	pos[1]=pos[0]=1;
	hops[0]=hops[1]=0;
}

void get_bot(char ch, int *current,int *other){
	switch(ch){
		case 'O':	*current=0;
					*other=1;
					break;
		case 'B':	*current=1;
					*other=0;
					break;
		default: 	*current=*other=-1;
	}
}

int process(){
	_init();
	int N,current,other,max_hops,jump;
	scanf("%d",&N);
	floop(i,0,N){
		bot[i]=getchar();
		scanf(" %c %d",(bot+i),(move+i));

//printf("%d %c\n",move[i],bot[i]);
	}

//printf("bot=%c bot_id=%d pos_orange=%d hops_orange=%d hops_black=%d pos_black=%d\n",bot[0],current,pos[0],hops[0],hops[1],pos[1]);
	
	floop(i,0,N){
		get_bot(bot[i],&current,&other);
		jump=abs(move[i]-pos[current]);

//printf("jump=%d move[i]=%d pos[current]=%d\n",jump,move[i],pos[current]);

		hops[current]=(jump <= (hops[other]-hops[current]))?hops[other]+1:hops[current]+jump+1;
		pos[current]=move[i];

//printf("bot=%c bot_id=%d pos_orange=%d hops_orange=%d hops_black=%d pos_black=%d\n",bot[i],current,pos[0],hops[0],hops[1],pos[1]);
	}

	max_hops=(hops[0]>hops[1])?hops[0]:hops[1];

	return max_hops;
}

main(){
	int testcases;
	scanf("%d",&testcases);
	floop(i,0,testcases){
		printf("Case #%d: %d\n",i+1,process());
	}
}

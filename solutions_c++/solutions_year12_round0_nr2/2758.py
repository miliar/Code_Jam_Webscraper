#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int calc_best(int total,int s)
{
	if (total==0){assert(!s);return 0;}
	if (!s){
		if (total%3==0)return total/3;
		else return total/3+1;
	}
	else{
		if (total%3==2)return total/3+2;
		else return total/3+1;
	}
	assert(0);
}

int above_num;

void search(int *sc,int rest,int S,int p,int curr_count)
{
	int total=*sc;
	if (rest==0){
		assert(S==0);
		//現在の結果を書き込む
		if (above_num<curr_count){
			above_num=curr_count;
		}
		return;
	}
	//fprintf(stderr,"rest=%d S=%d total=%d\n",rest,S,total);
	if (rest>S){
		//non-surprisingとみなして探索
		int inc;
		inc=(calc_best(total,0)>=p)?1:0;
		search(sc+1,rest-1,S,p,curr_count+inc);
	}
	if (S>0 && total>=2){
		//surprisingとみなす
		int inc;
		inc=(calc_best(total,1)>=p)?1:0;
		search(sc+1,rest-1,S-1,p,curr_count+inc);
	}
}

int main(void)
{
	int T,t;
	scanf("%d\n",&T);
	for (t=1;t<=T;t++){
		int N,S,p;
		int n;
		int sc[100];
		memset(sc,0,sizeof(sc));
		scanf("%d %d %d ",&N,&S,&p);
		for (n=0;n<N;n++){
			scanf("%d ",&sc[n]);
		}
		above_num=0;
		search(sc,N,S,p,0);
		printf("Case #%d: %d\n",t,above_num);
	}
	return 0;
}

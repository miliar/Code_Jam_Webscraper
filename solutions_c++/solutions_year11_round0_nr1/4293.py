#include <stdio.h>
#define FOR(i,a,b) for(i=(a);i<=(b);i++)
#define N 100

int t,T,n;

struct query{
	char color;
	int pos;
};


query seq[N+1];

void process(){
	int posB=1,posO=1,i,j,timecost=0;
	FOR(i,1,n){
		FOR(j,i+1,n){
			if (seq[j].color != seq[i].color) break;
		}
		int *posnow,*posoppo,*temp;
		posnow = &posB, posoppo = &posO;
		if (seq[i].color == 'O'){
			temp = posnow;
			posnow = posoppo;
			posoppo = temp;
		}
		while(1){
			timecost++;
			if (*posoppo < seq[j].pos) (*posoppo)++;
			else if (*posoppo > seq[j].pos) (*posoppo)--;
			if (*posnow == seq[i].pos) break;
			else if (*posnow < seq[i].pos) (*posnow)++;
			else if (*posnow > seq[i].pos) (*posnow)--;
		}
	}
	printf("Case #%d: %d\n",t,timecost);
}

void input(){
	scanf("%d",&n);
	int i;
	char robot[10];
	int pos;
	FOR(i,1,n){
		scanf("%s %d",robot,&pos);
		seq[i].color = robot[0];
		seq[i].pos = pos;
	}
}

int main(){
	freopen("a-large.in","rt",stdin);
	freopen("a-large.out","wt",stdout);
	scanf("%d",&T);
	FOR(t,1,T){
		input();
		process();
	}
	return 0;
}
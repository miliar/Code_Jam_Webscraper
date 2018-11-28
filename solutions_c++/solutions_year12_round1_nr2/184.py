#include<stdio.h>

const int NMAX=1000;

typedef struct {int a,b,c;} LEVEL;

int N; LEVEL level[NMAX];

int solve() {
	int i,j,ret=0,done=0,now=0;
	while(done!=N) {
		for(i=0;i<N;i++)
			if(level[i].c!=2&&now>=level[i].b) {
				now+=2-level[i].c;
				level[i].c=2;
				ret++;
				done++;
				//printf("->2 for %d, now %d\n",i,now);
				break;
			}
		if(i<N)continue;
		j=-1;
		for(i=0;i<N;i++)
			if(level[i].c==0&&now>=level[i].a&&(j<0||level[i].b>level[j].b))
				j=i;
		if(j<0)break;
		now++;
		level[j].c=1;
		ret++;
	}
	return done==N?ret:-1;
}

void input() {
	scanf("%d",&N);
	for(int i=0;i<N;i++) {
		scanf("%d%d",&level[i].a,&level[i].b);
		level[i].c=0;
	}
}

int main() {
	int t,s;
	scanf("%d",&t);
	for(s=1;s<=t;s++) {
		input();
		int ans=solve();
		if(ans<0)printf("Case #%d: Too Bad\n",s);
		else printf("Case #%d: %d\n",s,ans);
	}
	return 0;
}

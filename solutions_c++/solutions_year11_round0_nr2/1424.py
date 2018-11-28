#include <stdio.h>
#include <string.h>
#define MAXNUM 50
#define MAXLEN 120

int cn,dn,qn;
char con[MAXNUM][4],des[MAXNUM][3];
char cmat[128][128],dmat[128][128];
char seq[MAXLEN];

int ll;
char lst[MAXLEN];

inline void output() {
	int i;
	printf("[");
	for(i=0;i<ll;i++) {
		if(i) printf(", ");
		printf("%c",lst[i]);
	}
	puts("]");
}

inline void solve() {
	int i,j;
	char x;
	ll=0;
	for(i=0;i<qn;i++) {
		x=seq[i];
		if(ll&&cmat[x][lst[ll-1]]) lst[ll-1]=cmat[x][lst[ll-1]];
		else {
			for(j=0;j<ll;j++)
				if(dmat[x][lst[j]]) break;
			if(j<ll) ll=0;
			else lst[ll++]=x;
		}
	}
	output();
}

int main(void)
{
	int t,i,casenum=1;
	scanf("%d",&t);
	while(t--) {
		memset(cmat,0,sizeof(cmat));
		memset(dmat,0,sizeof(dmat));
		scanf("%d",&cn);
		for(i=0;i<cn;i++) {
			scanf("%s",con[i]);
			cmat[con[i][0]][con[i][1]]=con[i][2];
			cmat[con[i][1]][con[i][0]]=con[i][2];
		}
		scanf("%d",&dn);
		for(i=0;i<dn;i++) {
			scanf("%s",des[i]);
			dmat[des[i][0]][des[i][1]]=1;
			dmat[des[i][1]][des[i][0]]=1;
		}
		scanf("%d",&qn);
		scanf("%s",seq);
		printf("Case #%d: ",casenum++);
		solve();
	}
}

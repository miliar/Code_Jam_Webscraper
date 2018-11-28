#include <stdio.h>
#include <string.h>

char a[25][70];
int b[128];
int c[25][128];
char p[128];

int ans[128];
int n,K;
int frac[128];
int antif[10010];
int MOD = 10009;

char ur[105];
int up;

void go(int lev){
	for(int i=0;i<n;i++){
		for(int j=0;j<up;j++)
			b[ur[j]]+=c[i][ur[j]];
	/*	for(int j=0;a[i][j];j++)
			++b[a[i][j]];*/
		int nw=1,ns=0;
		for(int j=0;p[j];j++){
			if(p[j]=='+')
			{
				ns+=nw;nw = 1;}
			else{
				nw=nw*b[p[j]]%MOD;
			}
		}
		ns +=nw;
		ans[lev] = (ans[lev]+ns)%MOD;
		if(lev<K) go(lev+1);
		for(int j=0;j<up;j++)
			b[ur[j]]-=c[i][ur[j]];
		/*for(int j=0;a[i][j];j++)
			--b[a[i][j]];*/
	}
}
int main(void)
{
	int T,cs, i, j;
	scanf("%d",&T);
	frac[0]=1;
	for(i=1;i<=10;i++)
		frac[i] = frac[i-1]*i%MOD;
	for(i=1;i<=10008;i++){
		for(j=1;j<=10008;j++)
			if(i*j%MOD==1){
				antif[i] = j;
				break;
			}
	}
			
	for(cs=1;cs<=T;cs++){
		fprintf(stderr,"case %d\n",cs);
		printf("Case #%d:",cs);
		scanf("%s",p);
		memset(ans,0,sizeof(ans));
		memset(b,0,sizeof(b));
		scanf("%d",&K);
		scanf("%d",&n);
		memset(c,0,sizeof(c));
		for(i=0;i<n;i++){
			scanf("%s",a[i]);
			for(int j=0;a[i][j];j++)
			c[i][a[i][j]]++;
		}
		up=0;
		int used[128]={0};
		for(i=0;p[i];i++)
			if(p[i]!='+' && !used[p[i]])
				ur[up++] = p[i],used[p[i]]=1;
		go(1);
		for(i=1;i<=K;i++)
			printf(" %d",ans[i]);
		printf("\n");
	}
	return 0;
}

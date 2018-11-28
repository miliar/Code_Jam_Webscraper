#include <stdio.h>
#include <algorithm>

using namespace std;

#define MAX 11000

#define f1(a) (2*(a)+1)
#define f2(a) (2*(a)+2)

int pd[MAX][2];
int sig[MAX];
int c[MAX];
int op[2][2][2]={{{0,1},{1,1}},{{0,0},{0,1}}};

void solve(int pos)
{
	int i,j;
	for(i=0;i<2;++i)
		for(j=0;j<2;++j)
		{
			if(pd[f1(pos)][i]>=0 && pd[f2(pos)][j]>=0 && 
				(pd[pos][op[sig[pos]][i][j]]<0 ||
				pd[pos][op[sig[pos]][i][j]]>pd[f1(pos)][i]+pd[f2(pos)][j]) )
				pd[pos][op[sig[pos]][i][j]]=pd[f1(pos)][i]+pd[f2(pos)][j];
			if(c[pos] && pd[f1(pos)][i]>=0 && pd[f2(pos)][j]>=0 && 
				(pd[pos][op[!sig[pos]][i][j]]<0 ||
				pd[pos][op[!sig[pos]][i][j]]>pd[f1(pos)][i]+pd[f2(pos)][j]+1) )
				pd[pos][op[!sig[pos]][i][j]]=pd[f1(pos)][i]+pd[f2(pos)][j]+1;
		}
}

int main()
{
	int i;
	int n;
	int cnt,t;
	int tmp;
	int v;
	scanf("%d",&t);
	for(cnt=1;cnt<=t;++cnt)
	{
		scanf("%d %d",&n,&v);
		for(i=0;i<n;++i)
			pd[i][0]=pd[i][1]=-1;
		for(i=0;i<(n-1)/2;++i)
			scanf("%d %d",&sig[i],&c[i]);
		for(;i<n;++i)
		{
			scanf("%d",&tmp);
			pd[i][tmp]=0;
		}
		for(i=(n-1)/2 - 1;i>=0;--i)
			solve(i);

		printf("Case #%d: ",cnt);
		if(pd[0][v]>=0)
			printf("%d\n",pd[0][v]);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
		



	
	


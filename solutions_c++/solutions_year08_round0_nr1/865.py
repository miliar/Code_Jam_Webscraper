#pragma warning (disable : 4786)
#include<cstdio>
#include<string>
#include<cstring>
#include<map>

#define inf 100000000
using namespace std;

int memo[102][1002],N,Q,query[1002];
map<string,int> S;

int min(int a,int b) {return a<b ? a : b ; }

int solve(int n,int q)
{
	int ret=inf,i,j;

	if(q==Q) return 0;
	if(memo[n][q]!=-1) return memo[n][q];

	for(i=0;i<N;i++)
	{
		if(i==query[q]) continue;
		int change = (i==n) ? 0 : 1;
		if(q==0) change=0;
		ret=min(ret,change+solve(i,q+1));
	}

	return memo[n][q]=ret;
}
int main()
{
	int tests,cs=0,i;
	char line[250];

//	freopen("C:\\A.in","r",stdin);
//	freopen("C:\\Alarge2.txt","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		S.clear();
		scanf("%d\n",&N);
		for(i=0;i<N;i++)
		{
			gets(line);
			S[(string)line]=i;

		}
		scanf("%d\n",&Q);

		for(i=0;i<Q;i++)
		{
			gets(line);
			if(S.find(line)==S.end())
				query[i]=N;
			else
				query[i]=S[line];

		}
		memset(memo,-1,sizeof(memo));
		int ans=solve(0,0);
		printf("Case #%d: %d\n",++cs,ans);

	}
	return 0;
}

#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(i,a)for(int i=0;i<(a);i++)

int N,k,n,p[5];
char S[50001],T[50001];

int main()
{
	freopen("D.in","r",stdin);freopen("D.out","w",stdout);
	scanf("%d",&N);
	REP(C,N)
	{
		scanf("%d%s",&k,S);
		n=strlen(S);
		REP(i,k)p[i]=i;
		int ans=n;
		do
		{
			for(int i=0;i<n;i+=k)REP(j,k)T[i+j]=S[i+p[j]];
			int cnt=n;
			REP(i,n)if(i&&T[i]==T[i-1])cnt--;
			ans<?=cnt;
		}
		while(next_permutation(p,p+k));
		printf("Case #%d: %d\n",C+1,ans);
	}
	return 0;
}

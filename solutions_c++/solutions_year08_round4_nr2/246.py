#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(i,a)for(int i=0;i<(a);i++)

int C,N,M,A;

int main()
{
	freopen("B.in","r",stdin);freopen("B.out","w",stdout);
	scanf("%d",&C);
	REP(T,C)
	{
		scanf("%d%d%d",&N,&M,&A);
		REP(x1,N+1)for(int x2=x1;x2<=N;x2++)REP(y1,M+1)REP(y2,M+1)
			if(abs(x1*y2-x2*y1)==A)
			{
				printf("Case #%d: 0 0 %d %d %d %d\n",T+1,x1,y1,x2,y2);
				goto next;
			}
		printf("Case #%d: IMPOSSIBLE\n",T+1);
		next:;
	}
	return 0;
}

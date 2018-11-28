#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
using namespace std;

#define MAX(A,B) ((A)>(B)?(A):(B))
#define MIN(A,B) ((A)<(B)?(A):(B))
#define S(X) ((X)*(X))
#define ABS(X) ((X)>0?(X):(-(X)))
#define SZ(X) (int)(X.size())
typedef pair<int,int> PII;
typedef __int64 LL;

int pi[1004];
int u[1004];

void gen()
{
	int i,j;

	for(i=2;i<=1000;i++)
	{
		u[i]=1;
		pi[i]=1;
		for(j=2;j*j<=i;j++)
			if(i%j==0)
			{
				pi[i]=0;
				u[i]=0;
			}
	}

	for(i=2;i<=1000;i++)
	{
//		if(pi[i]) printf("%d\n",i);
		pi[i]+=pi[i-1];
	}
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin); freopen("C-small-output0.out","w",stdout);
//	freopen("C-small-attempt1.in","r",stdin); freopen("C-small-output1.out","w",stdout);
//	freopen("C-small-attempt2.in","r",stdin); freopen("C-small-output2.out","w",stdout);
//	freopen("C-large.in","r",stdin); freopen("C-large.out","w",stdout);

	int T, ks;
	int n;
	int i, cnt, now, best, worst;

	gen();

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		printf("Case #%d: ",ks);

		scanf("%d",&n);

		if(n==1)
		{
			printf("0\n");
			continue;
		}

		best = 0;
		worst=1;

		for(i=1;i<=n;i++)
			if(u[i]==1)
			{
				cnt = 0;
				now = n;
				while(now>=i)
				{
					cnt++;
					now/=i;
				}

				worst += cnt;
			}

		best = pi[n];

		printf("%d\n",worst-best);

	}

	return 0;
}
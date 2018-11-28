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

LL num[503][503], dp[503][503];
LL dpr[503][503], dpc[503][503];
LL DPR, DPC;
char grid[504][504];

int main()
{
//	freopen("B-small-attempt0.in","r",stdin); freopen("B-small-output0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin); freopen("B-small-output1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin); freopen("B-small-output2.out","w",stdout);
	freopen("B-large.in","r",stdin); freopen("B-large.out","w",stdout);

	int T, ks;
	int R,C,D;
	int i,j,maxx,ok,k;
	LL sum;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		printf("Case #%d: ",ks);

		scanf("%d%d%d",&R,&C,&D);

		for(i=1;i<=R;i++) scanf("%s",grid[i]+1);

		for(i=1;i<=R;i++)
			for(j=1;j<=C;j++)
			{
				num[i][j] = grid[i][j] - '0' + D;

				dp[i][j] = num[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1];

				dpr[i][j] = i*num[i][j]+ dpr[i-1][j] + dpr[i][j-1] - dpr[i-1][j-1];
				dpc[i][j] = j*num[i][j]+ dpc[i-1][j] + dpc[i][j-1] - dpc[i-1][j-1];
			}

		maxx = MIN(R,C);
		ok = 0;
		for(k = maxx;k>=3;k--)
		{
			for(i=1;i+k<=R+1;i++)
				for(j=1;j+k<=C+1;j++)
				{
					//from (i,j) to (i+k-1, j+k-1)

					if(k==5 && i==2 && j==2)
						k=k;

					sum = dp[i+k-1][j+k-1] - dp[i-1][j+k-1] - dp[i+k-1][j-1] + dp[i-1][j-1];
					sum-=num[i][j]; sum-=num[i+k-1][j]; sum-=num[i][j+k-1]; sum-=num[i+k-1][j+k-1];

					DPR = dpr[i+k-1][j+k-1] - dpr[i-1][j+k-1] - dpr[i+k-1][j-1] + dpr[i-1][j-1];
					DPR-=i*num[i][j]; DPR-=(i+k-1)*num[i+k-1][j]; DPR-=i*num[i][j+k-1]; DPR-=(i+k-1)*num[i+k-1][j+k-1];					
					DPC = dpc[i+k-1][j+k-1] - dpc[i-1][j+k-1] - dpc[i+k-1][j-1] + dpc[i-1][j-1];
					DPC-=j*num[i][j]; DPC-=j*num[i+k-1][j]; DPC-=(j+k-1)*num[i][j+k-1]; DPC-=(j+k-1)*num[i+k-1][j+k-1];					

					DPR -= sum*i;
					DPC -= sum*j;

					if(DPR*2 == sum*(k-1) && DPR==DPC)
					{
						ok = 1;
						goto e;
					}


				}
		}
e:
		if(ok) printf("%d\n",k);
		else printf("IMPOSSIBLE\n");

	}

	return 0;
}
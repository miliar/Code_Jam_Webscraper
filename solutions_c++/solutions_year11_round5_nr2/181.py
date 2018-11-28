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

int num[100];
int ks,T;
int i,j,now,ans;

int main()
{
	freopen("B-small-attempt0.in","r",stdin); freopen("B-small-output0.out","w",stdout);
//	freopen("B-small-attempt1.in","r",stdin); freopen("B-small-output1.out","w",stdout);
//	freopen("B-small-attempt2.in","r",stdin); freopen("B-small-output2.out","w",stdout);
//	freopen("B-large.in","r",stdin); freopen("B-large.out","w",stdout);

	int T, ks,n;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		printf("Case #%d: ",ks);

		scanf("%d",&n);
		for(i=0;i<n;i++) 
			scanf("%d",&num[i]);

		sort(num,num+n);

		ans = 0;
		do
		{
			now = n+n;
			for(i=0;i<n;)
			{
				for(j=i+1;j<n;j++)
					if(num[j-1]+1 != num[j])
						break;

				now = MIN(now, j - i);
				i = j;
			}

				ans = MAX(ans, now);
		}while(next_permutation(num,num+n));

		printf("%d\n",ans);
	}

	return 0;
}
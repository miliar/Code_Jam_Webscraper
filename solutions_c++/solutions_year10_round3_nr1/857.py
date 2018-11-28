#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<set>
#include<string>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<cmath>
#include<cstdio>
#include<utility>
using namespace std;
typedef long long ll;
#define pi acos(-1.0)
#define INF 1000000000
#define LINF 1000000000000000000LL
int gcd(int a,int b){return b==0?a:gcd(b,a%b);}

int A[1005];
int B[1005];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output1.txt","w",stdout);
	int T,N,i=0,j=0;
	scanf("%d",&T);
	for(int c=0;c<T;c++)
	{
		printf("Case #%d: ",c+1);
        scanf("%d",&N);
		for(i=0;i<N;i++)
		{scanf("%d %d",&A[i],&B[i]);}
		ll ans=0;
		for(i=0;i<N;i++)
			for(j=0;j<N;j++)
			{
				if(j!=i)
					if(A[i]>A[j]&&B[i]<B[j]||A[i]<A[j]&&B[i]>B[j]) ans++;
			}
		printf("%lld\n",ans/2);
	}
}
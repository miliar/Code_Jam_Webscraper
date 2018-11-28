#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <numeric>
#include <functional>
#include <iterator>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <complex>
#include <ctime>
using namespace std;

#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MEM(a,q) memset(a,q,sizeof(a))
#define FOR(i,s,n) for(i=s;i<n;i++)
#define PI acos(-1.0)
#define in(x) scanf("%d",&x)
#define out(x) printf("%d",x)



int a[1001][1001];
int b[1001][1001];

int c[1001];
int d[1001];
int num[1001];

int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int t,n,ca,i,j;
	__int64 ans;
	scanf("%d",&t);
	for(ca=1;ca<=t;ca++)
	{
		int r,k,n;
		in(r);
		in(k);
		in(n);
		for(i=0;i<n;i++)
		{
			in(num[i]);
		}
		int s;
		for(i=0;i<n;i++)
		{
			s=num[i];
			for(j=(i+1)%n;j!=i;j++,j%=n)
			{
				s+=num[j];
				if(s>k)
				{
				s-=num[j];
					break;
				}
			}
			c[i]=j;
			d[i]=s;
		}
		ans=0;
		int ss=0;
		while(r--)
		{
			ans+=d[ss];
			ss=c[ss];
		}
		printf("Case #%d: %I64d\n",ca,ans);
	}
	return 0;
}

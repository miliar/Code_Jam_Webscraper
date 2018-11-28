#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#define fi "A-small-attempt0.in"
#define fo "A-small-attempt0.out"
//#define fi "A.INP"
//#define fo "A.OUT"
#define nmax 10000+5
#define INF 1000000000
using namespace std;
typedef double dd;
//VARIABLES
int n,a[nmax],b[nmax],d[nmax];
//FUNCTION PROTOTYPES

void Init();
void Process(int test);

//MAIN
int main()
{
	int test;
       freopen(fi,"r",stdin);
       freopen(fo,"w",stdout);
       scanf("%d",&test);
       for (int i=1;i<=test;++i)
       {
	       Init();
       	Process(i);
       	cerr << i << endl;
	}
       return 0;
}

//FUNCTIONS AND PROCEDURES
void Init()
{
	memset(d,0,sizeof(d));
	scanf("%d",&n);
	for (int i=1;i<=n;++i) scanf("%d%d",&a[i],&b[i]);
	scanf("%d",&a[n+1]);
	d[1]=a[1];
}
void Process(int test)
{
	int k;
	for (int i=1;i<=n;++i)
	{
		k=i+1;
		while (a[i]+d[i]>=a[k])
		{
			if (k==n+1)
			{
				printf("Case #%d: YES\n",test);
				return;
			}
			d[k]=max(d[k],min(b[k],a[k]-a[i]));
			++k;
		}
	}
	printf("Case #%d: NO\n",test);
}

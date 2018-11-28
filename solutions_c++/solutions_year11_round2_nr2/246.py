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

typedef pair<int,int> PII;
typedef __int64 LL;

int p[300],v[300];
int C, D;

int ok(double t)
{
	double now = -1e50;
	int i;
	double dan, bam;

	for(i=0;i<C;i++)
	{
		bam = MAX(now + D, p[i]-t);
		dan = bam + 1.*D*(v[i]-1.);
		if( fabs(fabs(dan-p[i])-t)>1e-10 &&  ABS(dan - p[i])>t ) return 0;
		now = dan;
	}

	return 1;
}

int main()
{
//	freopen("B-small-attempt1.in","r",stdin); freopen("B-small-output1.out","w",stdout);
//	freopen("B-small-input1.in","r",stdin); freopen("B-small-output1.out","w",stdout);
//	freopen("B-small-input2.in","r",stdin); freopen("B-small-output2.out","w",stdout);
	freopen("B-large.in","r",stdin); freopen("B-large.out","w",stdout);

	int T, ks;
	int i;
	double lo, hi, mid;

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		printf("Case #%d: ",ks);

		scanf("%d%d",&C,&D);

		for(i=0;i<C;i++)
			scanf("%d%d",&p[i],&v[i]);

		lo = 0;
		hi = 1e15;

		for(i=0;i<400;i++)
		{
			mid = (hi+lo)/2;

			if( ok(mid) ) hi = mid;
			else 
			{
				lo = mid;
			}
		}

		printf("%.10lf\n",lo);

	}

	return 0;
}
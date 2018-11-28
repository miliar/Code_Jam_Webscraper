#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <ctime>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000
#define maxn 1000000

//typedef long long  LL;
typedef __int64 LL;

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

int pos[205],tot[205],n;

int check(double L,double D)
{
	int i,j,k;
	double now=pos[0]-L;

	for(i=0;i<n;i++)
	{
		for(j=0;j<tot[i];j++)
		{
			double p=pos[i];
			
			//printf("%lf %lf\n",p,now);
			if(fabs(p-now)-1e-9>L)
			{
				if(p-now>L)
					now=p-L;
				else
					return 0;
			}
			now+=D;
		}
	}
	
	return 1;
}

int main()
{
	int i,j,k,tests,cs=0;


	freopen("E:\\GCJ\\B-large.in","r",stdin);
	//freopen("E:\\GCJ\\Asmall.in","r",stdin);
	freopen("E:\\GCJ\\Blarge.out","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		double ans,D;
		LL lo=0,hi=1000000000;

		hi*=hi;

		scanf("%d%lf",&n,&D);
		for(i=0;i<n;i++)
			cin>>pos[i]>>tot[i];

		while(hi-lo>=0)
		{
			LL mid=(lo+hi)/2;
			double ll=(double)mid/2.0;

		//	mid=1.0;
			if(check(ll,D))
				ans=ll,hi=mid-1;
			else
				lo=mid+1;
			//break;
		}

		printf("Case #%d: %.6lf\n",++cs,ans);
	}

	return 0;
} 



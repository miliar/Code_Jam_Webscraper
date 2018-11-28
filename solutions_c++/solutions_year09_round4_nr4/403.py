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
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000
//typedef long long LL;
//typedef __int64 LL;

double x[50],y[50],r[50];

int main()
{
	int i,j,k,n,tests,cs=0;
	
//	freopen("C:\\Asmall.in","r",stdin);
	freopen("Dsmall60.out","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		double ans=inf;

		scanf("%d",&n);
		
		for(i=0;i<n;i++)
			scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);

		for(i=0;i<n;i++)
		{
			for(j=i+1;j<n;j++)
			{
				double d=sqrt( (x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j]) );
				d=d+r[i]+r[j];
				d/=2.0;

				double rr=r[0];

				if(i==0 && j==2) rr=r[1];
				if(i==0 && j==1) rr=r[2];

 				//printf("%d %d %lf\n",i,j,d);
				ans=MIN(ans,MAX(rr,d));
					 
			}
		}

		if(n==1)
			ans=r[0];

		if(n==2)
			ans=MAX(r[0],r[1]);

		printf("Case #%d: %.6lf\n",++cs,ans);


	}


	return 0;
} 



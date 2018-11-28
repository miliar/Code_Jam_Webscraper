#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define FOR(i,n) for( i = 0 ; i<(n) ; i++)
#define ROF(i,n) for( i = (n-1) ; i>=0 ; i--)
#define RFOR(i,a,b)  for( i = (a) ; i<(b) ; i++)
#define RROF(i,a,b)  for( i = (a-1) ; i>=(b) ; i--)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64
#define eps (1e-11)
#define inf (1<<29)
#define pb push_back 
#define ALL(a) a.begin(),a.end()
#define sz size()
double max(double a,double b)
{
	if(a>b) return a;
	else return b;
}
double min(double a,double b)
{
	if(a<b) return a;
	else return b;
}
struct node{
	double x,double y,double r;
};
node a[3];
double dis(node a,node b)
{
	double p = (a.x - b.x)*(a.x - b.x) +(a.y - b.y)*(a.y - b.y);
	return sqrt(p);
}
int main()
{
	
//	freopen("d.in","r",stdin);
	//freopen("d.txt","w",stdout);
	int tc,fg = 1;
	cin>>tc;
	while(tc--)
	{
		int n;
		cin>>n;
		int i;
		FOR(i,n)
			scanf("%lf %lf %lf",&a[i].x,&a[i].y,&a[i].r);
		double res = 0;
		if(n==1)
		{
			res = a[0].r;
		}
		else if(n == 2)
		{
			res = max(a[0].r,a[1].r);
		}
		else
		{
			res = max(a[0].r,a[1].r);
			res = max(res,a[2].r);
			double p1,p2,p3;
			p1 = (dis(a[0],a[1])+a[0].r+a[1].r)/2;
			p2 = (dis(a[0],a[2])+a[0].r+a[2].r)/2;
			p3 = (dis(a[2],a[1])+a[2].r+a[1].r)/2;
			double k = min(p1,p2);
			k = min(k,p3);
			res = max(res,k);
			
		}
		printf("Case #%d: %.6lf\n",fg++,res+eps);
		
	}
	
	return 0;
}
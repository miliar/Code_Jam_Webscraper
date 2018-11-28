#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>

using namespace std;
typedef long long ll;

const double PI=acos(-1.0);
const double eps=1e-11;

#define dump(x) cerr<<#x<<" = "<<(x)<<endl;

int countbit(int n) {return (n==0)?0:1+countbit(n&(n-1));}
int lowbit(int n) {return n&(n^(n-1));}
string toString(ll v) { ostringstream sout;sout<<v;return sout.str();}
string toString(int v) { ostringstream sout;sout<<v;return sout.str();}


int n;
double x[10],y[10],r[10];
bool vis[10];

double dis(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

bool test(double R)
{
	double R1,R2;
	int i,j;
	for (i=0;i<n;i++)
		if (!vis[i])
	{
		R1=R-r[i];
		for (j=i+1;j<n;j++)
			if (!vis[j])
		{		
			R2=R-r[j];
			if (R1+R2<dis(x[i],y[i],x[j],y[j])) return false;
		}
	}
	return true;
}


int main()
{
	int i,j,k;
	int t,v;
	int tim;

	int cas=0;
	double low,high,mid;

	freopen("in","r",stdin);
	freopen("out","w",stdout);

	scanf("%d",&t);
	while (t--)
	{
		cas++;
		scanf("%d",&n);	

		for (i=0;i<n;i++) scanf("%lf%lf%lf",&x[i],&y[i],&r[i]);

		double ans=1e10;

		if (n==1)
		{
			ans=r[0];
		}
		else
		{
			memset(vis,0,sizeof(vis));
			//all 
			low=r[0];
			for (i=1;i<n;i++) low=max(low,r[i]);
			high=1e10;
			int tim=10000;
			while (tim--)
			{
				mid=(low+high)/2;
				if (test(mid))  //ok
					high=mid;
				else
					low=mid;
			}
			ans=min(ans,mid);

			vis[0]=true;

			low=r[0];
			for (i=1;i<n;i++) low=max(low,r[i]);
			high=1e10;
			tim=10000;
			while (tim--)
			{
				mid=(low+high)/2;
				if (test(mid))  //ok
					high=mid;
				else
					low=mid;
			}
			ans=min(ans,mid);

			vis[0]=false;
			vis[1]=true;

			low=r[0];
			for (i=1;i<n;i++) low=max(low,r[i]);
			high=1e10;
			tim=10000;
			while (tim--)
			{
				mid=(low+high)/2;
				if (test(mid))  //ok
					high=mid;
				else
					low=mid;
			}
			ans=min(ans,mid);

			vis[1]=false;
			vis[2]=true;

			low=r[0];
			for (i=1;i<n;i++) low=max(low,r[i]);
			high=1e10;
			tim=10000;
			while (tim--)
			{
				mid=(low+high)/2;
				if (test(mid))  //ok
					high=mid;
				else
					low=mid;
			}
			ans=min(ans,mid);


		}

		printf("Case #%d: %lf\n",cas,ans);
	}
	return 0;
}

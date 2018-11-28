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
//typedef __int64 LL;

typedef pair<int,int> pi;
typedef pair<double,double> pd;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

pd all[1005];
double speed[1005],len[1005];
int flag[1005];

int main()
{
	int i,j,k,tests,cs=0,n;
	double L,R,S,t;


	//freopen("E:\\GCJ\\Asmall.in","r",stdin);
	freopen("E:\\GCJ\\Alarge.out","w",stdout);

	scanf("%d",&tests);

	while(tests--)
	{
		scanf("%lf%lf%lf%lf%d",&L,&S,&R,&t,&n);
		double ll=L;

		for(i=0;i<n;i++)
		{
			double s,t;
			scanf("%lf%lf%lf",&s,&t,&speed[i]);
			ll-=(t-s);
			len[i]=t-s;
		}
		len[n]=ll;
		speed[n++]=0.0;

		double ans=0.0,lo=0.0,hi=1e9;

		for(i=0;i<n;i++)
			all[i]=MP(speed[i],len[i]);

		sort(all,all+n);
		for(i=0;i<n;i++)
		{
			len[i]=all[i].first;
			speed[i]=all[i].second;
			swap(len[i],speed[i]);
		}
		for(i=0;i<n;i++)
		{

			double tt=MIN(len[i]/(speed[i]+R) , t);
		
			ans+=tt;
			t-=tt;
			double d= (speed[i]+R)*tt;

			if(d<len[i])
			{
				double t1= (len[i]-d)/(speed[i]+S);
				ans+=t1;
			}
		}

		printf("Case #%d: %.7lf\n",++cs,ans);
	}

	return 0;
} 



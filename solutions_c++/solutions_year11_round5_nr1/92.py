#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <utility>
#include <set>
#include <sstream>
#include <map>
#include <ctime>
#include <cstdlib>
#define fr(a,b,c) for (a=b;a<=c;a++)
#define frr(a,b,c) for (a=b;a>=c;a--)
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define F first
#define S second
#define oo 1000111222
#define eps 1e-9
using namespace std;
typedef long long ll;
const int dx[]={-1,0,1,0,-1,1,1,-1};
      int dy[]={0,1,0,-1,1,1,-1,-1};
      
int w,m,n,k;
double lft,rght,mid,per,area;
vector < pair<double,double> > a,b;
vector < double > re;

pair<double,double> intersect(pair<double,double> u,pair<double,double> v,double X)
{
	double A=u.S-v.S,B=v.F-u.F,C=-A*u.F-B*u.S;
	return make_pair(X,(-C-A*X)/B);
}

double calc(int m,int n)
{
	int i;
	double s=0;
	fr(i,0,m-2) s+=1.0*(a[i].F-a[i+1].F)*(a[i].S+a[i+1].S);
	frr(i,n-1,1) s+=1.0*(b[i].F-b[i-1].F)*(b[i].S+b[i-1].S);
	if (s<0) return -s/2;
	return s/2;
}

double cut(double X,int ok)
{
	int i,mm,nn,repa=0,repb=0;
	pair<double,double> ta,tb;
	frr(i,m-1,0)
		if (a[i].F<=X) break;
	if (a[i].F==X) mm=i+1;
	else 
	{
		repa=1; ta=a[i+1]; mm=i+2;
		a[i+1]=intersect(a[i],a[i+1],X);
	}
	frr(i,n-1,0)
		if (b[i].F<=X) break;
	if (b[i].F==X) nn=i+1;
	else
	{
		repb=1; tb=b[i+1]; nn=i+2;
		b[i+1]=intersect(b[i],b[i+1],X);
	}
	double re=calc(mm,nn);
	if (ok)	m=mm, n=nn;
	else
	{
		if (repa) a[mm-1]=ta;
		if (repb) b[nn-1]=tb;
	}
	return re;
}

double Abs(double x)
{
	if (x>=0) return x;
	return -x;
}

int main()
{
	freopen("alarge.in","r",stdin); freopen("alarge.out","w",stdout);
	int test,i,it;
	double x,y,tmp,pr;
	cin >> test;
	fr(it,1,test)
	{
		cout << "Case #" << it << ":" << endl;
		a.clear(); b.clear(); re.clear();
		cin >> w >> m >> n >> k;
		fr(i,1,m) scanf("%lf%lf",&x,&y), a.pb(mp(x,y));
		fr(i,1,n) scanf("%lf%lf",&x,&y), b.pb(mp(x,y));
		area=calc(m,n); 
		pr=1.0*area/k; lft=0; rght=1.0*w;
		while (--k)
		{
			 per=pr*k;
			 while (rght-lft>eps)
			 {
				 mid=(lft+rght)/2;
				 double tmp=cut(mid,0);
				 if (Abs(per-tmp)<eps) break;
				 if (tmp>per) rght=mid;
				 else lft=mid;
			 }
			 re.pb(mid);
			 tmp=cut(mid,1);
			 rght=mid; lft=0;
		}
		sort(re.begin(),re.end());
		fr(i,0,int(re.size())-1) printf("%.9lf\n",re[i]);
	}
   return 0;
}

#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
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
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

double pi=2*acos(0.0);

double f,outr,tt,ll,g,inr,i,tmp;

double getyu(double x)
{
	double tmp;
	tmp=(x+ll)/(ll+ll+g);
	tmp=tmp-(int)tmp;
	tmp*=(ll+ll+g);
	tmp-=ll;
	tmp-=ll;
	if (tmp<0) tmp+=(ll+ll+g);
	return tmp;
}

double dis(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

double gets(double x)
{
	double cs,tmp;
	cs=(2*inr*inr-x*x)/(2*inr*inr);
	tmp=acos(cs);
	return tmp*inr*inr/2-inr*inr*sin(tmp)/2;
}

double calc(double x1,double y1,int z1,double x2,double y2,int z2)
{
	double tmp1,tmp2;
	if (z1==0)
	{
		if (z2==0)
		{
			tmp1=getyu(y1);
			tmp2=getyu(y2);
			return (tmp1+tmp2)*g/2+gets(dis(x1,y1,x2,y2));
		}
		else
		{
			tmp1=getyu(y1);
			tmp2=getyu(x2);
			return tmp1*tmp2/2+gets(dis(x1,y1,x2,y2));
		}
	}
	else
	{
		if (z2==0)
		{
			tmp1=g-getyu(x1);
			tmp2=g-getyu(y2);
			return g*g-tmp1*tmp2/2+gets(dis(x1,y1,x2,y2));
		}
		else
		{
			tmp1=getyu(x1);
			tmp2=getyu(x2);
			return (tmp1+tmp2)*g/2+gets(dis(x1,y1,x2,y2));
		}
	}
}

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);

	int l,t,j;
	double tot,x1,y1,x2,y2,tmp;
	vector<pair<pair<double,double>,int> > a;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%lf%lf%lf%lf%lf",&f,&outr,&tt,&ll,&g);
		tt+=f;
		ll+=f;
		g-=f;
		g-=f;
		inr=outr-tt;
		if (g<=0)
		{
			printf("Case #%d: %.6lf\n",l+1,1.0);
			continue;
		}
		tot=0;
		for (i=ll+g;i<=inr;i+=(ll+ll+g))
		{
			tmp=sqrt(inr*inr-i*i);
			tot+=g*g*(int)((tmp+ll)/(ll+ll+g));
		}
		a.clear();
		for (i=0;i<=inr;)
		{
			i+=ll;
			tmp=sqrt(inr*inr-i*i);
			if ((i<=inr)&&(getyu(tmp)<=g))
			{
				a.push_back(make_pair(make_pair(i,sqrt(inr*inr-i*i)),0));
				a.push_back(make_pair(make_pair(sqrt(inr*inr-i*i),i),1));
			}
			i+=g;
			tmp=sqrt(inr*inr-i*i);
			if ((i<=inr)&&(getyu(tmp)<=g))
			{
				a.push_back(make_pair(make_pair(i,sqrt(inr*inr-i*i)),0));
				a.push_back(make_pair(make_pair(sqrt(inr*inr-i*i),i),1));
			}
			i+=ll;
		}
		sort(a.begin(),a.end());
		for (j=0;j<a.size();j+=2)
		{
			x1=a[j].first.first;
			y1=a[j].first.second;
			x2=a[j+1].first.first;
			y2=a[j+1].first.second;
			tot+=calc(x1,y1,a[j].second,x2,y2,a[j+1].second);
		}
		tot=(pi*outr*outr-4*tot)/pi/outr/outr;
		printf("Case #%d: %.6lf\n",l+1,tot);
	}
	return 0;
}


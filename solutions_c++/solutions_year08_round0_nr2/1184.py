#include <cstdio>
#include <deque>
#include <vector>
#include <algorithm>
using namespace std;
class Date
{
public:
	int h,m;
	int t;
	void scan(int type)
	{
		scanf("%d:%d",&h,&m);
		t=type;
	}
	Date operator+(int t)
	{
		Date res;
		res.m=m+t;
		res.h=h;
		if(res.m>60) {res.h+=res.m/60;res.m%=60;}
		
		return res;
	}
	Date(){}
};
bool operator<(const Date& a,const Date& b)
{
	if(a.h<b.h) return true;
	if(a.h>b.h) return false;
	
	return a.m<b.m;
}
bool operator>(const Date& a,const Date& b)
{
	if(a.h>b.h) return true;
	if(a.h<b.h) return false;
	return a.m>b.m;
}
bool pr(const Date& a,const Date& b)
{
	if(a.h<b.h) return true;
	if(a.h>b.h) return false;
	
	if(a.m<b.m) return true;
	if(a.m>b.m) return false;
	if(a.t==1||a.t==3)
	{
		if(b.t==0||b.t==2) return true;
		return false;
	}
	if(b.t==1||b.t==3) return false;
	return true;
	
}
void solution(int num)
{
	int n,m,i;
	int t;
	scanf("%d",&t);
	scanf("%d %d",&n,&m);
	vector<Date> a;
	Date e;
	for(i=0;i<n;i++)
	{
		e.scan(0);
		a.push_back(e);
		e.scan(1);
		a.push_back(e);
	}
	for(i=0;i<m;i++)
	{
		e.scan(2);
		a.push_back(e);
		e.scan(3);
		a.push_back(e);
	}
	sort(a.begin(),a.end(),pr);
	n=a.size();
	deque<Date> aa;
	deque<Date> bb;
	int j;
	int ar=0,br=0;
	for(i=0;i<n;i++)
	{
		if(a[i].t==0)
		{
			if(aa.empty())
			{
				ar++;
				continue;
			}
			if(aa[0]>a[i]) ar++;
			else aa.pop_front();
			continue;
		}
		if(a[i].t==1)
		{
			bb.push_back(a[i]+t);
			continue;
		}
		if(a[i].t==2)
		{
			if(bb.empty())
			{
				br++;
				continue;
			}
			if(bb[0]>a[i]) br++;
			else bb.pop_front();
			continue;
		}
		if(a[i].t==3)
		{
			aa.push_back(a[i]+t);
			continue;
		}
		
	}
	printf("Case #%d: %d %d\n",num,ar,br);
}
int main()
{
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	scanf("%d",&n);
	int i;
	for(i=0;i<n;i++)
		solution(i+1);
	return 0;
}

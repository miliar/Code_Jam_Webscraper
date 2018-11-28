#pragma warning(disable:4786)
#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

struct Che
{
	Che(int type,int s,int e)
	{
		_type=type;
		_s=s;
		_e=e;
	}
	bool operator < (const Che & c)const
	{
		return _s<c._s;
	}
	int _type;
	int _s;
	int _e;
};

struct To
{
	To(int type,int d)
	{
		_type=type;
		_d=d;
	}
	bool operator <(const To & t)const
	{
		return _d<t._d;
	}
	int _type;
	int _d;
};

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	int cnt;
	for(cnt=1;cnt<=t;cnt++)
	{
		int d;
		cin>>d;
		int m,n;
		cin>>m>>n;
		int i;
		multiset<Che> sc;
		multiset<To> st;
		multiset<Che>::iterator itc,itc1;
		multiset<To>::iterator itt,itt1;
		for(i=0;i<m;i++)
		{
			int type=1;
			int h1,m1,h2,m2;
			scanf("%d:%d%d:%d",&h1,&m1,&h2,&m2);
			int s1=h1*60+m1,s2=h2*60+m2+d;
			sc.insert(Che(type,s1,s2));
		}
		for(i=0;i<n;i++)
		{
			int type=2;
			int h1,m1,h2,m2;
			scanf("%d:%d%d:%d",&h1,&m1,&h2,&m2);
			int s1=h1*60+m1,s2=h2*60+m2+d;
			sc.insert(Che(type,s1,s2));
		}
		int a=0,b=0;
		int sa=0,sb=0;
		for(i=0;i<1440;i++)
		{
			for(itt=st.begin();itt!=st.end()&&itt->_d==i;)
			{
				itt1=itt;
				itt++;
				if(itt1->_type==1)
				{
					sb++;
				}
				else
				{
					sa++;
				}
				st.erase(itt1);
			}
			for(itc=sc.begin();itc!=sc.end()&&itc->_s==i;)
			{
				itc1=itc;
				itc++;
				if(itc1->_type==1)
				{
					if(sa>0)
						sa--;
					else
						a++;
				}
				else
				{
					if(sb>0)
						sb--;
					else
						b++;
				}
				st.insert(To(itc1->_type,itc1->_e));
				sc.erase(itc1);
			}
		}
		cout<<"Case #"<<cnt<<": "<<a<<" "<<b<<endl;
	}
	return 0;
}
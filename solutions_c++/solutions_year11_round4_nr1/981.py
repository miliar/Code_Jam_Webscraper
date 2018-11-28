#include<iostream>
#include<map>
#include<algorithm>
using namespace std;
struct node
{
	int x,y;
	int z;
}s[100000],ss[100000];
bool comp1(const node&a,const node&b)
{
	return a.x<b.x;
}
bool comp2(const node&a,const node&b)
{
	return a.z<b.z;
}
int main()
{
	freopen("ain.txt","r",stdin);
	freopen("aout.txt","w",stdout);
	int cas_num;
	scanf("%d",&cas_num);
	for(int case_num=1;case_num<=cas_num;case_num++)
	{
		printf("Case #%d: ",case_num);
		map<int,int>mp;
		int m,h,r,t,n;
		scanf("%d%d%d%d%d",&m,&h,&r,&t,&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d%d%d",&s[i].x,&s[i].y,&s[i].z);
			mp[s[i].x];
			mp[s[i].y];
		}
		if(n>0)
		sort(s,s+n,comp1);
		int p1 =0;
		int p2=n;
		if(n==0)
		{
			s[p2].x=0,s[p2].y=m;
			s[p2].z=0;
			p2++;
		}else
		{
			if(s[0].x!=0)
			{
				s[p2].x=0,s[p2].y=s[0].x;
				s[p2].z=0;
				p2++;
			}
			for(int i=1;i<n;i++)
			{
				if(s[i-1].y!=s[i].x)
				{
					s[p2].x=s[i-1].y;
					s[p2].y=s[i].x;
					s[p2].z=0;
					p2++;
				}
			}
			if(s[n-1].y!=m)
			{

				s[p2].x=s[n-1].y,s[p2].y=m;
				s[p2].z=0;
				p2++;
			}
		}
	//	sort(s,s+p2,comp1);	for(int i=0;i<p2;i++)	cout<<s[i].x<<" "<<s[i].y<<" "<<s[i].z<<endl;
		sort(s,s+p2,comp2);
		mp[0];
		mp[m];
		int index=0;
		for(map<int,int>::iterator it = mp.begin();it!=mp.end();it++)
		{
			it->second=index++;
		}

		long double res = 0;
		long double sj = 0;
		bool f = 1;
		for(int i=0;i<p2;i++)
		{
			int z  = s[i].y-s[i].x;
			long double t1 = z*1.0L/(h+s[i].z);
			long double t2 = z*1.0L/(r+s[i].z);
			if(!f)
				res+=t1;
			else
			{
				if(res+t2<=t)
					res+=t2;
				else
				{
					long double dis = (t-res)*(r+s[i].z);
					dis = z-dis;
					long double t3 = (t-res)+dis/(h+s[i].z);
					res+=t3;
					f=0;
				}
			}
		}
		printf("%.8lf\n",res);
	}
}
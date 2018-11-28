#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

long long  i,j,k,s,t,n,m,ans,T,I,t1,t2,t3,t4;
long long a[1000];
long long b[1000],c[1000],d[1000];

bool cmp(long long x,long long y){return x>y;}
main()
{
	cin>>T;
	for (I=1;I<=T;++I)
	{
		t1=t2=t3=t4=0;
		cin>>n;
		for (i=0;i<n;++i)
		{
			cin>>s;
			if (s>0) a[t1++]=s;
			else b[t2++]=s;
		}
		for (i=0;i<n;++i)
		{
			cin>>s;
			if (s>0) c[t3++]=s;
			else d[t4++]=s;
		}
		sort(a,a+t1);
		sort(b,b+t2,cmp);
		sort(c,c+t3);
		sort(d,d+t4,cmp);
		ans=0;
		if (t1>t4)
		{
//			cout<<t1<<t2<<t3<<t4<<endl;
			for (i=0;i<t4;++i)
			{
//				cout<<d[i]<<' '<<a[i+t1-t4]<<endl;
				ans+=d[i]*a[i+t1-t4];
			}
			for (i=0;i<t2;++i)
			{
//				cout<<b[i]<<' '<<c[i+t3-t2]<<endl;
				ans+=b[i]*c[i+t3-t2];
			}
			for (i=0;i<t1-t4;++i)
			{
//				cout<<a[i]<<' '<<c[t3-t2-1-i]<<endl;
				ans+=a[i]*c[t3-t2-i-1];
			}
		}
		else 
		{
			for (i=0;i<t1;++i)
				ans+=a[i]*d[i+t4-t1];
			for (i=0;i<t3;++i)
				ans+=c[i]*b[i+t2-t3];
			for (i=0;i<t4-t1;++i)
				ans+=d[i]*b[t2-t3-i-1];
		}
		cout<<"Case #"<<I<<": "<<ans<<endl;
	}
	return 0;
}
				

#include <iostream>
using std::cout;
using std::cin;


int main()
{
	int cases,ns[35],s[35],sCount,t,n,p,y;
	ns[0]=0;
	ns[1]=1;
	ns[29]=10;
	ns[30]=10;
	for(int i=2;i<=28;i++)
	{
		if(i%3==0)
		{
			ns[i]=i/3;
			s[i]=(i/3)+1;
		}
		if(i%3==1)
		{
			ns[i]=((i-1)/3)+1;
			s[i]=(i+2)/3;
		}
		if(i%3==2)
		{
			ns[i]=(i+1)/3;
			s[i]=((i-2)/3)+2;
		}
	}
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>n>>sCount>>p;
		y=0;
		for(int i=1;i<=n;i++)
		{
			cin>>t;
			if(t==0||t==1||t==29||t==30)
			{
				if(ns[t]>=p)y++;
			}
			else
			{
				if(ns[t]>=p)
				{
					y++;
				}
				else if(ns[t]<p && s[t]>=p && sCount>0)
				{
					sCount--;
					y++;
				}
			}
		}

		cout<<"Case #"<<kase<<": "<<y<<"\n";
	}
	return 0;
}
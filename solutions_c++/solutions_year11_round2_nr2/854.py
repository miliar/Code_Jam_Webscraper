#include<iostream>
#include<cmath>
using namespace std;

int work(int test_now)
{
	cout<<"Case #"<<test_now+1<<": ";
	int n,m;
	cin>>n>>m;
	int x[n+1];
	int y[n+1];
	for (int i=0; i<n; i++)
		{
			cin>>x[i];
			cin>>y[i];
		}
	/*for (int i=0; i<n; i++)
		for (int j=0; j<n-1; j++)
			if (x[i]>x[i+1])
			{
				int tmp=x[i];
				x[i]=x[i+1];
				x[i+1]=tmp;
				tmp=y[i];
				y[i]=y[i+1];
				y[i+1]=tmp;
          }*/
	double l=0;
	double r=1e13;
	while (r-l>1e-7)
	{	
		double mid=(l+r)/2;
		double now=-1e12;
		int ok=1;

		for (int i=0; i<n; i++)
			{
				if (now+m<x[i]-mid)
				   now=x[i]-mid;
	             else 
	               now=now+m;
                now=now+double(m)*(y[i]-1);
                
                if (now>x[i]+mid)
                {
                   ok=0;
                   break;
                   }
			}
		if (ok)
			r=mid;
		else
			l=mid;
	}
	cout<<l<<endl;
}

int main()
{
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
	int test_num;
	cin>>test_num;
	for (int i=0; i<test_num; i++)
		work(i);
	return 0;
}

#include<iostream>
using namespace std;

int main()
{
	int t,n,s,p;
	int T[100];
	int q,r,c=0;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n;
		cin>>s;
		cin>>p;
		for(int j=0;j<n;j++)
		{
			cin>>T[j];
			q = T[j] / 3;
			r = T[j] % 3;
			if(r==0)
			{
				if(q>=p)
					c++;
				else if(p==q+1&&q>0)
				{
					if(s>0)
					{	
						s--;
						c++;
					}
				}
			}
			else if(r==1)
			{
				if(q+1>=p)
					c++;
			}
			else
			{
				if(q+1>=p)
					c++;
				else if(q+2==p)
				{
					if(s>0)
					{
						s--;
						c++;
					}
				}
			}
		}
		cout<<"Case #"<<i<<": "<<c<<"\n";
		c = 0;
	}
	return 0;
}


#include <iostream>

using namespace std;

int main()
{
	int t,n,s,p;
	int point[150];
	freopen("B-large.in","r",stdin);
	freopen("Bout1","w",stdout);
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>n>>s>>p;
		cout<<"Case #"<<i<<": ";
		int res=0;		
		for(int j=0;j<n;j++)
		{
			cin>>point[j];
			if(point[j]==0)
				continue;
			int avg=point[j]/3;
			int sup=point[j]%3;
			if(avg>=p)
			{
				res++;
				continue;
			}
			if(sup>=1&&avg+1>=p)
			{
				res++;
				continue;
			}
			if(s>=1)
			{
				if(sup==0&&avg+1>=p)
				{
					res++;
					s--;
					continue;
				}
				if(sup==2&&avg+2>=p)
				{
					res++;
					s--;
					continue;
				}
			}	
		}
		if(p==0)
		{
			cout<<n<<endl;
			continue;
		}
		cout<<res<<endl;
	}
	return 0;
}


#include<iostream>
#include<math.h>
using namespace std;

int data[1010];

int main()
{

	int t;
	int r,k,n;
	cin>>t;
	int cases=0;
	while(t--)
	{
		cout<<"Case #"<<++cases<<": ";
		cin>>r>>k>>n;

		int all=0;
		int money=0;
		int last=0;
		int sum;
		int i,j;
		for(i=0;i<n;i++)
		{
			cin>>data[i];
			all+=data[i];
		}
		if(all<=k)
		{
			money+=r*all;
		}
		else
		{
			while(r--)
			{
				sum=0;
				for(i=last;;i=(i+1)%n)
				{
					if(sum+data[i]>k)
						break;
					sum+=data[i];
				}

				last=i;
				money+=sum;
			}
		}
		cout<<money<<endl;
	}
}
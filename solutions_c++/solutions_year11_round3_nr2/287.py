#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int ttt;
	cin>>ttt;
	for(int tt=1;tt<=ttt;tt++)
	{
		cout<<"Case #"<<tt<<": ";
		int L,n,C;
long long int t;
		int arr[10000];
		int d[1000003];
		cin>>L>>t>>n>>C;
		for(int i=0;i<C;i++)
			cin>>arr[i];
		for(int i=0;i<n;i++)
		{
			d[i]=arr[i%C]*2;
		}
		if(L==0)
		{
			long long int sum=0;
			for(int i=0;i<n;i++)
				sum+=d[i];
			cout<<sum<<endl;
		}
		if(L>0)
		{
			long long int sum=0;
			int i;
			for(i=0;i<n;i++)
			{
				sum+=d[i];
				if(sum>t)break;
			}
			if(t>=sum)cout<<sum<<endl;
			else
			{
				d[i]=sum-t;
				sum=t;
				 int sor[1000003];
				 int c=0;
				for( int j=i;j<n;j++)
					sor[c++]=d[j];
				sort(sor,sor+c);
				for( int j=c-1;j>=0;j--)
				{
					if(L>0){sum+=sor[j]/2;L--;}
					else sum+=sor[j];
				}
				cout<<sum<<endl;


			}

		}


	}


}

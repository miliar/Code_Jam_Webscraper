#include<iostream>
using namespace std;
long max(long a,long b)
{
	if(a>b)return a;
	else return b;
}	
bool addone(int mark[],int n)
{
	int i;
	bool check=false;
	for(i=0;i<n;i++)
		if(mark[i]==0)
			check=true;
	for(i=0;i<n;i++)
	{
		if(mark[i]==0)
		{
			mark[i]=1;
			break;
		}
		else
		{
			mark[i]=0;
		}
	}
	return check;
}

int main()
{
	int t,c=1;
	cin>>t;
	while(t)
	{
		t--;
		int n,i;
		cin>>n;
		long a[n];
		int mark[n];
		long maxsum=-1,sum=0,sum1=0,sum2=0,total=0;
		for(i=0;i<n;i++)
		{cin>>a[i];mark[i]=0;total+=a[i];}
		/*for(i=0;i<n;i++)
			sum=sum+a[i];
		cout<<sum<<"\n";*/
		do
		{
			for(i=0;i<n;i++)
			{
				if(mark[i]==0)
				{
					sum1=sum1^a[i];
					sum=sum+a[i];
				}
				else
					sum2=sum2^a[i];
			}
			if(sum1==sum2 && sum!=0 && sum!=total)
			{
				long r=max(sum,(total-sum));
				if(maxsum<r)
					maxsum=r;
			}
			sum=0;sum1=0;sum2=0;
		}while(addone(mark,n));
		if(maxsum==-1)
			cout<<"Case #"<<c<<": NO\n";
		else
			cout<<"Case #"<<c<<": "<<maxsum<<"\n";
		c++;
	}
return 0;
}
#include<iostream>
#include<cstdio>
using namespace std;
int cases,n,arr[20],total,ans=-1;
bool taken[20];
void check()
{
	int sum=0,pile1=0,pile2=0;
	
	for(int i=0;i<n;i++)
	{
		if(taken[i])
		{
			sum+=arr[i];
			pile1=pile1^arr[i];
		}
		else
			pile2=pile2^arr[i];
	}

	if(sum!=total && sum!=0 && pile1==pile2)
	{
		ans=max(ans,sum);
	}
}
void permute(int pos)
{
	if(pos==n)
	{
		check();
		return;
	}

	taken[pos]=false;
	permute(pos+1);
	taken[pos]=true;
	permute(pos+1);
}
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	cin>>cases;
	for(int cc=0;cc<cases;cc++)
	{
		ans=-1;
		total=0;

		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>arr[i];
			total+=arr[i];
		}

		permute(0);

		cout<<"Case #"<<cc+1<<": ";
		if(ans!=-1)
			cout<<ans<<endl;
		else
			cout<<"NO\n";
	}
	return 0;
}
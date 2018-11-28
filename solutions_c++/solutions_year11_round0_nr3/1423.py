#include "iostream"
#include "string"

using namespace  std;


int n;
int v[1010],mini,maxi;
int cnt[100];

void process(int num)
{
	int i=0;
	while(num)
	{
		if(num%2)
			cnt[i]++;
		num/=2;
		i++;
	}
}
void work()
{
	cin>>n;
	mini=1000000;
	maxi=0;
	for(int i=0;i<n;++i)
	{
		cin>>v[i];
		if(v[i]<mini)
			mini=v[i];
		if(v[i]>maxi)
			maxi=v[i];
	}
	for(int i=0;i<100;++i)
		cnt[i]=0;

	for(int i=0;i<n;++i)
	{
		process(v[i]);
	}
	for(int i=0;i<100;++i)
	{
		if(cnt[i]%2)
		{
			cout<<"NO"<<endl;
			return;
		}
	}
	int sum=0;
	for(int i=0;i<n;++i)
	{
		sum+=v[i];
	}
	sum-=mini;
	cout<<sum<<endl;
}

int main()
{
	freopen("c.txt","r",stdin);
	freopen("c.out.txt","w",stdout);

	int cs;
	cin>>cs;
	for(int i=1;i<=cs;++i)
	{
		cout<<"Case #"<<i<<": ";
		work();
	}
}
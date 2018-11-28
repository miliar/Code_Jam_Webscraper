#include "template"

int main()
{
	int t,n,i,j;
	unsigned int c[1001];
	unsigned int ans;
	long long int sum;
	cin>>t;
	REP(i,t)
	{
		ans=0;
		sum=0;
		cin>>n;
		REP(j,n)
		{
			cin>>c[j];
			ans^=c[j];
			sum+=c[j];
		}
		cout<<"Case #"<<i+1<<": ";
		if(ans!=0)
		{
			cout<<"NO"<<endl;
		}
		else
		{
			sort(c,c+n);
			sum-=c[0];
			cout<<sum<<endl;
		}
	}
	return 0;
}

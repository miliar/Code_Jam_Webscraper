#include<iostream>
using namespace std;
const int MAXN=1009;
int a[MAXN],b[MAXN],t,n,ans;

void online()
{
	ans=0;
	for (int i=1;i<=n;i++)
	{
		cin>>a[i]>>b[i];
		for (int j=1;j<i;j++)
			if ((a[i]-a[j])*(b[i]-b[j])<0) ans++;
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>t;
	for (int test=1;test<=t;test++)
	{
		cin>>n;
		online();
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
	fclose(stdin);	fclose(stdout);
	return 0;
}



#include <iostream>
#include <algorithm>
using namespace std;

int n;
int m;
int b,t;
int x[100],v[100];
bool flag[100];
int ans;

int caseN;
int main()
{
	cin>>caseN;
	for (int caseI=1;caseI<=caseN;caseI++)
	{
		cin>>n>>m>>b>>t;
		for (int i=0;i<n;i++)
			cin>>x[i];
		for (int i=0;i<n;i++)
			cin>>v[i];
		for (int i=0;i<n;i++)
			flag[i]=(x[i]+v[i]*t>=b);
		if (count(flag,flag+n,true)<m)
			ans=-1;
		else
		{
			ans=0;
			for (int i=n-1;m;i--)
				if (flag[i])
				{
					for (int j=i+1;j<n;j++)
						if (!flag[j])
							ans++;
					m--;
				}
		}
		cout<<"Case #"<<caseI<<": ";
		if (ans<0)
			cout<<"IMPOSSIBLE"<<endl;
		else
			cout<<ans<<endl;
	}
	return 0;
}




			


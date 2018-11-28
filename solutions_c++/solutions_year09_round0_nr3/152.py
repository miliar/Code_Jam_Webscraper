#include<string>
#include<iostream>
#include<cstring>
using namespace std;
int f[500][20];
int n,i,j,ans,casenum,k;
string s1,s2,tmp;
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	s2="welcome to code jam";
	cin>>n;
	getline(cin,s1);
	for (casenum=1;casenum<=n;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		memset(f,0,sizeof(f));
		getline(cin,s1);
		ans=0;
		for (i=0;i<s1.size();i++)
		{
			if (s1[i]=='w') f[i][0]=1;
			for (j=1;j<s2.size();j++)
			{
				if (s2[j]!=s1[i]) continue;
				if (j>i) break;
				for (k=0;k<i;k++)
					f[i][j]=(f[i][j]+f[k][j-1])%10000;
			}
		}
		for (i=0;i<s1.size();i++)
			ans=(ans+f[i][18])%10000;
		if (ans<1000) cout<<0;
		if (ans<100) cout<<0;
		if (ans<10) cout<<0;
		cout<<ans<<endl;
	}
	return 0;
}

#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
string name[209];
int n,m,t,ans,s[209];

void init()
{
	for (int i=1;i<=n+m;i++) 
	{	
		cin>>name[i]; name[i]+="/";
	}
}

int maxpre(string a,string b)
{
	int l=min(a.size(),b.size());
	for (int i=0;i<l;i++)
		if (a[i]!=b[i])
		{
			//return i-1;
			int j;
			for (j=i-1;a[j]!='/';j--);
			return j;
		}
	return l-1;
}

void query()
{
	ans=0;
	for (int i=n+1;i<=n+m;i++)
	{
		int l=name[i].size();
		memset(s,0,sizeof(s));
		for (int j=l-1;j>=0;j--)
		{
			s[j]=s[j+1];
			if (name[i][j]=='/') s[j]++;
		}
		int k=s[0]-1;
		for (int j=1;j<i;j++)
			k=min(k,s[maxpre(name[i],name[j])]-1);
		//cout<<k<<endl;
		ans+=k;
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
//	freopen("a.in","r",stdin);
	freopen("a3.out","w",stdout);
	cin>>t;
	for (int test=1;test<=t;test++)
	{
		cin>>n>>m;
		init();
		query();
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
	fclose(stdin); fclose(stdout);
	return 0;
}

	
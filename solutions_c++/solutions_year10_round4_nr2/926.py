#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
using namespace std;
int T,casenum,p,one,i,j,k,n,ans;
int m[2000];
bool flag;
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>T;
	for (casenum=1;casenum<=T;casenum++)
	{
		cout<<"Case #"<<casenum<<": ";
		cin>>p;
		n=(1<<p);
		for (i=1;i<=n;i++)
		{
			cin>>m[i];
			m[i]=p-m[i];
		}
		for (i=1;i<=(1<<(p))-1;i++)
			cin>>one;
		ans=0;
		for (i=p;i>=1;i--)
		{
			for (j=1;;j+=(1<<i))
			{
				if (j>n) break;
				flag=true;
				for (k=1;k<=(1<<i);k++)
					if (m[j+k-1]>0) flag=false;
				if (!flag)
				{
					ans++;
					for (k=1;k<=(1<<i);k++)
						if (m[j+k-1]>0) m[j+k-1]--;
				}
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}

#include<iostream>
#include<vector>
using namespace std;
vector< vector< int > > f;
vector<int> tmp;
int n,t,casenum,last,i,j,k,ans;
char ch;
int main()
{
	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>t;
	casenum=0;
	while (casenum<t)
	{
		casenum++;
		cout<<"Case #"<<casenum<<": ";
		cin>>n;
		f.clear();
		for (i=1;i<=n;i++)
		{
			tmp.clear();
			last=0;
			for (j=1;j<=n;j++)
			{
				cin>>ch;
				if (ch=='0') tmp.push_back(0);
				else tmp.push_back(1);
				if (ch=='1') last=j;
			}
			tmp.push_back(last);
			f.push_back(tmp);
			scanf("\n");
		}
		ans=0;
		for (i=1;i<=n;i++)
		{
			for (j=i;j<=n;j++)
				if (f[j-1][n]<=i) break;
			for (k=j;k>i;k--)
			{
				tmp=f[k-1];
				f[k-1]=f[k-2];
				f[k-2]=tmp;
				ans++;
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}

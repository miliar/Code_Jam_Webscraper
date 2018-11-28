#include<iostream>
#include<set>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	string ex[110],md[110];
	set<string> flag;
	int c,i,j,cs,n,m,ans;
	string tmp;
	cin>>cs;
	for (c=1;c<=cs;c++)
	{
		cin>>n>>m;
		flag.clear();
		for (i=0;i<n;i++)
		{
			cin>>ex[i];
			tmp="/";
			for (j=1;j<ex[i].size();j++)
				if (ex[i][j]!='/') tmp=tmp+ex[i][j];
				else 
				{
					flag.insert(tmp);
					tmp=tmp+ex[i][j];
				}
			flag.insert(tmp);
		}
		ans=0;
		for (i=0;i<m;i++)
		{
			cin>>md[i];
			tmp="/";
			for (j=1;j<md[i].size();j++)
			{
				if (md[i][j]!='/') tmp=tmp+md[i][j];
				else
				{
					if (flag.find(tmp)==flag.end())
					{
						ans++;
						flag.insert(tmp);
//						cout<<tmp<<endl;
					}
					tmp=tmp+md[i][j];
				}
			}
			if (flag.find(tmp)==flag.end())
			{
				ans++;
				flag.insert(tmp);
//				cout<<tmp<<endl;
			}
		}
		cout<<"Case #"<<c<<": "<<ans<<endl;
	}
	return 0;
}

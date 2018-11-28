#include<iostream>
#include<string>
#include<map>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int cs,i,n,css,ans,ct,q;
	string s;
	cin>>cs;
	for(css=1;css<=cs;css++)
	{
		cin>>n;
		map<string,int>d;
		getline(cin,s);
		for(i=1;i<=n;i++)
			getline(cin,s);
		cin>>q;
		getchar();
		ans=ct=0;
		while(q--)
		{
			getline(cin,s);
			if(d[s]==false)
			{
				d[s]=true;
				ct++;
				if(ct==n)
				{
					ct=1;
					ans++;
					d.clear();
					d[s]=true;
				}
			}
		}
		cout<<"Case #"<<css<<": "<<ans<<endl;
	}
	return 0;
}

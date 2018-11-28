#include <iostream>
#include <string>

using namespace std;

string c[100],d[100];

int T;

int main()
{
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int cn,dn;
		cin>>cn;
		for(int i=0;i<cn;i++)
			cin>>c[i];
		cin>>dn;
		for(int i=0;i<dn;i++)
			cin>>d[i];
		string str, ans;
		int len=0,n;
		cin>>n;
		cin>>str;
		//cout<<cn<<' '<<dn<<' '<<str<<endl;
		for(int i=0;i<n;i++)
		{
			if(len>0)
			{
				string s=ans.substr(len-1,1)+str[i];
				bool bo=false;
				for(int j=0;j<cn;j++)
					if(c[j][0]==s[0]&&c[j][1]==s[1]||c[j][1]==s[0]&&c[j][0]==s[1])
					{
						ans[len-1]=c[j][2];
						bo=true;
						break;
					}
				if(bo)continue;
				for(int j=0;j<dn;j++)
					if(str[i]==d[j][0]&&ans.find(d[j][1])!=string::npos||str[i]==d[j][1]&&ans.find(d[j][0])!=string::npos)
					{
						ans.clear();
						len=0;
						bo=true;
						break;
					}
				if(bo)continue;
			}
			ans+=str[i];
			len++;
		}
		cout<<"Case #"<<t<<": ";
		cout<<'[';
		if(len)
		{
			cout<<ans[0];
			for(int i=1;i<len;i++)cout<<", "<<ans[i];
		}
		cout<<']'<<endl;
		//cout<<ans<<endl;
	}
}

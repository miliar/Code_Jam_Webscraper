#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int main()
{
	int t,no=0;
	cin>>t;
	while(t--)
	{
		string str;
		cin>>str;
		string old_str=str;
		cout<<"Case #"<<++no<<": ";
		if(next_permutation(str.begin(),str.end()))
			cout<<str<<endl;
		else
		{
			string ans="";
			if(str[0]!='0')
			{
				ans=str[0];
				ans+="0";
				ans+=str.substr(1,str.size()-1);
			}
			else
			{
				for(int i=0;i<(int)str.size();i++)
					if(str[i]!='0')
					{
						swap(str[0],str[i]);
						break;
					}
				ans=str[0];
				ans+="0";
				ans+=str.substr(1,str.size()-1);
			}
			cout<<ans<<endl;
		}
	}
	return 0;
}
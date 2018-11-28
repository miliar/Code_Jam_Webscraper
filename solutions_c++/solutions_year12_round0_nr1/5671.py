#include <iostream>
#include <fstream>
#include <string>

using namespace std ;
#define SZ(x) ((int)x.size()) 

int main()
{
	ifstream cin ("input.in");
	ofstream cout ("b.out");
	int t ;
	string s2="yhesocvxduiglbkrztnwjpfmaq";
	string s1="abcdefghijklmnopqrstuvwxyz";
	string str;
	cin>>t;
	getline(cin,str);
	for(int i=0;i<t;i++)
	{
		string ans;
		getline(cin,str);
		for(int j=0;j<SZ(str);j++)
		{
			if(str[j]==' ')
			{
				ans.push_back(' ');
				continue;
			}
			for(int k=0;k<SZ(s1);k++)
			{
				if(s1[k]==str[j])
				{
					ans.push_back(s2[k]);
				    break ;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	return 0;
}
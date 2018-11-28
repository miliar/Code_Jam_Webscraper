#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <string>
using namespace std;
int t,n,m;
string str;
int main ()
{
	freopen ("input", "r", stdin);
	freopen ("output", "w", stdout);
	cin>>t;
	for (int cas=1;cas<=t;cas++)
	{
		set <string> sea;
		cin>>n>>m;
		getline (cin,str);

		for (int i=0;i<n;i++)
		{
			getline (cin,str);
			str+='/';
			string k;
			for (int j=0;j<str.size();j++)
			{
				k.push_back(str[j]);
				if (j>0 && str[j]=='/')
					sea.insert (k);
			}
		}
		int a=sea.size();

		for (int i=0;i<m;i++)
		{
			getline (cin,str);
			str+='/';
			string k;
			for (int j=0;j<str.size();j++)
			{
				k.push_back(str[j]);
				if (j>0 && str[j]=='/')
					sea.insert (k);
			}
		}
		cout<<"Case #"<<cas<<": "<<sea.size()-a<<endl;
		
	}

	return 0;
}

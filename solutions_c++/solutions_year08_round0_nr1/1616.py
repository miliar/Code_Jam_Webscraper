#include <iostream>
#include <fstream>
#include <set>
#include <string>
using namespace std;

int main()
{
	ifstream cin("large.in");
	ofstream cout("large.out");
	int z;
	cin>>z;
	for (int tc = 1 ; tc <= z ; tc++)
	{
		int n;
		cin>>n;

		set <string> dict;

		string s;
		getline(cin, s);
		while(n--)
		{
			getline(cin, s);
			dict.insert(s);
		}	

		set <string> a;

		cin>>n;
		getline(cin, s);
		int ans = 0;
		while(n--)
		{
			getline(cin, s);
			if (dict.count(s)) a.insert(s);
			if (a.size() == dict.size()) ans++, a.clear(), a.insert(s);
		}

		cout<<"Case #"<<tc<<": "<<ans<<endl;
	}
}
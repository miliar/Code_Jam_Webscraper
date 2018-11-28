#include <string>
#include <iostream>
#include <map>
using namespace std;

int main()
{
	char* G[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
					"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
					"de kr kd eoya kw aej tysr re ujdr lkgc jv"
				};
	char* E[] = {"our language is impossible to understand",
				 "there are twenty six factorial possibilities",
				"so it is okay if you want to just give up"
				};

	map<char, char> dict;
	for(int i = 0; i < 3; ++i)
	{
		string s(G[i]);
		for(int j = 0; j < s.length(); ++j)
		{
			if(s[j] != ' ')
				dict[s[j]] = E[i][j];
		}
	}
	dict['q'] = 'z';
	dict['z'] = 'q';

	/*map<char,char>::iterator it = dict.begin();
	while(it != dict.end())
	{
		cout<<it->first<<"-->"<<it->second<<endl;
		++it;
	}
	cout<<dict.size()<<endl;*/

	int T;
	cin>>T;
	string tmp;
	getline(cin, tmp);

	for(int i = 0; i < T; ++i)
	{
		string g;
		getline(cin, g);
		
		string out;
		for(int j = 0; j < g.length(); ++j)
		{
			if(g[j] != ' ')
				out.push_back(dict[g[j]]);
			else
				out.push_back(' ');
		}

		cout<<"Case #"<<i+1<<": "<<out<<endl;
	}
}
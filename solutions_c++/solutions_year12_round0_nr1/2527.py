#include <iostream>
#include <map>
#include <string>
#include <string.h>

using namespace std;

#define ARRSIZE(x) (sizeof((x))/sizeof((x)[0]))

static const char *inp[] = {"our language is impossible to understand",
			"there are twenty six factorial possibilities",
			"so it is okay if you want to just give up"};
static const char *mapping[]= {
			"ejp mysljylc kd kxveddknmc re jsicpdrysi",
			"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
			"de kr kd eoya kw aej tysr re ujdr lkgc jv"
};
static map<char, char> lang;
static bool inited = false;

string process(const string &str)
{
	if(!inited)
	{
		for(int i = 0; i < ARRSIZE(inp); i++)
		{
			for(int j = 0; j < strlen(inp[i]); j++)
			{
				lang[mapping[i][j]] = inp[i][j];
			}
		}
		lang['q'] = 'z'; // inferred from example 'hint'
		lang['z'] = 'q';

		inited = true;

		// map<char, char>::const_iterator itr;
		// itr = lang.begin();
		// while(itr != lang.end())
		// {
		// 	cout << itr->first << "->" << itr->second << endl;
		// 	itr++;
		// }
	}
	string result=str;
	for(int i = 0; i < str.length(); i++)
		result[i]=lang[str[i]];

	return result;
}

int main()
{
	int cases;
	cin >> cases;

	string line;
	getline(std::cin, line); // skip eol from cases input
	for(int i = 0; i < cases; i++)
	{
		getline(std::cin, line);
		cout << "Case #" << (i+1) << ": " << process(line) << endl; 
	}
}
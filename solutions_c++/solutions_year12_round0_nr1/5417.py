#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <algorithm>
#include <map>


using namespace std;

ifstream in("small.in");
ofstream out("small.out");

string inp[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
				 "de kr kd eoya kw aej tysr re ujdr lkgc jv", "yeq"};
string outp[] = {"our language is impossible to understand", "there are twenty six factorial possibilities",
				 "so it is okay if you want to just give up", "aoz"};

map <char, char> ans;
char c[110];

void Analyze()
{	
	ans[' '] = ' ';
	ans['z'] = 'q';
	for (int t = 0; t < sizeof(inp) / sizeof(inp[0]); ++t)
	{
		for (int i = 0; i < inp[t].size(); ++i)
		{
			if (ans.find(inp[t][i]) != ans.end() && ans[inp[t][i]] != outp[t][i])
			{
				cout << "Error" << endl;
			}

			ans[inp[t][i]] = outp[t][i];
		}
	}
}

int main()
{
	Analyze();

	int test,t;

	in >> test;
	
	in.getline(c,110);

	for (t = 1; t <= test; ++t)
	{
		in.getline(c,110);

		out << "Case #" << t << ": ";

		for (int i = 0 ; i < strlen(c); ++i)
			out << ans[c[i]];
		
		out << endl;
	}

	return 0;
}
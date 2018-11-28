#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <set>
#include <map>
#include <fstream>

char* s1[] =
{
	"ejp mysljylc kd kxveddknmc re jsicpdrysi",
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	"de kr kd eoya kw aej tysr re ujdr lkgc jv",
	"y qee z",
};

char* s2[] =
{
	"our language is impossible to understand",
	"there are twenty six factorial possibilities",
	"so it is okay if you want to just give up",
	"a zoo q",
};

std::map<char, char> e2g;
std::map<char, char> g2e;

void CreateTable()
{
	std::set<std::pair<char, char> > dic;

	for (int i = 0; i < 4; ++i)
	{
		int len = (int)strlen(s1[i]);
		for (int j = 0; j < len; ++j)
		{
			char c1 = s1[i][j];
			char c2 = s2[i][j];
			//if (c1 != ' ' && c2 != ' ')
			{
				dic.insert(std::pair<char, char>(c1, c2));
			}
		}
	}

// 	std::string alpha = "abcdefghijklmnopqrstuvwxyz";
// 	std::string a1 = alpha;
// 	std::string a2 = alpha;
// 	for (std::set<std::pair<char, char> >::iterator it = dic.begin(); it != dic.end(); ++it)
// 	{
// 		char c1;
// 
// 		c1 = it->first;
// 		for (int i = 0; i < (int)alpha.size(); ++i)
// 		{
// 			if (a1[i] == c1)
// 			{
// 				a1[i] = '-';
// 				break;
// 			}
// 		}
// 
// 		c1 = it->second;
// 		for (int i = 0; i < (int)alpha.size(); ++i)
// 		{
// 			if (a2[i] == c1)
// 			{
// 				a2[i] = '-';
// 				break;
// 			}
// 		}
// 	}

	for (std::set<std::pair<char, char> >::iterator it = dic.begin(); it != dic.end(); ++it)
	{
		char c1 = it->first;
		char c2 = it->second;
		e2g[c2] = c1;
		g2e[c1] = c2;
	}

	std::string s = s2[0];
	std::string s2 = s;
	for (int i = 0; i < (int)s.size(); ++i)
	{
		s2[i] = e2g[s[i]];
	}

	char tmp;
}

int main()
{
	CreateTable();

	std::ifstream fIn("./A-small-attempt3.in");
	std::ofstream fOut("./out.txt");

	int n;
	fIn >> n;

	std::string s;
	int count = 1;
	while( getline(fIn, s) )
	{
		if( s.empty() )
			continue;

		std::string s2(s);
		for (int j = 0; j < (int)s2.size(); ++j)
		{
			s2[j] = g2e[s[j]];
		}
		fOut << "Case #" << count++ << ": " << s2 << std::endl;
	}

	return 0;
}


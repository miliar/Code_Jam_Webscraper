#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
using namespace std;

void find_pattern(const char* str,int l,const set<string>& wordlist,string res,set<string>& outcome)
{
	if (res.size() == l) // enough
	{
		if (wordlist.find(res) != wordlist.end()) // find
		{
			outcome.insert(res);
		}
	}
	else
	{
		int offset = 0;
		vector<char> charlist;

		if (str[offset] != '(') // single
		{
			charlist.push_back(str[offset++]);
		}
		else
		{
			offset++; // for (

			while (str[offset] != ')')
			{
				charlist.push_back(str[offset++]);
			}

			offset++;
		}

		for (int i = 0; i != charlist.size(); i++)
		{
			bool f = false;
			int index = res.size() + 1;
			string newres = res + charlist[i];

			for (set<string>::const_iterator iter = wordlist.begin(); iter != wordlist.end(); iter++)
			{
				int k = 0;
				for (; k != newres.size(); k++)
				{
					if (newres[k] != (*iter)[k])
					{
						break;
					}
				}
				if (k == newres.size())
				{
					f = true;
					break;
				}
			}

			if (f)
			{
				find_pattern(str + offset,l,wordlist,res + charlist[i],outcome);
			}
		}
	}
}

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");

	int l,d,n;

	fin >> l >> d >> n;

	set<string> wordlist;

	for (int i = 0; i < d; i++)
	{
		string temp;
		fin >> temp;

		wordlist.insert(temp);
	}

	for (int j = 1; j <= n; j++)
	{
		set<string> outcome;

		string pattern;
		fin >>  pattern;

		find_pattern(pattern.c_str(),l,wordlist,"",outcome);

		fout << "Case #" << j << ": " << outcome.size() << endl;
	}

	fout.close();
	fin.close();

	return 0;
}
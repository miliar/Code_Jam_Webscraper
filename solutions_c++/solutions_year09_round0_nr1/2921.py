#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <set>


using namespace std;

int main()
{
	fstream file("A-large.in");
	ofstream outfile("Result.txt");

	if(!file)
	{
		cout << "no file" << endl;
		return -1;
	}

	int l,d,n;
	vector<string> wordList;

	file >> l >> d >> n;

	string s;
	for(int i = 0 ; i < d ; i ++)
	{
		file >> s;
		wordList.push_back(s);
	}

	int testCase(1);

	for(;testCase <= n ; testCase++)
	{
		vector<set<char>> pattern(l);
		int wordLoca(0);
		file >> s;
		while(s.length() != 0)
		{
			int nextChar(0);

			if(s[0] == '(')
			{
				nextChar = s.find_first_of(')');
				for(int i = 1 ; i < nextChar ; i ++)
				{
					pattern[wordLoca].insert(s[i]);
				}

			}
			else
			{
				pattern[wordLoca].insert(s[0]);
			}

			wordLoca ++;
			s = s.substr(nextChar + 1);
		}

		int count(0);
		for(int i = 0 ; i < d ; i ++)
		{
			bool exit(true);

			for(int j = 0 ; j < l ; j ++)
			{
				if(pattern[j].count(wordList[i][j]) == 0 )
				{
					exit = false;
					break;
				}
			}

			if(exit)
			{
				count ++;
			}	
		}

		outfile << "Case #" << testCase << ": " << count << endl;

	}

	file.close();
	outfile.close();
	return 0;
}
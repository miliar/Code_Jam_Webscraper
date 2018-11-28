#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int made(vector <string> have, vector <string> trab)
{
	int sh = have.size();
	int sw = trab.size();
	int mn = min(sh, sw);
	int counter = 0;
	while ((counter < mn) && (have[counter] == trab[counter]))
	{
		++counter;
	}
	return sw - counter;
}

int main()
{
	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);	
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int N;
		int M;
		cin >> N >> M;
		vector <vector <string> > home;		
		for (int j = 0; j < N; ++j)
		{
			string input;
			cin >> input;
			vector <string> inp;
			int length = input.length();
			string word = "";
			for (int k = 0; k < length; ++k)
			{
				if (input[k] != '/')
				{
					word += input[k];
				}
				else
				{
					if (word != "")
					{
						inp.push_back(word);
						word = "";
					}
				}
			}
			if (word != "") 
			{
				inp.push_back(word);
			}
			home.push_back(inp);
		}
		int mkdir = 0;
		for (int j = 0; j < M; ++j)
		{
			string input;
			cin >> input;
			vector <string> inp;
			int length = input.length();
			string word = "";
			for (int k = 0; k < length; ++k)
			{
				if (input[k] != '/')
				{
					word += input[k];
				}
				else
				{
					if (word != "")
					{
						inp.push_back(word);
						word = "";
					}
				}
			}
			if (word != "") 
			{
				inp.push_back(word);
			}
			int size = home.size();
			int mn = inp.size();
			for (int k = 0; k < size; ++k)
			{
				int md = made(home[k], inp);
				if (md < mn)
				{
					mn = md;
				}
			}
			mkdir += mn;
			home.push_back(inp);
		}
		cout << "Case #" << i + 1 << ": " << mkdir << endl;		
	}
	return 0;
}

#include <iostream>
#include <string>

using namespace std;

char com[26][26];
bool opp[26][26];

string process(string line)
{
	int s = line.size();
	if (s <= 1)
		return line;
	int i;
	if (com[line[s-1]-'A'][line[s-2]-'A'] != -1)
	{
		line[s-2] = com[line[s-1]-'A'][line[s-2]-'A'];		
		line.resize(s-1);
		return process(line);	
	}
	for (i = 0; i < s-1; ++i)
	{
		if (opp[line[i]-'A'][line[s-1]-'A'])
		{
			line = "";
			break;
		}
	}
	return line;
}

int main()
{
	int T, t, N;
	int C, D, i, j;
	char c1, c2, c3, c;
	string line;
	cin >> T;
	for (t = 0; t < T; ++t)
	{
		for (i = 0; i < 26; ++i)
		{
			for (j = 0; j < 26; ++j)
			{
				com[i][j] = -1;
				opp[i][j] = false;
			}
		}

		cin >> C;
		for (i = 0; i < C; ++i)
		{
			cin >> c1 >> c2 >> c3;
			com[c1-'A'][c2-'A'] = c3;
			com[c2-'A'][c1-'A'] = c3;
		}

		cin >> D;
		for (i = 0; i < D; ++i)
		{
			cin >> c1 >> c2;
			opp[c1-'A'][c2-'A'] = true;
			opp[c2-'A'][c1-'A'] = true;
		}

		line = "";
		cin >> N;
		cin >> c;
		line += c;
		for (i = 1; i < N; ++i)
		{
			cin >> c;
			line += c;
			line = process(line);			
		}
		cout << "Case #" << t+1 << ": [";
		for (i = 0; i < line.size(); ++i)
		{
			cout << line[i];
			if (i < line.size()-1)
				cout << ", ";
		}
		cout << "]" << endl;
	}
	return 0;
}
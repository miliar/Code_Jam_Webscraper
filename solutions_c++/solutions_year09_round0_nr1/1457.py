#include <iostream>
#include <string>
#include <vector>

using namespace std;

int states[500][15][26];

int main(int argc, char** argv)
{
	memset(states, 0, sizeof(states));

	int L, D, N;
	{
		char temp[100];
		cin.getline(temp, 100);
		sscanf(temp, "%d %d %d", &L, &D, &N);
	}
	
	vector<string> dict;
	for (int i = 0; i < D; i++)
	{
		char temp[100];
		cin.getline(temp, 100);
		
		string s = temp;

		dict.push_back(temp);
	}
	
	for (int i = 0; i < N; i++)
	{
#define maxlen (15 * (26 + 2) + 1)
		char temp[maxlen];
		
		cin.getline(temp, maxlen);
		
		string s = temp;
		int stind = 0;
		
		for (int j = 0; j < L; j++)
		{
			if (s[stind] == '(')
			{
				stind++;
				while(s[stind] != ')')
				{
					states[i][j][s[stind] - 'a'] = 1;
					stind++;
				}
				stind++;
			}
			else
			{
				states[i][j][s[stind] - 'a'] = 1;
				stind++;
			}
		}
	}

	
	for (int i = 0; i < N; i++)
	{
		int count = 0;
		for (int j = 0; j < D; j++)
		{
			bool match = true;
			for (int k = 0; k < L; k++)
			{
				if (states[i][k][dict[j][k] - 'a'] == 0)
				{
					match = false;
					break;
				}
				
			}
			if (match) count++;			
		}
		
		cout << "Case #" << i + 1 << ": " << count << endl;
	}

}
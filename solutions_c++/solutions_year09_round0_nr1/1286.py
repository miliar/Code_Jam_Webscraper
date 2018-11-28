#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

bool possLetter[15][26];

int main()
{
	freopen("large.in",  "r", stdin);
	freopen("output.txt", "w", stdout);

	int L, D, N;
	cin >> L >> D >> N;

	vector<string> words(D);

	
	

	for (int i = 0; i < D; i++)
	{
		cin >> words[i];
	}
	
	for (int i = 0; i < N; i++)
	{
		string mess;
		cin >> mess;
		for (int j = 0; j < L; j++)
			for (int h = 0; h < 26; h++)
				possLetter[j][h] = false;

		int pos = 0;
		bool isInside = false;
		for (int j = 0; j < mess.length(); j++)
		{
			if (mess[j] == '(')
			{
				isInside = true;
				int h = j + 1;
				while (mess[h] != ')') 
				{
					possLetter[pos][ mess[h] - 'a'] =  true;
					h++;
					
				}
				pos++;
			}
			if (mess[j] == ')') isInside = false;

			if (!isInside && mess[j] != '(' && mess[j] != ')' )
			{
				possLetter[pos][ mess[j] - 'a'] =  true;
				pos++;
			}
		}

		int ans = 0;
		for (int j = 0; j < D; j++)
		{
			bool flag = true;
			for (int h = 0; h < L; h++)
				if (!possLetter[h][ words[j][h] - 'a']) flag = false;

			if (flag) ans++;
		}

		cout << "Case #" << i + 1 << ": " << ans <<endl;
	}

	return 0;
}
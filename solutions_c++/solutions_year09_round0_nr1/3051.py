#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
using namespace std;

int L, D, N;
string word, pattern;
vector <string> t;
int c;

struct TRI{
	int ch[26];

	TRI()
	{
		int i;
		for (i = 0; i < 26; i ++)
			ch[i] = -1;
	}

} T[5000*16];

void init()
{
	int i, j, id;
	int p;

	c = 1;
	for (i = 0; i < D; i ++)
	{
		cin >> word;
		id = 0;
		for (j = 0; j < L; j ++)
		{
			p = word[j]-'a';
			if (T[id].ch[p] == -1)
			{
				T[id].ch[p] = c ++;
			}

			id = T[id].ch[p];
		}
	}
}

int getans(int r, int s)
{
	if (s == L) return 1;

	int i, ans = 0;

	for (i = 0; i < t[s].size(); i ++)
	{
		int p = t[s][i] - 'a';
		if (T[r].ch[p] != -1)
			ans += getans(T[r].ch[p], s+1);
	}

	return ans;
}

int main()
{
	freopen("A_ans.txt", "w", stdout);
	int i, j, k, ans;

	cin >> L >> D >> N;
	
	init();

	for (i = 0; i < N; i ++)
	{
		ans = 0;
		cin >> pattern;

		t.clear();
		for (j = 0; j < pattern.size(); j ++)
		{
			if (pattern[j] == '(')
			{
				k = j+1;
				while (pattern[k] != ')') k ++;
				{
					t.push_back(pattern.substr(j+1, k-j-1));
				}
				j = k;
			}
			else
			{
				t.push_back(pattern.substr(j, 1));
			}
		}

		cout << "Case #" << i+1 << ": " << getans(0, 0) << endl;
	}

	return 0;
}

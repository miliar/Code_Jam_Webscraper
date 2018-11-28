#include <stdio.h>
#include <vector>
#include <map>
#include <stack>
#include <math.h>
#include <algorithm>

using namespace std;

int combine[26][26];
bool opposite[26][26];

int main()
{
	freopen("out.txt", "w", stdout);
	freopen("in.txt", "r", stdin);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		int N;
		for (int i = 0; i < 26; i++)
			for (int j = 0; j < 26; j++)
			{
				combine[i][j] = -1;
				opposite[i][j] = false;
			}
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			char s[1000];
			scanf("%s", s);
			combine[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
			combine[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
		}
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			char s[1000];
			scanf("%s", s);
			opposite[s[0] - 'A'][s[1] - 'A'] = true;
			opposite[s[1] - 'A'][s[0] - 'A'] = true;
		}
		scanf("%d", &N);
		char p[1000];
		scanf("%s", p);
		vector<int> v;
		for (int i = 0; p[i]; i++)
		{
			v.push_back(p[i] - 'A');
			if (v.size() > 1)
			{
				int a = combine[v[v.size()- 1]][v[v.size()- 2]];
				if (a != -1)
				{
					v.pop_back();
					v.pop_back();
					v.push_back(a);
				}
				bool f = false;
				for (int j = 0; j < v.size() - 1; j++)
					if (opposite[v[v.size()- 1]][v[j]])
					{
						f = true;
					}
				if (f)
					v.clear();
			}
		}
		printf("Case #%d: [", t + 1);
		for (int i = 0; i < v.size(); i++)
		{
			if (i > 0)
				printf(", ");
			printf("%c", 'A' + v[i]);
		}
		printf("]\n");
	}

	return 0;
}
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

char combo[27][27];
bool kills[27][27];

void process(vector<char>& in)
{
	bool change;
	do
	{
		change = false;
		if (in.size() > 1)
		{
			change = true;
			char a = in[in.size()-1];
			char b = in[in.size()-2];
			if (combo[a][b] != -1)
			{
				in.resize(in.size()-2);
				in.push_back(combo[a][b]);
			}
			else
			{
				bool kill = false;
				for (int i = 0, s = in.size(); i < s; ++i)
					if (kills[a][in[i]] || kills[b][in[i]])
					{
						kill = true;
						break;
					}
				if (kill)
					in.clear();
				else
					change = false;
			}
		}
	}
	while (change);
}

int main()
{
	int n, c, d, s;
	char x, y, z;
	scanf("%d", &n);
	
	for (int q = 1; q <= n; ++q)
	{
		memset(combo, -1, sizeof combo);
		memset(kills, 0, sizeof kills);
		scanf(" %d ", &c);
		for (int i = 0; i < c; ++i)
		{
			scanf(" %c %c %c ", &x, &y, &z);
			x -= 'A'; y -= 'A'; z -= 'A';
			combo[x][y] = z;
			combo[y][x] = z;
		}
		scanf(" %d ", &d);
		for (int i = 0; i < d; ++i)
		{
			scanf(" %c %c ", &x, &y);
			x -= 'A'; y -= 'A';
			kills[x][y] = true;
			kills[y][x] = true;
		}
		scanf(" %d ", &s);
		vector<char> in;
		for (int i = 0; i < s; ++i)
		{
			scanf(" %c ", &x);
			x -= 'A';
			in.push_back(x);
			process(in);
		}
		printf("Case #%d: [", q);
		if (in.size())
			printf("%c", in[0] + 'A');
		for (int i = 1, t = in.size(); i < t; ++i)
			printf(", %c", in[i] + 'A');
		printf("]\n");
	}
	
	return 0;
}


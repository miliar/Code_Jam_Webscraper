#include <cstdio>
#include <vector>
#include <string>

using namespace std;

vector<string> vec;

vector<string> Solve()
{
	bool can = true;
	for (int i=0; i<vec.size(); i++)
	{
		for (int j=0; j<vec[i].size(); j++)
		{
			if (vec[i][j] == '#')
			{
				vec[i][j] = '/';
				if (i+1<vec.size())
				{
					if (vec[i+1][j] == '#')
						vec[i+1][j] = '\\';
					else
						can = false;
				}
				else
					can = false;
				if (j+1<vec[i].size())
				{
					if (vec[i][j+1] == '#')
						vec[i][j+1] = '\\';
					else
						can = false;
				}
				else
					can = false;
				if (i+1<vec.size() && j+1<vec[i].size())
				{
					if (vec[i+1][j+1] == '#')
						vec[i+1][j+1] = '/';
					else
						can = false;
				}
				else
					can = false;
			}
		}
	}

	if (can == false)
	{
		vec.clear();
	}
	return vec;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		int r,c;
		scanf("%d%d", &r, &c);

		char buf[100];
		vec.clear();
		for (int x=0; x<r; x++)
		{
			scanf("%s", buf);
			string s = buf;
			vec.push_back(s);
		}

		vector<string> res = Solve();

		if (res.size() == 0)
		{
			printf("Case #%d:\n%s\n", t, "Impossible");
		}
		else
		{
			
			printf("Case #%d:\n", t);
			for (int x=0; x<r; x++)
			{
				for (int y=0; y<c; y++)
				{
					printf("%c", res[x][y]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}
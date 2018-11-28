#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("D-small-attempt0.in.txt");
ofstream fout("D-small-attempt0.out.txt");

char s[1024], news[1024];
int n, k;

int used[10];
int per[10];

int ans;

void dfs(int step)
{
	if (step == k)
	{
		int m = strlen(s);
		for (int i = 0; i < m / k; i++)
		{
			for (int j = 0; j < k; j++)
				news[i*k + j] = s[ i*k + per[j] ];
		}

		int count = 0;
		for (int i = 0; i < m; i++)
		{
			if (i == 0 || news[i] != news[i-1]) count++;			
		}
		if (count < ans) ans = count;

		return;
	}

	for (int i = 0; i < k; i++)
		if (used[i] == 0)
		{
			per[step] = i;
			used[i] = 1;
			dfs(step+1);
			used[i] = 0;			
		}
}

int main()
{
	fin >> n;
	for (int cases = 1; cases <= n; cases++)
	{
		fin >> k;
		fin >> s;

		memset(used, 0, sizeof(used));
		memset(news, 0, sizeof(news));

		ans = strlen(s);

		dfs(0);

		fout << "Case #" << cases << ": " << ans << endl;
		

	}

	return 0;
}

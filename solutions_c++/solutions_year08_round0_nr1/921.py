#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("A-large.in.txt");
ofstream fout("A-large.out.txt");


int ans;
int n, server, query;

char s_name[256][512];
char q_id[1024];
int f[1024][256];

int findserver(char * q_name)
{
	for (int i = 0; i < server; i++)
		if (strcmp(q_name, s_name[i]) == 0)
			return i;
	return -1;
}

int main()
{
	char s[1024];

	fin.getline(s, 1024);
	sscanf(s, "%d", &n);

	for (int cases = 1; cases <= n; cases++)
	{
		memset(s_name, 0, sizeof(s_name));

		memset(s, 0, sizeof(s));
		fin.getline(s, 1024);
		sscanf(s, "%d", &server);

		for (int i = 0; i < server; i++)
		{
			fin.getline(s_name[i], 1024);
		}

		memset(s, 0, sizeof(s));
		fin.getline(s, 1024);
		sscanf(s, "%d", &query);

		for (int i = 0; i < query; i++)
		{
			memset(s, 0, sizeof(s));
			fin.getline(s, 1024);

			q_id[i] = findserver(s);
		}
		
		memset(f, 0, sizeof(f));

		if (query == 0)
			ans = 0;
		else
		{
			for (int j = 0; j < server; j++)				
				if (q_id[0] == j)
					f[0][j] = 10000;
				else
					f[0][j] = 0;

			for (int i = 1; i < query; i++)
				for (int j = 0; j < server; j++)
				{
					f[i][j] = 10000;
					
					if (q_id[i] == j) continue;

					for (int k = 0; k < server; k++)
					{
						if (k == j && f[i-1][k] < f[i][j])
							f[i][j] = f[i-1][k];
						if (k != j && f[i-1][k] + 1 < f[i][j])
							f[i][j] = f[i-1][k] + 1;
					}				
				}

			ans = 10000;
			for (int j = 0; j < server; j++)
				if (f[query-1][j] < ans) ans = f[query-1][j];
		}

		fout << "Case #" << cases << ": " << ans << endl;
	}

	return 0;
}
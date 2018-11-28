#include <stdio.h>
#include <memory.h>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int matr[100][1001];

map<string, int> qm;

int min(int a, int b)
{
	return a < b ? a : b;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int N;
	scanf("%d", &N);

	int S, Q;
	char p[1000];
	char * s = p;
	for (int t = 0; t < N; t++)
	{
		scanf("%d", &S);
		gets(s);		
		qm.clear();
		int c = 0;
		for (int i = 0; i < S; i++)
		{
			s = gets(s);
			string ss = s;
			if (qm.find(ss) == qm.end())
			{
				qm[ss] = c;
				c++;
			}
		}
		scanf("%d", &Q);
		gets(s);
		for (int i = 0; i < 100; i++)
			for (int j = 0; j < 1000; j++)
				matr[i][j] = 2000000000;
		for (int i = 0; i < 100; i++)
			matr[i][0] = 0;
		for (int i = 0; i < Q; i++)
		{
			s = gets(s);
			string ss = s;
			int a;
			if (qm.find(ss) == qm.end())
				a == -1;
			else
				a = qm[s];
			for (int j = 0; j < S; j++)
			{
				for (int k = 0; k < S; k++)
				{
					if (k != a)
					{
						if (k == j)
							matr[k][i+1] = min(matr[j][i], matr[k][i+1]);
						else
							matr[k][i+1] = min(matr[j][i] + 1, matr[k][i+1]);
					}
				}
			}
		}

		int res = 2000000000;
		for (int i = 0; i < S; i++)
			res = min(res, matr[i][Q]);

		printf("Case #%d: %d\n", t + 1, res);


	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
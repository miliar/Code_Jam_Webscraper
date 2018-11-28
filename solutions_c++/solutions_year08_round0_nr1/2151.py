#include <cstdio>
#include <string>
#include <map>
#include <iostream>

using namespace std;

const int MaxN = 110;
const int MaxQ = 1010;

int N, Q;
map<string, int> name;
int q[MaxQ];
int f[MaxQ][MaxN];

int main()
{
	int runs;
	string tmp;
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	cin >> runs;
	for (int t = 0; t < runs; t++)
	{
		cin >> N;
		getline(cin, tmp);
		name.clear();
		for (int i = 0; i < N; i++)
		{
			getline(cin, tmp);
			name[tmp] = i;
		}
		cin >> Q;
		getline(cin, tmp);
		for (int i = 0; i < Q; i++)
		{
			getline(cin, tmp);
			q[i] = name[tmp];
		}

		fill(f[0], f[Q+1], INT_MAX);
		for (int j = 0; j < N; j++)
			f[0][j] = 0;
		for (int i = 0; i < Q; i++)
			for (int j = 0; j < N; j++)
			{
				if (f[i][j] == INT_MAX) continue;
				if (j != q[i])
					f[i+1][j] = min(f[i+1][j], f[i][j]);
				else
					for (int k = 0; k < N; k++)
						if (k != q[i])
							f[i+1][k] = min(f[i+1][k], f[i][j] + 1);
			}
/*		for (int i = 0; i <= Q; i++)
		{
			for (int j = 0; j < N; j++)
				printf ("%d ", f[i][j]);
			printf ("\n");
		} */
		int ans = INT_MAX;
		for (int i = 0; i < N; i++)
			ans = min(ans, f[Q][i]);
		printf ("Case #%d: %d\n", t+1, ans);			
	}
}


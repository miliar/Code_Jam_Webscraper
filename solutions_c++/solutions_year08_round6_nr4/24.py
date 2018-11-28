#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

int matrix[8][8];
int sub[8][8];
int lis[] = {0, 1, 2, 3, 4, 5, 6, 7};

int main()
{
	int N;
	cin >> N;
	for(int t = 1; t <= N; ++t)
	{
		int n, m;
		cin >> n;
		memset(matrix, 0, 8 * 8 * 4);
		memset(sub, 0, 8 * 8 * 4);
		for(int i = 0; i < n - 1; ++i)
		{
			int a, b;
			cin >> a >> b;
			--a; --b;
			matrix[a][b] = matrix[b][a] = 1;
		}
		cin >> m;
		for(int i = 0; i < m - 1; ++i)
		{
			int a, b;
			cin >> a >> b;
			--a; --b;
			sub[a][b] = sub[b][a] = 1;
		}
		bool ok = false;
		do
		{
			bool is_ok = true;
			for(int i = 0; i < m && is_ok; ++i)
			{
				for(int j = i + 1; j < m && is_ok; ++j)
				{
					is_ok = matrix[lis[i]][lis[j]] == sub[i][j];
				}
			}
			ok = ok || is_ok;
		}while(next_permutation(lis, lis + n));
		printf("Case #%d: ", t);
		if(ok) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}

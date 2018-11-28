#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std; 
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("GCJ_A.txt", "w", stdout);
	int T, tcnt = 0;
	int move[200][2];
	scanf("%d", &T);
	while (T--)
	{
		int N;
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
		{
			char col[3];
			scanf("%s %d", col, &move[i][1]);
			if (col[0] == 'O')
				move[i][0] = 0;
			else
				move[i][0] = 1;
		}
		int x[2];
		x[1] = x[0] = 1;
		int ans = 0;
		for (int i = 0; i < N; i++)
		{
			int s = abs(move[i][1] - x[move[i][0]]) + 1;
			//printf("%d\n", s);
			ans += s;
			x[move[i][0]] = move[i][1];
			int nxt = x[move[i][0] ^ 1];
			for (int j = i + 1; j < N; j++)
				if (move[j][0] == (move[i][0] ^ 1))
				{
					nxt = move[j][1];
					break;
				}
			int bs = s < abs(nxt - x[move[i][0] ^ 1]) ? s : abs(nxt - x[move[i][0] ^ 1]);
			if (nxt > x[move[i][0] ^ 1])
				x[move[i][0] ^ 1] += bs;
			else
				x[move[i][0] ^ 1] -= bs;
		}
		++tcnt;
		cout << "Case #" << tcnt << ": " << ans << endl;
		
	}
	return 0;
}

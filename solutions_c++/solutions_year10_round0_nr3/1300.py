# include <cstdio>
# include <iostream>
using namespace std;


__int64 appR[100000010];
int  z[1010], first[1010];

int main()
{
	int t, i, R, k, N, remain, start, game, circle;
	__int64 total, ans;


//	freopen("C-large.in", "rt", stdin);
//	freopen("C-large.out1", "wt", stdout);
	
	cin >> t;
	for (game = 1; game <= t; game++)
	{
		total = ans = start = 0;
		cin >> R >> k >> N;
		for (i = 0; i < N; i++)
		{
			cin >> z[i];
			total += z[i];
		}
		cout << "Case #" << game << ": ";
		if (total <= k)	printf("%I64d\n", total * R);
		else
		{
			ans = start = 0;
			memset(first, 0, sizeof(first));
			first[0] = R;
			appR[R] = 0;
			remain = k;
			while (R)
			{
				if (remain >= z[start]) 
				{
					ans += z[start];
					remain -= z[start];
					start = (start < N - 1) ? (start + 1) : 0; 					
				} 
				else
				{
					R--;
					remain = k;
					appR[R] = ans;
					if (!first[start]) first[start] = R;											
					else
					{
						circle = first[start] - R;
						ans += (R / circle) * (appR[R] - appR[first[start]]);
						if (R % circle) 
							ans += appR[first[start] - (R % circle)] - appR[first[start]];
						R = 0;
					}
				}
			}
			printf("%I64d\n", ans);
		}
	}
	
	return 0;
}
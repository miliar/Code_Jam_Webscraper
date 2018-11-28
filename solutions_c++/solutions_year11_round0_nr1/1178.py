#include <iostream>
#include <math.h>
#include <stdlib.h>

using namespace std;

#define MAX 128

char S[MAX];
int B[MAX];
int ans[MAX];

int main()
{
	int t;
	///freopen("A-large.in", "r", stdin);
	//freopen("A.out", "w", stdout);
	cin >> t;
	int Case = 0;
	while (t--)
	{
		int m;
		cin >> m;
		for (int i = 1; i <= m; ++i)
		{
			cin >> S[i] >> B[i];
		}
		for (int i = 1; i <= m; ++i)
		{
			int last = 1;
			int tim = 0;
			for (int j = i - 1; j > 0; --j)
			{
				if (S[j] == S[i])
				{
					last = B[j];
					tim = ans[j];
					break;
				}
			}
			int cnt = tim + abs(B[i] - last) + 1;
			tim = 0;
			for (int j = i - 1; j > 0; --j)
			{
				if (S[j] != S[i])
				{
					tim = ans[j];
					break;
				}
			}
			if (cnt <= tim) cnt = tim + 1;
			ans[i] = cnt;
		}
		printf("Case #%d: %d\n", ++Case, ans[m]);
	}
	return 0;
}



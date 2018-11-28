#include <iostream>
#include <cstdio>
#define maxN 10000

using std::cin;
using std::cout;
using std::endl;

int R, K, N;
long long a[maxN], S[maxN], pans[maxN];
int b[maxN], l[maxN];

long long
sum(int l, int r)
{
	long long a = 0;
	for (int i = l; i < r; i++)
		a += pans[i];
	return(a);
}

int
main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T, z;
	cin >> T;
	for (z = 1; z <= T; z++)
	{
		cin >> R >> K >> N;
		int i, j;
		for (i = 0; i < N; i++)
			cin >> a[i];
		for (i = 0; i < N; i++)
		{
			S[i] = 0;
			b[i] = i;
			for (j = 0; j < N; j++)
				if (S[i] + a[(i + j) % N] > K)
				{
					b[i] = (i + j) % N;
					break;
				}
				else
					S[i] += a[(i + j) % N];
		}
		for (i = 0; i < N; i++)
			l[i] = -1;
		long long Ans = 0;
		j = 0;
		for (i = 0; i < R; i++)
			if (l[j] >= 0)
			{
				int loop = i - l[j], remain = R - i;
				Ans += remain / loop * sum(l[j], i) + sum(l[j], l[j] + remain % loop);
				break;
			}
			else
			{
				l[j] = i;
				pans[i] = S[j];
				Ans += S[j];
				j = b[j];
			}
		cout << "Case #" << z << ": " << Ans << endl;
	}
	return(0);
}

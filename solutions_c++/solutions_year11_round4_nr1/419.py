#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define maxN 2000

using namespace std;

long double X, S, R, t;
int N;
long double B[maxN], E[maxN], W[maxN];
long double length[maxN];
int q[maxN];
const long double eps = 1e-10;

bool cmp(int left, int right)
{
	return W[left] < W[right];
}

int main()
{
	int T;
	cin >> T;
	for (int z = 1; z <= T; z++)
	{
		cin >> X >> S >> R >> t >> N;
		length[0] = X;
		W[0] = 0;
		for (int i = 1; i <= N; i++)
		{
			cin >> B[i] >> E[i] >> W[i];
			length[i] = E[i] - B[i];
			length[0] -= length[i];
			q[i] = i;
		}
		sort(q + 1, q + N + 1, cmp);
		q[0] = 0;
		long double Ans = 0;
		for (int i = 0; i <= N; i++)
		{
			long double need = length[q[i]] / (W[q[i]] + R);
			if (t >= need - eps)
			{
				t -= need;
				Ans += need;
			}
			else
			{
				Ans += t;
				length[q[i]] -= t * (W[q[i]] + R);
				for (int j = i; j <= N; j++)
					Ans += length[q[j]] / (W[q[j]] + S);
				break;
			}
		}
		printf("Case #%d: ", z);
		cout.precision(16);
		cout << Ans << endl;
	}
	return 0;
}


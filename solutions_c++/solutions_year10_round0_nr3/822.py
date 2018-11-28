#include <iostream>

using namespace std;

const int MAX_N = 1004;

long long g[MAX_N], m[MAX_N], t[MAX_N];
int next[MAX_N];
int mark[MAX_N];

int main()
{
	int nTests;
	cin >> nTests;
	long long R, k;
	for (int run = 1; run <= nTests; ++run)
	{
		int n;
		cin >> R >> k >> n;
		for (int i = 0; i < n; ++i)
			cin >> g[i];
		for (int i = 0; i < n; ++i)
		{
			long long s = g[i];
			int j = (i+1)%n;
			while (j != i && s + g[j] <= k) 
			{
				s += g[j];
				j = (j+1)%n;
			}
			next[i] = j;
			m[i] = s;
		}
		memset(mark, 0, sizeof(mark));
		int cur = 0;
		t[0] = 0;
		for (int i=1; i <= n+1; ++i)
		{
			if (i == R) 
			{
				cout << "Case #" << run << ": " << t[i-1] + m[cur] << endl;
				break;
			}
			if (mark[cur] > 0)
			{
				int j = mark[cur];
				long long k = (R - (j-1)) % (i-j);
				long long total = (t[j-1]) + ((R - (j-1)) / (i-j)) * (t[i-1]-t[j-1]) + (t[k+j-1] - t[j-1]);
				cout << "Case #" << run << ": " << total << endl;
				break;
			}
			t[i] = t[i-1] + m[cur];
			mark[cur] = i;
			cur = next[cur];
		}
	}
	return 0;
}

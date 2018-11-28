#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cstring>

using namespace std;

const int MaxN = 105;
int N, L, H;
int freq[MaxN];

int doit()
{
	for (int i = L; i <= H; ++i)
	{
		bool ok = true;
		for (int j = 0; j < N; ++j)
		{
			if (i % freq[j] != 0 && freq[j] % i != 0)
			{
				ok = false;
				break;
			}
		}
		if (ok) return i;
	}
	return -1;
}

int main()
{
	int Ncase;
	freopen("c_small.in", "r", stdin);
	freopen("c_small.out", "w", stdout);
	cin >> Ncase;
	for (int run = 0; run < Ncase; ++run)
	{
		cin >> N >> L >> H;
		for (int i = 0; i < N; ++i)
			cin >> freq[i];

		int ans = doit();
		cout << "Case #" << run+1 << ": ";
		if (ans == -1) cout << "NO";
		else cout << ans;
		cout << endl;
	}
}

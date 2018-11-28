#pragma comment(linker, "/STACK:16777216")
#include <queue>
#include <cassert>
#include <sstream>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <iostream>
using namespace std;
typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VL;
typedef pair<int, int> PII;

int R, K, N;
VI Q;
VL psum;
LL Sum(int a, int b)
{
	a = a % N;
	b = b % N;
	if (a < b)
		return psum[b] - psum[a];
	else
		return psum[N] - psum[a] + psum[b] - psum[0];
}
LL Find(int a, int& b)
{
	int L = a + 1;
	int R = a + N;
	while (L < R)
	{
		int m = L + (R - L + 1) / 2;
		LL s = Sum(a, m);
		if (s <= K)
		{
			L = m;
		}
		else
		{
			R = m - 1;
		}		
	}
	b = L % N;
	return Sum(a, L);
}
void Go1()
{
	cin >> R >> K >> N;
	Q.clear();
	psum.clear();
	Q.resize(N);
	psum.resize(N + 1);
	for (int i = 0; i < N; i++)
	{
		cin >> Q[i];
		psum[i + 1] = psum[i] + Q[i];
	}
	LL res = 0;
	int a = 0;
	for (int i = 0; i < R; i++)
	{
		res += Find(a, a);
	}
	cout << res;
}
void Go2()
{
	cin >> R >> K >> N;
	Q.clear();
	psum.clear();
	Q.resize(N);
	psum.resize(N + 1);
	for (int i = 0; i < N; i++)
	{
		cin >> Q[i];
		psum[i + 1] = psum[i] + Q[i];
	}
	LL res = 0;
	int a = 0;
	VL sc(N, -1);
	VI pa;
	for (int i = 0; i < R; i++)
	{
		if (sc[a] != -1)
		{
			int rem = R - i;
			int st = 0;
			for (int j = 0; j < pa.size(); j++)
			{
				if (pa[j] == a)
				{
					st = j;
					break;
				}
			}
			int cnt = pa.size() - st;
			if (rem >= cnt)
			{
				LL ss = 0;
				for (int j = st; j < pa.size(); j++)
				{					
					ss += sc[pa[j]];
				}
				res += ss * (rem / cnt);
				rem %= cnt;
			}
			for (int j = 0; j < rem; j++)
			{
				res += sc[pa[st + j]];
			}
			break;
		}
		else
		{
			int na;
			sc[a] = Find(a, na);
			res += sc[a];
			pa.push_back(a);
			a = na;
		}
	}
	cout << res;
}

int main()
{
#ifdef _DEBUG
	freopen("inp.txt", "r", stdin);
#else
	const string file_name = "C-large";
	freopen((file_name + ".in").c_str(), "r", stdin);
	freopen((file_name + ".out").c_str(), "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for (int yy = 1; yy <= t; yy++)
	{
		printf("Case #%d: ", yy);
		Go2();
		printf("\n");
	}
	return 0;
}
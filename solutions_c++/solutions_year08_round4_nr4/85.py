#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:64000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
//#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<bool> vb;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))

#define forn(i, x) for (int i = 0; i < int(x); i++)
#define fors(i, x) forn(i, sz(x))

template<typename T> T sqr(T x) { return x * x;            }
template<typename T> T abs(T x) { return (x > 0) ? x : -x; }

int K;
string S;
int A[20][20];
int B[20][20];
int opt[1 << 16][16][16];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	cin >> nt;
	forn(it, nt)
	{
		cin >> K;
		cin >> S;
		int N = sz(S);
		memset(A, 0, sizeof(A));
		memset(B, 0, sizeof(B));
		for (int i = 0; i < K; i++)
			for (int j = 0; j < K; j++)
				for (int k = 0; k < N / K; k++)
				{
					if (S[k * K + i] == S[k * K + j]) A[i][j]++;
					if (k == N / K - 1) continue;
					if (S[k * K + i] == S[(k + 1) * K + j]) B[i][j]++;
				}
		memset(opt, 0, sizeof(opt));
		forn(i, (1 << K) - 1) forn(j, K) forn(k, K)
		{
			if (((i >> j) & 1) == 0) continue;
			if (((i >> k) & 1) == 0) continue;
			forn(l, K)
			{
				if ((i >> l) & 1) continue;
				int nmask = i | (1 << l);
				int add = A[k][l];
				if (nmask == (1 << K) - 1) add += B[l][j];
				opt[nmask][j][l] >?= opt[i][j][k] + add;
			}
		}
		int ans = 0;
		forn(j, K) forn(k, K) ans >?= opt[(1 << K) - 1][j][k];
		printf("Case #%d: %d\n", it + 1, N - ans);
		cerr << it << "\n";
	}
	return 0;
}

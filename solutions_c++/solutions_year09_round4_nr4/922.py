#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <bitset>
#include <list>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

const double PI = acos(-1.0);

#define FOR(k,a,b) for(typeof(a) k=(a); k < (b); ++k)
#define FORREV(k,a,b) for(typeof(b) k=(b); (a) <= (--k);)
#define two(X) (1<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define RA(x) (x).begin(), (x).end()
#define SZ(x) ((int) (x).size())
#define LN(x) ((int) (x).length())

template<class T> void checkmin(T& a, T b) { if (b < a) a = b; }
template<class T> void checkmax(T& a, T b) { if (b > a) a = b; }
template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

ifstream fin("in.txt");
ofstream fout("out.txt");

int T, N;
int X[100], Y[100], R[100];

double sqr(int x) { return x * x; }

double dis(int a, int b)
{
	return sqrt(sqr(X[a] - X[b]) + sqr(Y[a] - Y[b]));
}

int cross(int a, int b, int c)
{
	return (X[b] - X[a]) * (Y[c] - Y[b]) - (X[c] - X[b]) * (Y[b] - Y[a]);
}

double radius(int a, int b, int c)
{
	double l1 = dis(a, b);
	double l2 = dis(b, c);
	double l3 = dis(c, a);
	double S = abs(cross(a, b, c) / 2.0);
	if (S < 1e-12) return max(max(l1, l2), l3) / 2;
	return (l1 * l2 * l3 / (4 * S)) + max(max(R[a], R[b]), R[c]);
}

double calc(int s)
{
	int id[100];
	int M = 0;
	for (int i = 0; i < N; ++i)
		if (((1 << i) & s) > 0) id[M++] = i;
	if (M == 0) return 0;
	if (M == 1) return R[id[0]];
	if (M == 2) return (dis(id[0], id[1]) + R[id[0]] + R[id[1]]) / 2;

	double max = 0;
	for (int i = 0; i < M - 2; ++i)
		for (int j = i + 1; j < M - 1; ++j)
			for (int k = j + 1; k < M; ++k)
			{
				double temp = radius(id[i], id[j], id[k]);
				if (temp > max) max = temp;
			}
	return max;
}

void solve()
{
	fin >> N;
	for (int i = 0; i < N; ++i)
		fin >> X[i] >> Y[i] >> R[i];
	double ans = 1e30;
	for (int i = 0; i < (1 << N); ++i)
	{
		double r1 = calc(i);
		double r2 = calc(~i);
		double temp = max(r1, r2);
		if (temp < ans) ans = temp;
	}
	fout << fixed << setprecision(6) << ans << endl;
}

int main()
{
	fin >> T;
	for (int cas = 1; cas <= T; ++cas)
	{
		fout << "Case #" << cas << ": ";
		solve();
	}
	fin.close();
	fout.close();
	return 0;
}

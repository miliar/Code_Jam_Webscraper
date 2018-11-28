#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
const int INF = 1000000100, P = 10;
typedef long long int LL;
int t, p;
LL V[1 << P], T[1 << P][P + 1];
void zloz(LL T[], LL A[], LL B[], LL c)
{
	for(int i = 0; i < P; ++i)
		T[i] = min(A[i + 1] + B[i + 1], A[i] + B[i] + c);
	T[P] = A[P] + B[P] + c;
	for(int i = P - 1; i >= 0; --i)
		T[i] = min(T[i], T[i + 1]);
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase)
	{
		for(int i = 0; i < (1 << P); ++i)
			for(int j = 0; j <= P; ++j)
				T[i][j] = INF;
		cin >> p;
		for(int i = 0; i < (1 << p); ++i)
			cin >> V[i];
		for(int i = 0; i < (1 << p); ++i)
			for(int j = 0; j <= V[i]; ++j)
				T[i][j] = 0;
		for(int i = p - 1; i >= 0; --i)
		{
			for(int j = 0; j < (1 << i); ++j)
				cin >> V[j];
			for(int j = 0; j < (1 << i); ++j)
				zloz(T[j], T[2 * j], T[2 * j + 1], V[j]);
		}
		cout << "Case #" << testCase << ": " << T[0][0] << endl;
	}
}

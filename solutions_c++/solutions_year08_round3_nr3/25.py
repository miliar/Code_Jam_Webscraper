#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <vector>
#include <string>
#pragma comment (linker, "/STACK:16000000")
using namespace std;
#define inf 2123456789
#define INPUT "in.txt"
#define OUTPUT "out.txt"

long long a[500011];

inline int Prev(int x)
{
	return x & (x-1);
}
inline int Next(int x)
{
	return (x << 1) - Prev(x);
}

long long A[500011] = {0}; // Summator
inline long long FindSum(int e)
{
	long long res=0;
	while (e > 0) {
		res += A[e];
		e = Prev(e);
	}
	return res;
}

inline void Modify(int pos, long long val)
{
	while (pos <= 500005) {
		A[pos] += val;
		A[pos] %= 1000000007;
		pos = Next(pos);
	}
}

int s[500011];
int pos [500011], tmp;
void Quicks(int b, int e)
{
	int i = b, j = e;
	long long X = s[(e+b)/2];
	while (i<=j) {
		while (s[i] < X) i++;
		while (s[j] > X) j--;

		if (i<=j) {
			tmp = s[j];
			s[j] = s[i];
			s[i] = tmp;
			
			tmp = pos[j];
			pos[j] = pos[i];
			pos[i] = tmp;

			i++;
			j--;
		}
	}
	if (i<e) Quicks(i,e);
	if (b<j) Quicks(b,j);
}

void Quickpos(int b, int e)
{
	int i = b, j = e;
	long long X = pos[(e+b)/2];
	while (i<=j) {
		while (pos[i] < X) i++;
		while (pos[j] > X) j--;

		if (i<=j) {
			tmp = s[j];
			s[j] = s[i];
			s[i] = tmp;
			
			tmp = pos[j];
			pos[j] = pos[i];
			pos[i] = tmp;

			i++;
			j--;
		}
	}
	if (i<e) Quickpos(i,e);
	if (b<j) Quickpos(b,j);
}

int main()
{
	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);
	int t; cin >> t;
	for (int i=0; i<t; i++) {
		int n,m;
		long long X,Y,Z;
		cin >> n >> m >> X >> Y >> Z;
		for (int u=0; u<m; u++) cin >> a[u];

		memset(A, 0, sizeof A);
		for (int u=0; u<n; u++) {
			s[u] = a[u % m] + 1;
			pos[u] = u;
	//		cout << s[u] << ' ';
			a[u % m] = (X * a[u % m] + Y * (u + 1)) % Z;
		}

		Quicks(0, n-1);
		int cur = s[0];
		s[0] = 1;
		for (int u=1; u<n; u++) {
			if (s[u] != cur) {
				cur = s[u];
				s[u] = s[u-1]+1;
			}
			else
				s[u] = s[u-1];
		}
		Quickpos(0, n-1);
		for (int u=0; u<n; u++)
			Modify(s[u], FindSum(s[u]-1) + 1);
		cout << "Case #" << i+1 << ": " << (FindSum(500002)%1000000007) << endl;
	}
	return 0;
}
/**					Be name Khoda					**/
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <algorithm>
#include <bitset>
#include <limits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <memory.h>
#include <ctime>
#include <cassert>
using namespace std;

#define ll long long
#define un unsigned
#define IT iterator
#define VAL(x) #x << " = " << x << "   "
#define SQR(a) ((a) * (a))
#define SZ(x) ((int) x.size())
#define ALL(x) x.begin(), x.end()
#define CLR(x, a) memset(x, a, sizeof x)
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define SAL cout << "Salam!\n"
#define MAXN 1000
#define cout fout
#define cin fin

pair<int, int> getMax(int n)
{
	if (n == 0)
		return mp(0, 0);
	int q = n / 3, r = n % 3;
	if (r == 0)
		return mp(q, q + 1);
	if (r == 1)
		return mp(q + 1, q + 1);
	if (r == 2)
		return mp(q + 1, q + 2);
}

int main ()
{
	ifstream fin("B-large.in");
	ofstream fout("B.out");
	int tc, k = 0;
	cin >> tc;
	while (tc --)
	{
		k ++;
		int n, s, p, a[MAXN], ans = 0;
		cin >> n >> s >> p;
		for (int i = 0; i < n; i ++)
			cin >> a[i];
		for (int i = 0; i < n; i ++)
		{
			pair<int, int> now = getMax(a[i]);
			//cout << VAL(now.X) << VAL(now.Y) << endl;
			if (now.X >= p)
				ans ++;
			else
			if (now.Y >= p && s > 0)
			{
				s --;
				ans ++;
			}
		}
		cout << "Case #" << k << ": " <<  ans << endl;
	}
	return 0;
}



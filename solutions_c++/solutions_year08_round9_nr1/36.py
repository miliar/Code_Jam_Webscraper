#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
//#include <utility>
//#include <set>
//#include <map>
//#include <queue>
#include <iomanip>
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

vector<int> a[5000];
int t;
int x[5000];
int y[5000];

int m;
int v[5010];

void up(int x)
{
	int bak = v[x];
	while (x > 1)
	{
		int y = x/2;
		if (v[y] > bak) break;
		v[x] = v[y];
		x = y;
	}
	v[x] = bak;
}

void down(int x)
{
	int bak = v[x];
	int y = x*2;
	while (y <= m)
	{
		if (y < m && v[y+1]>v[y]) y++;
		if (v[y] <= bak) break;
		v[x] = v[y];
		x = y;
		y = x*2;
	}
	v[x] = bak;
}


int calc(int va)
{
	int best = 0;
	m = 0;
	FI(i,0,t)
	{
		v[++m] = y[i];
		up(m);
		int limit = 10000-va-x[i];

		while (m > 0 && v[1] > limit)
		{
			v[1] = v[m];
			m--;
			down(1);
		}
		if (m >= best) best = m;
	}
	return best;
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		int n;
		fin >> n;
		FI(i,0,n)
		{
			a[i].clear();
			FI(j,0,3)
			{
				int k;
				fin >> k;
				a[i].push_back(k);
			}
		}
		FI(i,0,n) FI(j,i+1,n) if (a[i] > a[j]) swap(a[i], a[j]);

		t = 0;
		int ans = 0;
		FI(i,0,n)
		{
			int x1 = a[i][1], y1 = a[i][2];
			int j = 0;
			while (j < t && x[j] <= x1) j++;
			for (int k = t-1; k >= j; k--)
			{
				x[k+1] = x[k];
				y[k+1] = y[k];
			}
			t++;
			x[j] = x1; y[j] = y1;
			if (i < n-1 && a[i][0] == a[i+1][0]) continue;
			int va = a[i][0];
			int ret = calc(va);
			if (ret > ans) ans = ret;
		}

		fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}

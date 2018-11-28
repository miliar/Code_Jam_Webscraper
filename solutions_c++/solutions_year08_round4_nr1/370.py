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
using namespace std;

#define mset(A,B) memset(A,B,sizeof(A));
#define mcpy(A,B) memcpy(A,B,sizeof(B));
typedef long long ll;
typedef long double ld;
typedef vector<int> vint;
//typedef vector<string> vstr;
#define FI(I,L,U) for (int I=L;I<U;I++)
#define sqr(x) ((x)*(x))

int a[11000][2];
int g[11000];
int c[11000];

inline void upd(int& x, int c1, int c2, int q)
{
	if (c1 >= 0 && c2 >= 0)
	{
		q += c1+c2;
		if (x < 0 || q < x) x = q;
	}
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		//istringstream strin();
		int m,v;
		fin >> m >> v;
		mset(a, 255);
		FI(i,1,(m-1)/2+1)
			fin >> g[i] >> c[i];
		int j = (m-1)/2+1;
		int k;
		FI(i,0,(m+1)/2)
		{
			fin >> k;
			a[i+j][k] = 0;
		}
		for (int i = (m-1)/2; i >= 1; i--)
		{
			if (g[i] == 1 || c[i] == 1)
			{	// and
				int q = 0;
				if (g[i] != 1) q = 1;
				upd(a[i][0], a[i*2][0], a[i*2+1][0], q);
				upd(a[i][0], a[i*2][0], a[i*2+1][1], q);
				upd(a[i][0], a[i*2][1], a[i*2+1][0], q);
				upd(a[i][1], a[i*2][1], a[i*2+1][1], q);
			}
			if (g[i] == 0 || c[i] == 1)
			{	// or
				int q = 0;
				if (g[i] != 0) q = 1;
				upd(a[i][0], a[i*2][0], a[i*2+1][0], q);
				upd(a[i][1], a[i*2][0], a[i*2+1][1], q);
				upd(a[i][1], a[i*2][1], a[i*2+1][0], q);
				upd(a[i][1], a[i*2][1], a[i*2+1][1], q);
			}
		}

		int ans = a[1][v];
		if (ans < 0)
			fout << "Case #" << tind << ": " << "IMPOSSIBLE" << endl;
		else
			fout << "Case #" << tind << ": " << ans << endl;
	}
	return 0;
}

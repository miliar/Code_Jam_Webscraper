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
#include <queue>
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

bool m[55][55];
int dis[51][51][51];// row start end
bool ex[51][51][51];

int getDrop(int x, int y) {
	int ret = 0;
	while (m[x+1][y]) {
		++x; ++ret;
	}
	return ret;
}

int rr, cc;
void test(int x, int y, int y2, int newdis, queue<int>& q) {
	if (dis[x][y][y2] < 0 || dis[x][y][y2] > newdis) {
		dis[x][y][y2] = newdis;
		q.push((x*cc+y)*cc+y2);
		//cout << x << ' ' << y << '-' << y2 << ' ' << newdis << endl;
	}
}

int x, yl, y2;
bool emp(int r1, int c1)
{
	return m[r1][c1] || (r1 == x && (c1-yl)*(c1-y2)<=0);
}

int main()
{
	int tcase = 0;
	ifstream fin("z.in");
	ofstream fout("z.out");
	fin >> tcase;
	for (int tind = 1; tind <= tcase; tind++)
	{
		int r,c,f;
		string s;
		fin >> r >> c >> f;
		cc = c; rr = r;
		mset(m, 0);
		FI(i,0,r) {
			fin >> s;
			FI(j,0,c) if (s[j] == '.') m[i][j] = true;
		}

		mset(dis, 255);
		mset(ex, 0);
		dis[0][0][0] = 0;
		queue<int> q[51*51];
		q[0].push(0);
		int ans = -1;
		int i = 0;
		while (1) {
			while (i <= r*c && q[i].empty()) ++i;
			if (i > r*c) break;
			int z = q[i].front();
			q[i].pop();
			x = z/c/c;
			yl = z/c%c;
			y2 = z%c;
			if (ex[x][yl][y2]) continue;
			ex[x][yl][y2] = true;
			if (x == r-1) {
				ans = i;
				break;
			}
			int c1 = yl;
			while (c1 > 0 && emp(x, c1-1) && !m[x+1][c1-1]) c1--;
			int c2 = yl;
			while (c2 < c-1 && emp(x, c2+1) && !m[x+1][c2+1]) c2++;
			
			if (c1 > 0 && emp(x,c1-1)) {
				int k = getDrop(x, c1-1);
				if (k > 0 && k <= f)
					test(x+k, c1-1, c1-1, i, q[i]);
			}
			if (c2 < c-1 && emp(x,c2+1)) {
				int k = getDrop(x, c2+1);
				if (k > 0 && k <= f)
					test(x+k, c2+1, c2+1, i, q[i]);
			}
			if (c1 < c2) {
				for (int c3 = c1; c3 <= c2; ++c3) {
					int k = getDrop(x+1, c3);
					if (1+k <= f)
						test(x+1+k, c3, c3, i+1, q[i+1]);
				}
				for (int c3 = c1; c3 <= c2; ++c3) if (!m[x+2][c3]) 
					for (int c4 = c1; c4 <= c2; ++c4)
				{
					if (c3 == c4) continue;
					if (c3 == c1) continue;
					if (c3 == c2) continue;
					test(x+1, c3, c4, i+abs(c3-c4)+1, q[i+abs(c3-c4)+1]);
				}

			}
		}

		if (ans < 0)
			fout << "Case #" << tind << ": No" << endl;
		else
			fout << "Case #" << tind << ": Yes " << ans << endl;
	}
	return 0;
}

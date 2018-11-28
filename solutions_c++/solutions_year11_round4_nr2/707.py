#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <ctime>

using namespace std;

typedef long long lint;

int w[500][500];

bool checkCorner(int i, int j, int s) {
	if (i==0 && (j==0 || j==s-1)) return true;
	if (i==s-1 && (j==0 || j==s-1)) return true;
	return false;
}

bool calCen(int x, int y, int s) {
	long double cx, cy, wx=0, wy=0, mx, my;
	int wgt=0;
	mx = x + 1.0*s/2;
	my = y + 1.0*s/2;
	for (int i=0; i<s; i++)
		for (int j=0; j<s; j++) {
			if (!checkCorner(i,j,s)) {
				wx += w[i+x][j+y] * (i+x+0.5);
				wy += w[i+x][j+y] * (j+y+0.5);
				wgt += w[i+x][j+y];
			}
		}
	if (wx/wgt == mx && wy/wgt == my) return true;
	else return false;
}

int main() {
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("Bs.out", "w", stdout);

	int T; cin>>T;
	int r, c, d, s;
	char ch;
	bool solved;
	for (int K=1; K<=T; K++) {
		cin>>r>>c>>d;
		s = min(r,c);
		solved = false;

		for (int i=0; i<r; i++) {
			for (int j=0; j<c; j++) {
				cin>>ch;
				w[i][j] = (ch-'0')+d;
			}
		}
		
		cout<<"Case #"<<K<<": ";

		while (!solved && s>=3) {
			for (int i=0; !solved && i+s<=r; i++)
				for (int j=0; !solved && j+s<=c; j++) {
					if (calCen(i,j,s)) {
						solved = true;
						cout<<s<<endl;
					}
				}
			--s;
		}
		if (!solved) cout<<"IMPOSSIBLE\n";
	}
}

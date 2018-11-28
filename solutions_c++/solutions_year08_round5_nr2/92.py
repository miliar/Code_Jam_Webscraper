#include <iostream>
#include <list>
#include <algorithm>
using namespace std;

bool vv[15][15][15][15];
int p[15][15][4][2];
bool w[15][15];

int main()
{
    int N; cin >> N;
    for (int X = 1; X <= N; ++X) {
	int r, c; cin >> r >> c;
	int is, js, it, jt;
	list<pair<pair<int, int>, pair<int, int> > > q;
	for (int i = 0; i < r; ++i) {
	    for (int j = 0; j < c; ++j) {
		char k; cin >> k;
		w[i][j] = false;
		switch (k) {
		case '#': w[i][j] = true; break;
		case 'O': is = i; js = j; break;
		case 'X': it = i; jt = j; break;
		}
	    }
	}
	for (int i = 0; i < r; ++i)
	    for (int j = 0; j < c; ++j)
		for (int d = 0; d < 4; ++d) {
		    int u, v, u1 = i, v1 = j;
		    do {
			u = u1; v = v1;
			switch (d) {
			case 0: u1++; break;
			case 1: v1++; break;
			case 2: u1--; break;
			case 3: v1--; break;
			}
		    } while (u1 >= 0 && u1 < r && v1 >= 0 && v1 < c &&
			     !w[u1][v1]);
		    p[i][j][d][0] = u; p[i][j][d][1] = v;
		    //cout << "p " << i << ' ' << j << ' ' << d << ' ' << u << ' ' << v << endl;
		}
	for (int i = 0; i < r; ++i)
	    for (int j = 0; j < c; ++j)
		for (int u = 0; u < r; ++u)
		    for (int v = 0; v < c; ++v)
			vv[i][j][u][v] = false;
	vv[is][js][is][js] = true;
	q.push_back(make_pair(make_pair(is, js), make_pair(is, js)));
	int t;
	for (t = 1; !q.empty(); ++t) {
	    list<pair<pair<int, int>, pair<int, int> > > qq;
	    qq.swap(q);
	    while (!qq.empty()) {
		int i = qq.front().first.first, j = qq.front().first.second,
		    u = qq.front().second.first, v = qq.front().second.second;
		if (i < 0 || i >= r || j < 0 || j >= c || w[i][j]) {
			cerr << "WRONG" << ' ' << X << ' ' << t << ' ' << i << ' ' << j << ' ' << u << ' ' << v << endl;
		    return 1;
		    }
		qq.pop_front();
		for (int d = 0; d < 5; ++d) {
		    int u1 = u, v1 = v;
		    if (d < 4)
			u1 = p[i][j][d][0], v1 = p[i][j][d][1];
		    for (int e = 0; e < 4; ++e) {
			int i1 = i, j1 = j;
			switch (e) {
			case 0: i1++; break;
			case 1: j1++; break;
			case 2: i1--; break;
			case 3: j1--; break;
			}
			if (i1 >= 0 && i1 < r && j1 >= 0 && j1 < c &&
			    !w[i1][j1]) {
			    if (!vv[i1][j1][u1][v1]) {
				if (i1 == it && j1 == jt)
				    goto done;
				vv[i1][j1][u1][v1] = true;
				q.push_back(make_pair(make_pair(i1, j1),
						      make_pair(u1, v1)));
			    }
			} else {
			    if (!vv[u1][v1][i][j]) {
				if (u1 == it && v1 == jt)
				    goto done;
				vv[u1][v1][i][j] = true;
				q.push_back(make_pair(make_pair(u1, v1),
						      make_pair(i, j)));
			    }
			}
		    }
		}
	    }
	}
	cout << "Case #" << X << ": THE CAKE IS A LIE" << endl;
	continue;
    done:
	cout << "Case #" << X << ": " << t << endl;
    }
}

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <ctime>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>

using namespace std;

const long long INF = 10000000000000000ll;

inline long long prev(long long x) {
	return (x & (x-1));
}

inline long long next (long long x) {
	return (x << 1) - (x & (x-1));
}

struct ddd {
	long long x;
	long long y;

	bool operator < (const ddd &ot) const {
		return x < ot.x || (x == ot.x && y < ot.y);
	}
};

long long dx[] = {-1, 1, 0, 0};
long long dy[] = {0, 0, -1, 1};

long long size;
long long s[1111][1111];
long long p = 0;
long long M[5555];

long long res[1111][1111][11];
long long cost[1111][1111];

long long mmin(long long a, long long b) {
	return (a < b) ? a : b;
}

long long findRes(long long b, long long e, long long up = 0) {
	if (res[b][e][up] != -1) return res[b][e][up];

	bool has = false;
	bool more = false;
	for (long long i=b; i<e; i++) {
		if (M[i] -up > 0) {
			has = true;
		}
		if (M[i] - up > 1) 
			more = true;
	}
	if (!has) {
		res[b][e][up] = 0;
		return 0;
	}

	if (b == e-2) {
		if (more) return INF;
		return cost[b][e];
	}

	long long len = (e - b) >> 1;
	long long cur = mmin(findRes(b, b+len, up + 1) + findRes(b+len, e, up + 1) + cost[b][e], findRes(b, b+len, up) + findRes(b+len, e, up));
	if (cur > INF) cur = INF;
	res[b][e][up] = cur;

	return cur;

}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	//int t; cin >> t;

	//for (int e=1; e<=t; e++) {
	//	int ans = 0;
	//	set<ddd> l;
	//	int r; cin >> r;
	//	for (int i=0; i<r; i++) {
	//		int x1, y1, x2, y2;
	//		cin >> x1 >> y1 >> x2 >> y2;
	//		for (int x=x1; x<=x2; ++x) {
	//			for (int y=y1; y<=y2; ++y) {
	//				ddd tmp = {x,y};
	//				l.insert(tmp);
	//			}
	//		}
	//	}

	//	set <ddd> l2;
	//	for (; ; ans++) {
	//	//	map<ddd, bool> m;

	//		l2.clear();
	//		for (set<ddd>::iterator it = l.begin(); it != l.end(); ++it) {

	//			ddd up = {it->x-1, it->y};
	//			ddd left = {it->x, it->y-1};
	//			if (l.find(up) != l.end() || l.find(left) != l.end() ) {
	//				l2.insert(*it);
	//			}

	//			for (int i=0; i<4; i++) {
	//				int x = it->x + dx[i];
	//				int y = it->y + dy[i];

	//				ddd up = {x, y-1};
	//				ddd left = {x-1, y};

	//				if (l.find(up) != l.end() && l.find(left) != l.end() ) {
	//					ddd ins = {x, y};
	//					l2.insert(ins);
	//				}
	//			}
	//		}

	//		if (l2.size() == 0) break;
	//		l = l2;
	//	}



	//	cout << "Case #" << e << ": " << ans+1 << endl;
	//}

//	int t; cin >> t;
//
//	for (int e=1; e<=t; e++) {
//		cin >> size;
//		memset(s, -1, sizeof s);
//
//		int x = 500;
//		int y = 500;
//
//		int lim = 1;
//		int dir = 1;
//
//		set <ddd> used;
//		for (int i=0; i<size * 2 - 1; i++) {
//			x = 500 + (abs(size - i - 1));
//			for (int u=0; u<lim; u++, x+=2) {
//				cin >> s[x][y];
//				ddd tmp = {x,y};
//				used.insert(tmp);
//			}
//
//			lim += dir;
//			if (lim > size) {
//				lim -= 2;
//				dir = -dir;
//			}
//
//			++y;
//		}
//		
//		int best = INF;
//
//		for (int sz = size; sz <= size * 2; sz++) {
//			set<ddd> now;
//			for (int cy = 500 - size * 2; cy < 500 + (size*3); cy++) {
//				for (int cx = 500 - size * 2; cx < 500 + (size*3); cx++) {
//					if ( (cx + cy) % 2 == (size+1) % 2) {
//						now = used;
//						bool can = true;
//						int add = 0;
//
//
//						int lim1 = cx;
//						dir = 1;
//						for (int yy = cy - sz + 1; yy<= cy; yy++) {
//							for (int xx = cx - abs(cx - lim1); xx<=lim1; xx+=2) {
//								if (yy == cy && xx >= cx) {
//									if (s[xx][yy] == -1)
//										add++;
//									else {
//										ddd tmp = {xx, yy};
//										now.erase(tmp);
//									}
//									break;
//								}
//								if (s[xx][yy] != -1) {
//									ddd tmp = {xx, yy};
//									now.erase(tmp);
//									if (s[ cx * 2 - xx ][ yy] != -1 && s[ cx * 2 - xx ][ yy] != s[xx][yy]) {
//										can = false;
//										goto end;
//									}
//									if (s[ cx * 2 - xx ][ yy] == -1) {
//										++add;
//									} else {
//										ddd tmp = {cx * 2 - xx , yy};
//										now.erase(tmp);
//									}
//
//
//									if (s[ xx ][ cy * 2 - yy] != -1 && s[ xx ][ cy * 2 - yy] != s[xx][yy]) {
//										can = false;
//										goto end;
//									}
//									if (s[ xx ][ cy * 2 - yy] == -1) {
//										++add;
//									} else {
//										ddd tmp = {xx , cy * 2 - yy};
//										now.erase(tmp);
//									}
//
//								} else {
//									++add;
//									if (cy * 2 - yy != yy && s[  xx ][ cy * 2 - yy] == -1) {
//										++add;
//									}
//									if (cx*2 - xx != xx && s[ cx*2 - xx ][ yy] == -1) {
//										++add;
//									}
//
//									if (s[ cx*2 - xx ][ yy] != -1 && s[  xx ][ cy * 2 - yy] != -1 && 
//										s[ cx*2 - xx ][ yy] != s[  xx ][ cy * 2 - yy]) {
//											can = false;
//											goto end;
//									}
//								}
//							}
//
//							lim1 += dir;
//							if (yy == cy + 1) {
//								lim1 -= 2;
//								dir = -dir;
//							}
//						}
//
//end:;
//
//						if (can && add < best && now.size() == 0) {
//							best = add;
//							goto nxt;
//						}
//
//					}
//				}
//			}
//
//		}
//
//nxt:;
//
//
//		cout << "Case #" << e << ": " << best << endl;
//
//
//	}

	long long t; cin >> t;
	for (long long e=1; e<=t; e++) {
		cin >> p;

		for (long long i=0; i< (1<<p); i++) {
			cin >> M[i];
			M[i] = p-M[i];
		}

		long long curlen = 2;
		for (long long i=p-1; i>=0; i--) {
			long long ttt = 0;
			for (long long u=0; u< (1 << i); u++) {
				cin >> s[i][u];
				cost[ttt][ttt+curlen] = s[i][u];
				ttt += curlen;
			}
			curlen <<= 1;
		}

		memset(res, -1, sizeof res);

		cout << "Case #" << e << ": " << findRes(0, (1<<p)) << endl;
	}


	return 0;
}


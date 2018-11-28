#include <vector>
#include <deque>
#include <iostream>
#include <string>
using namespace std;
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <set>

//By chyx111
#define DBG(a) do{cerr << #a << ": " << (a) << endl;}while(0)
#define FORE(elem,v)\
	for(__typeof__(v.begin()) _it = v.begin(); _it != v.end(); ++_it)\
for(int _once=1, _done=0; _once; (!_done) ? (_it=v.end(), --_it) : _it )\
for(__typeof__(*_it) & elem = * _it; _once && !(_once=0); _done=1)
template<class T> void inline checkMax(T& a, T b)
{
	if(a < b){
		a = b;
	}
};
template<class T> void inline checkMin(T& a, T b)
{
	if(b < a){
		a = b;
	}
};
#define DBG_(a) do{cerr << #a << ": " << (a) << ' ';}while(0)
#define REP(i,n) for(int n_##__LINE__ = (n), i = 0; i < n_##__LINE__; ++i)

int const N = 1010;

struct Point{
	int x, y;
	int r;
	int id;
	bool operator<(Point const& other)const{
		return r < other.r;
	}
	bool intersect(Point const& other)const{
		return x - (r + other.r) <= other.x && other.x <= x + (r + other.r);
	}
};
Point point[N];
bool cmp(Point const& a, Point const& b){
	return a.id < b.id;
}

int main() {
	int ca;
	scanf("%d", &ca);
	REP (ica, ca){
		int n, W, L;
		scanf("%d%d%d", &n, &W, &L);
		REP (i, n){
			scanf("%d", &point[i].r);
			point[i].id = i;
		}
		sort(point, point + n);
		reverse(point, point + n);

		point[0].x = point[0].y = 0;
		int st = 1;
		int wid = point[0].r;
		for(int i = 1; i < n; ++i){
			if(point[i].r + wid > W){
				break;
			}
			st = i + 1;
			point[i].x = wid + point[i].r;
			wid += point[i].r * 2;
			point[i].y = 0;
		}
		DBG(st);
		for(int i = st; i < n; ++i){
			vector<int> difs;
			for(int ref = 0; ref < i; ++ref){
				difs.clear();
				difs.push_back(point[ref].r + point[i].r);
				difs.push_back(-(point[ref].r + point[i].r));

				bool found = false;
				FORE (dif, difs){
					point[i].x = point[ref].x + dif; checkMax(point[i].x, 0); checkMin(point[i].x, W);
					point[i].y = 0;
					REP (j, i){
						if(point[j].intersect(point[i])){
							checkMax(point[i].y, point[j].y + point[j].r + point[i].r);
						}
					}
					if(point[i].y <= L){
						found = true;
						break;
					}
				}
				if(found)break;
			}
		}
		sort(point, point + n, cmp);
		printf("Case #%d:", ica + 1);
		REP (i, n){
			printf(" %d %d", point[i].x, point[i].y);
		}
		puts("");
	}
}

#include <algorithm> 
#include <bitset> 
#include <cassert>
#include <cmath> 
#include <complex>
#include <cstdio> 
#include <cstdlib> 
#include <cstring>
#include <ctime> 
#include <deque> 
#include <functional> 
#include <iomanip> 
#include <iostream> 
#include <list> 
#include <map> 
#include <numeric> 
#include <queue> 
#include <set> 
#include <sstream> 
#include <stack> 
#include <utility> 
#include <vector> 
using namespace std; 

#define ALL(x) (x).begin(), (x).end()
#define MP make_pair
#define SZ(x) ((int) (x).size())
#define max2(x,y) ((x) = max((x),(y)))
#define min2(x,y) ((x) = min((x),(y)))
typedef long long LL;

int N;
typedef pair<set<int>,int> P;
#define x first
#define y second

map<P,int> cache;

map<string,int> colormap;
int getcolor(const string &s)
{
	map<string,int>::iterator it = colormap.find(s);
	if (it == colormap.end()) {
		int sz = SZ(colormap);
		colormap[s] = sz;
		return sz;
	}
	return it->second;
}

int A[16], B[16], C[16];

int getmin(const P &p)
{
	if (SZ(p.x) > 3)
		return 423;
	if (p.y >= 10001)
		return 0;

	map<P,int>::iterator it = cache.find(p);
	if (it != cache.end())
		return it->second;

	int r = 1234;
	for (int i = 0; i < N; ++i) {
		if (A[i] <= p.y && B[i] >= p.y) {
			set<int> s = p.x;
			s.insert(C[i]);
			min2(r, getmin(MP(s,B[i]+1))+1);
		}
	}

	cache[p] = r;
	return r;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TT = 1; TT <= T; ++TT) {
		cache.clear();
		colormap.clear();
		scanf("%d", &N);
		for (int i = 0; i < N; ++i) {
			char tmp[16];
			scanf("%s %d %d", tmp, &A[i], &B[i]);
			C[i] = getcolor(tmp);
		}
		set<int> s;
		int r = getmin(MP(s,1));
		printf("Case #%d: ", TT);
		if (r <= 300)
			printf("%d\n", r);
		else
			puts("IMPOSSIBLE");
	}
	return 0;
}

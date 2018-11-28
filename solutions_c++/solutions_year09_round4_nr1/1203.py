#include <cstdio>
#include <functional>
#include <cstdlib>
#include <vector>
#include <string.h>
#include <string>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#define feq(x,y) (fabs((x)-(y))<eps)
#define flt(x,y) ((x)<(y)-eps)
#define fgt(x,y) ((x)>(y)+eps)
#define fle(x,y) ((x)<(y)+eps)
#define fge(x,y) ((x)>(y)-eps)
using namespace std;
const double inf = 1e40, eps = 1e-9;

int n, a[50], ans;
struct r{
	int a[50], c;
	r(){}

	void aswap(int x, int y){
		int t = a[x];
		a[x] = a[y];
		a[y] = t;
	}	

	long long cal(){
		long long r = 0;
		for (int i=0;i<n; i++)
			r = r*10 + a[i];
		return r;
	}

	bool check(){
		for (int i=0; i<n; i++)
			if (a[i] > i)
				return false;
		return true;
	}

	bool operator<(const r &p)const{ return c < p.c; }
	bool operator>(const r &p)const{ return c > p.c; }

};


map< int, int> ma;
priority_queue< r, vector<r>, greater<r> > q;
void dfs(){
	while (!q.empty()) q.pop();

	r p; for (int i=0; i<n; i++) p.a[i] = a[i]; p.c = 0;
	q.push(p);
	while (!q.empty()){
		r p = q.top(); q.pop();
		long long d = p.cal();
		if (ma.find(d) != ma.end()) 
			continue;
		ma.insert(make_pair(d,p.c));
		//for (int i=0; i<n; i++) printf("%d ", p.a[i]); printf(": %d\n", p.c);
		//	if (c > n*n) return;
		if (p.check()){
			ans = p.c;
			return;
		}
		for (int i=0; i<n; i++){
			if (i!=0 && p.a[i] < i){
				r np; for (int j=0; j<n; j++) np.a[j] = p.a[j]; np.c = p.c+1;
				np.aswap(i, i-1);
				q.push(np);
			}
			if (i!=n-1 && p.a[i] > i){
				r np; for (int j=0; j<n; j++) np.a[j] = p.a[j]; np.c = p.c+1;
				np.aswap(i, i+1);
				q.push(np);
			}
		}
	}
}

int main(){
	int T, ca = 0;
	char s[50];
	scanf("%d", &T); gets(s);
	while (T--){
		memset(a, 0, sizeof(a));
		scanf("%d", &n); gets(s);
		for (int i=0; i<n; i++){
			int last = -1;
			gets(s);
			for (int j=0; j<n; j++){
				if (s[j]=='1') last = j;
			}
			a[i] = last;
		}


		ma.clear();
		ans = 2147483647;
		dfs();

		printf("Case #%d: %d\n", ++ca, ans);
	}
}

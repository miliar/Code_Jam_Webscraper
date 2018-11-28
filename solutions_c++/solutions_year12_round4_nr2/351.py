#include<cstdio>
#include<algorithm>
#include<functional>

#define ST first
#define ND second

using namespace std;


const int maxn = 1e3+7;

int n, w, l, i, a, b;
pair<int, int> r[maxn];
int x[maxn], y[maxn];
int aktx, akty, dy;

void testcase(){
	scanf("%d %d %d", &n, &w, &l);
	for(i=0;i<n;++i){
		scanf("%d", &a);
		r[i].ST = a;
		r[i].ND = i;
	}
	sort(r, r+n, greater<pair<int, int> >());
	
	aktx = -r[0].ST;
	akty = 0;
	dy = r[0].ST;

	for(i=0;i<n;++i){
		if(aktx + r[i].ST > w){
			aktx = -r[i].ST;
			akty = dy + r[i].ST;
			dy += 2*r[i].ST;
		}
		x[r[i].ND] = aktx + r[i].ST;
		y[r[i].ND] = akty;
		aktx += 2*r[i].ST;
	}

	for(i=0;i<n;++i)
		printf("%d %d ", x[i], y[i]);
	printf("\n");

	return;
}

int t, ti;

int main(){
	scanf("%d", &t);
	for(ti=1;ti<=t;++ti){
		printf("Case #%d: ", ti);
		testcase();
	}

	return 0;
}

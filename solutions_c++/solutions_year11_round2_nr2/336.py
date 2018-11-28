#include<cstdio>
#include<cstring>
#include<cmath>
#include<map>
#include<algorithm>
#define EPS (1e-8)
#define MAX_C 210
#define MVC 1000010
using namespace std;
int D, C;
int V[MAX_C], P[MAX_C];
pair<int, int> p[MAX_C];
bool check(double t){
	double d = p[0].first - t;
	for(int i=0;i<C;++i){
		int n = p[i].second;
		for(int j=0;j<n;++j){
			d = max(d + D, p[i].first - t);
			if(d - p[i].first - EPS > t){
				return false;
			}
		}
	}
	return true;
}
double solve(){
	double res;
	double l, u, c;
	for(int i=0;i<C;++i){
		p[i].first = P[i];
		p[i].second = V[i];
	}
	sort(p, p+C);
	p[0].second--;

	l = 0.0;
	u = (double)D * (double)MVC;
	res = u;
	for(int k=0;k<50;++k){
		c = (l + u) / 2.0;
		if(check(c)){
			res = c;
			u = c;
		}
		else{
			l = c;
		}
	}
	return res;
}
int main(){
	int T;
	scanf("%d", &T);
	for(int k=0;k<T;++k){
		scanf("%d%d", &C, &D);
		for(int i=0;i<C;++i){
			scanf("%d%d", &P[i], &V[i]);
		}
		printf("Case #%d: %.8lf\n", k+1, solve());
	}
}

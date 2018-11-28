#include<cstdio>
#include<algorithm>
inline double abs(double A){return A > 0.0 ? A: -A;}
inline double max(double A, double B){return A > B? A: B;}
inline double min(double A, double B){return A < B? A: B;}
int T, C, V;
double D, now;
double pos[1000001];
bool chk(double K){
	for(int i = V - 1; i >= 0; i--){
		double now = min(now - D, pos[i] + K);
		if(abs(now - pos[i]) > K + 1e-8)return false;
	}
	return true;
}
int main(){
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		now = 1e300;
		V = 0;
		scanf("%d%lf", &C, &D);
		for(int i = 0; i < C; i++){
			int v;
			double P;
			scanf("%lf%d", &P, &v);
			for(int j = 0; j < v; j++)
				pos[V++] = P;
		}
		std::sort(pos, pos + V);
		double bg = 0.0, ed = 1e13, mid;
		while(ed - bg > 1e-7){
			mid = (bg + ed) / 2.0;
			if(chk(mid))ed = mid;
			else bg = mid;
		}
		printf("Case #%d: %lf\n", t, mid);
	}
}

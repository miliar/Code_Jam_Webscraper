#include<cstdio>
#include<algorithm>
struct wlk{
	int B, E;
	double spd, len;
	bool operator<(const wlk &cmp)const{
		return spd < cmp.spd;
	}
}W[1001];
int T, N;
double S, R, X, tm, ans;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		ans = 0.0;
		scanf("%lf%lf%lf%lf%d", &X, &S, &R, &tm, &N);
		for(int i = 0; i < N; i++){
		    scanf("%d%d%lf", &W[i].B, &W[i].E, &W[i].spd);
			W[i].len = W[i].E - W[i].B;
			X -= (W[i].E - W[i].B);
		}
		std::sort(W, W + N);
		if(R * tm > X){
			ans = X / R;
			tm -= ans;
		}else{
			ans = (X - R * tm) / S + tm;
			tm = 0.0;
		}
		for(int i = 0; i < N; i++){
			double tR = R + W[i].spd, tS = S + W[i].spd;
			if(tR * tm > W[i].len){
				ans += W[i].len / tR;
				tm -= W[i].len / tR;
			}else{
				ans += (W[i].len - tR * tm) / tS + tm;
				tm = 0.0;
			}
		}
		printf("Case #%d: %lf\n", t, ans);
	}
}

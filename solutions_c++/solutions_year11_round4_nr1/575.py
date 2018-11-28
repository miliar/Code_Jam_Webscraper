#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<vector>

using namespace std;

struct walk {
	int B, E, w;
	
	bool operator<(const walk &o) const {
		return B < o.B;
	}
};

walk corr[10000];
pair<int,int> data[10000];

int main() {
	int T;
	int X, S, R, t, N;
	
	scanf("%d\n", &T);
	
	for(int nCase = 1; nCase <= T; nCase++) {
		scanf("%d %d %d %d %d\n", &X, &S, &R, &t, &N);
		
		for(int i = 0; i < N; i++) {
			scanf("%d %d %d\n", &corr[i].B, &corr[i].E, &corr[i].w);
		}
		
		sort(corr, corr + N);
		
		int di = 0;
		int si = 0;
		
		for(int i = 0; i < N; i++) {
			if(di < corr[i].B) {
				data[si].first = 0;
				data[si].second = corr[i].B - di;
				si++;
			}
			data[si].first = corr[i].w;
			data[si].second = corr[i].E - corr[i].B;
			si++;
			di = corr[i].E;
		}
		
		if(di < X) {
			data[si].first = 0;
			data[si].second = X - di;
			si++;
		}
		
		sort(data, data + si);
		
		double ans = 0;
		double rt = t;
		double tim;
		
		for(int i = 0; i < si; i++) {
			if(rt > 0) {
				tim = data[i].second / (double)(data[i].first + R);
				
				if(tim >= rt) {
					double dist = rt * (data[i].first + R);
					ans += rt + (data[i].second - dist) / (double)(data[i].first + S);
					rt = 0;
				} else {
					ans += tim;
					rt  -= tim;
				}
			} else {
				ans += data[i].second / (double)(data[i].first + S);
			}
		}
		
		printf("Case #%d: %.10lf\n", nCase, ans);
	}
}

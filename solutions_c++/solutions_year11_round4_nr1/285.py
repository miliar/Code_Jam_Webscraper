#include <iostream>

using namespace std;

int main(){
	int TEST; cin >> TEST;
	static int cnt[101];
	for(int test=1;test<=TEST;test++){
		int X, S, R, t, N; cin >> X >> S >> R >> t >> N;
		memset(cnt, 0, sizeof(cnt));
		cnt[0] = X;
		for(int i=0;i<N;i++){
			int B, E, w; cin >> B >> E >> w;
			cnt[w] += E-B;
			cnt[0] -= E-B;
		}
		double res = 0;
		double lest = t;
		for(int i=0;i<=100;i++){
			if(cnt[i]==0) continue;
			if(lest < 1e-8){
				res += (double)cnt[i]/(S+i);
				lest = 0;
			}
			else if((double)cnt[i]/(R+i) < lest){
				res += (double)cnt[i]/(R+i);
				lest -= (double)cnt[i]/(R+i);
			}
			else{
				res += ((double)cnt[i]-lest*(R+i))/(S+i) + lest;
				lest = 0.0;
			}
		}
		printf("Case #%d: %.8lf\n", test, res);
	}
}

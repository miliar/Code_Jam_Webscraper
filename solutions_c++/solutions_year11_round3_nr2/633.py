#include<cstdio>
#include<vector>
#include<algorithm>
#include<iostream>
using namespace std;
int n;
int L, N, C;
long long t;
int Case = 0;
int main() {
	scanf("%d", &n);
	while(n--) {
        ++Case;
		scanf("%d %lld %d %d", &L, &t, &N, &C);

        int a[C];

        for(int i = 0; i < C; ++i) {
            scanf("%d", a + i);
        }

        int D[N];
        long long T[N];
        long long S[N];

        for(int i = 0; i < N; ++i) {
            D[i] = a[i % C];
            T[i] = (long long)(2*D[i]);
            S[i] = T[i] + ((i == 0) ? 0 : S[i-1]); 
        }

        long long ans = S[N-1], ans2;

        for(int i = 0; i < N; ++i) {
            long long t0 = ((i == 0) ? 0 : S[i-1]);
            long long d = max(0LL, t - t0);            
            long long trt = D[i] + d/2;
            long long gain = T[i] - trt;
            ans = min(ans, S[N-1] - gain);
        }

       
        if(L == 2) {
            ans2 = S[N-1];

            for(int i = 0; i < N-1; ++i) {
                for(int j = i+1; j < N; ++j) {
                    long long t0 = ((i==0)?0:S[i-1]);
                    long long d = max(0LL, t - t0);
                    long long trt = D[i] + d/2;
                    long long gain = T[i] - trt;                    
                    long long t1 = S[j-1] - gain;
                    long long d2 = max(0LL, t - t1);
                    long long trt2 = D[j] + d2/2;
                    long long gain2 = T[j] - trt2;
                    ans2 = min(ans2, S[N-1] - gain - gain2);
                }
            }
            ans = min(ans, ans2);
        }
        


        printf("Case #%d: %lld\n", Case, (L > 0) ?  ans : S[N-1]);

	}
	return 0;
}

#include <cstdio>
#include <algorithm>
using namespace std;

int t, l, n, ti, c, d[1000];

int main(void){
	scanf("%d", &t);
	for(int cas=1; cas<=t; cas++){
		scanf("%d%d%d%d", &l, &ti, &n, &c);
		for(int i=0; i<c; i++) scanf("%d", &d[i]);

		if(l==0){
			int cnt=0;
			for(int i=0; i<n; i++) cnt += d[i%c];
			printf("Case #%d: %d\n", cas, cnt*2);
		} else if(l==1) {
			int m = 1e9, cnt=0;
			for(int i=0; i<n; i++){
				cnt=0;
				for(int pos=0; pos<n; pos++){
					if(i==pos && cnt >= ti){
						cnt += d[pos%c];
					} else if ( i==pos) {
						cnt += 2*d[pos%c];
						if(cnt >= ti){
							cnt -= (cnt-ti)/2;
						}
					} else {
						cnt += 2*d[pos%c];
					}
				}
				m = min(cnt, m);
			}
			printf("Case #%d: %d\n", cas, m);
		} else if(l==2) {
			int m = 1e9, cnt = 0;
			for(int i=0; i<n-1; i++){
				for(int j=i+1; j<n; j++){
					cnt = 0;
					for(int k=0; k<n; k++){
						if(k==i){
							if(cnt >= ti){
								cnt += d[k%c];
							} else {
								cnt += 2*d[k%c];
								if(cnt > ti) cnt -= (cnt-ti)/2;
							}
						} else if (k==j){
							if(cnt >= ti){
								cnt += d[k%c];
							} else {
								cnt += 2*d[k%c];
								if(cnt > ti) cnt -= (cnt-ti)/2;
							}
						} else {
							cnt += 2*d[k%c];
						}
					}

					m = min(cnt, m);
				}
			}
			printf("Case #%d: %d\n", cas, m);
		}
	}
}

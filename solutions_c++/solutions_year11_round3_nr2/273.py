#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
#define int64 long long
int64 R[1000005];
int64 a[1000005];
int64 stk[1000005];
int k, n_case, r, n;
int64 mint;
int64 mindis;
int64 sum;
int64 del;
bool cmp(int x, int y){
	return x > y;	
}
int main(){
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int C;
	scanf("%d", &C);
	while(C--){
		scanf("%d%I64d%d%d", &k, &mint, &n, &r);
		for(int i = 0; i < r; i++){
			scanf("%I64d", R+i);
		}
		for(int i=0,cnt=0; i < n; i++,cnt++){
			if(cnt >= r) cnt-=r;
			a[i] = R[cnt];
		}
		/*for(int i = 0; i < n; i++){
			printf("%d\n", a[i]);	
		}
		return 0;*/
		mindis=mint/2;
		int f = 0, idx = -1, cnt=0;
		sum = 0;
		for(int i = 0; i < n; i++){
			sum += a[i];
			if(sum >= mindis && !f){
				f = 1;
				idx = i;
				if(sum != mindis){
					stk[cnt++] = sum - mindis;	
				}	
			}
		}
		printf("Case #%d: ", ++n_case);
		if(idx == -1){
			printf("%I64d\n", sum*2);
		} else {
			for(int i = idx+1; i < n; i++){
				stk[cnt++] = a[i];
			}
			sort(stk, stk+cnt, cmp);
			/*for(int i = 0; i < cnt; i++){
				printf("%d\n", stk[i]);	
			}
			return 0;*/
			del = 0;
			for(int i = 0, tmpk = 0; i < cnt&&tmpk < k; i++, tmpk++){
				del += stk[i];
			} 
			printf("%I64d\n", sum*2 - del);
		}
	}	
}

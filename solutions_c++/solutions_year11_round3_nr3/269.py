#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
int a[105];
int N, H, L, n_case=0;
int gcd(int a,int b)
{
	if (a<b) swap(a,b);
	if (!b) return a; return gcd(b,a%b);
};
int lcm(int a,int b)
{
	if(!(a*b)) return 0;
	else return a*(b/gcd(a,b));
};
int check(int k){
	for(int i = 0; i < N; i++){
		int tmp1 = k, tmp2 = a[i];
		if(tmp1 < tmp2) swap(tmp1, tmp2);
		if(tmp1 % tmp2 != 0) return 0;
	}
	return 1;
}
int main(){
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int C;
	scanf("%d", &C);
	while(C--){
		scanf("%d%d%d", &N, &L, &H);
		for(int i = 0; i < N; i++){
			scanf("%d", a+i);
		}
		printf("Case #%d: ", ++n_case);
		int f = 0, res;
		for(int r = L; r <= H; r++){
			if(check(r)) {
				f = 1; res = r;break;
			}
		}
		if(f){
			printf("%d\n", res);	
		} else printf("NO\n");
		/*(N == 1){
			if(a[0] >= L && a[0] <= H){
				printf("%d\n", a[0]);	
			}	else printf("NO\n");
			continue;
		} else{
			int res = a[0];
			for(int i = 1; i < N; i++){
				res = lcm(res, a[i]);	
			}
			printf("res = %d\n", res);
			if(res >= L && res <= H){
				printf("%d\n", res);	
			} else printf("NO\n");
		}*/
	}	
}

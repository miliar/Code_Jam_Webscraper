#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int tmp1[105], tmp2[105];
int cnt1,cnt2;
int tmp[105];
int a[1005];
int n,n_case=0;
int add(int a, int b){
	cnt1 = 0;
	memset(tmp1, 0, sizeof(tmp1));
	while(a>0){
		tmp1[cnt1++] = a%2;
		a /= 2;	
	}
	cnt2 = 0;
	memset(tmp2, 0, sizeof(tmp2));
	while(b > 0){
		tmp2[cnt2++] = b%2;
		b /= 2;	
	}
	for(int i = max(cnt1, cnt2) - 1; i >= 0; i--){
		tmp1[i] = tmp1[i] ^ tmp2[i];
	}
	int res = 0;
	for(int i = max(cnt1,cnt2)-1; i>= 0; i--){
		res = res*2+tmp1[i]; 	
	}
	return res;
}
int updatemax(int &a, int b){
	if(b > a){
		a = b;
		return 1;	
	}
	return 0;
}
void solve(){
	/*printf("\n%d\n", add(4, 5));
	printf("\n%d\n", add(7, 9));
	printf("\n%d\n", add(50, 10));
	return ;*/
	int S = 0;
	for(int i = 0; i < n; i++){
		S = add(S,a[i]);	
	}
	//printf("S = %d\n", S);
	if(S != 0){
		printf("Case #%d: NO\n", ++n_case);
		return;
	}
	int tot = 1<<n;
	int res = 0;
	for(int i = 1; i < tot-1; i++){
		int SS = 0, ss = 0, s = 0;
		for(int j = 0; j < n; j++){
			if(i&(1<<j)){
				SS = add(SS, a[j]);
				s+=a[j];
			} else {
				ss = add(ss, a[j]);
			}
		}
		if(SS == ss){
			//printf("ss = %d SS = %d\n", ss, SS);
			updatemax(res,s);
		}
	}
	printf("Case #%d: %d\n", ++n_case, res);
}
void input(){
	scanf("%d", &n);
	for(int i = 0; i < n; i++){
		scanf("%d", &a[i]);	
	}	
}

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int C;
	scanf("%d", &C);
	while(C--){
		input();
		solve();
	}	
}

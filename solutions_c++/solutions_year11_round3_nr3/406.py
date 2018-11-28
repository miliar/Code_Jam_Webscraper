#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <map>
using namespace std;
const int M = 210;
const int inf = 1000000000;
const double eps = 1e-8;
int n;
long long c,r;
long long num[10000];
long long gcd(long long a, long long b){
	return a == 0 ? b : gcd(b%a, a);
}
bool judge(long long tt){
	int i;
	for(i = 0; i < n;i ++){
		if(tt % num[i] == 0 || num[i]%tt == 0) continue;
		else return false;
	}
	return true;
}
long long solve(){
	int i;
	long long j;
	scanf("%d%lld%lld", &n, &r, &c);
	for(i = 0; i < n; i ++)
		scanf ("%lld", &num[i]);
	sort(num, num+n);
	for(j= r; j <=c; j ++){
		if(judge(j)) return j;
	}
	return -1;
	long long cc = 1, gc;
	/*for(i = 0; i < n; i ++){
		if(cc <= c && cc >= r){
			for(j = i; j < n; j ++){
				if(num[j] % cc == 0 || cc % num[j] == 0) continue;
				else break;
			}
			if(j == n) return cc;
		}
		gc = gcd(cc, num[i]);
		cc = cc /gc * num[i];
		if(cc >= )

	}*/
}
int main(){
	int cas;
	int i;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	scanf ("%d", &cas);
	for(i = 1; i <= cas; i ++){
		printf ("Case #%d: ", i);
		long long s = solve();
		if(s == -1) puts("NO");
		else printf ("%lld\n", s);
	}
	return 0;
}
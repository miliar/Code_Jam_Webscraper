#include <iostream>
#include <cstdio>
using namespace std;
int gcd(int a, int b){
	if(b > a) swap(a, b);
	if(b == 0) return a;
	return gcd(b, a%b);
}
long long n;
int main(){
	freopen("test.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		int a, b, res;
		cin>>n >>a >> b;
		if(a == 100) {
			//printf("go");
			if(b == 0)res = 0;
			else res = 1;
		}else if(a == 0){
			res = (b == 100?0:1);
		}else {
			int g = gcd(a, 100);
			//printf("g = %d\n", g);
			int left = 100 / g;
			if(n < left) res = 0;
			else {
				if(b == 100 || b == 0){
					res = 0;
				} else res = 1;
			}
		}
		//printf("%d %d %d\n", n, a, b);
		printf("Case #%d: %s\n", i, res == 0?"Broken":"Possible");	
	}
}

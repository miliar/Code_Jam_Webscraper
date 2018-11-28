#include<cstdio>
#include<cstring>
int N, pd, pg;
int gcd(int x, int y){
	return y == 0? x: gcd(y, x % y);
}
bool solve(){
	bool res = false;
	if(pg == 0){
		res = pd == 0;
	}
	else if(pg == 100){
		res = pd == 100;
	}
	else{
		if(pd == 0){
			res = true;
		}
		else{
			int lcm = 100 / gcd(100, pd) * pd;
			int t = lcm / pd;
			if(t <= N){
				res = true;
			}
		}
	}
	return res;
}
int main(){
	int T;
	scanf("%d", &T);
	for(int i=0;i<T;++i){
		scanf("%d%d%d", &N, &pd, &pg);
		printf("Case #%d: %s\n", i+1, solve() ? "Possible": "Broken");
	}
	return 0;
}

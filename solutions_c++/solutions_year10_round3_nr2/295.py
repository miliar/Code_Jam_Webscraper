#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

long long c, L, P;

int work(long long  x, long long y){
	if(x*c>=y) 
		return 0;
	long long  tx, ty;
	tx = x;
	ty = y;
	while(true){
		tx *= c;
		if(tx * c >= ty)
			return work(x, tx)+1;
		if(ty % c == 0)
			ty /= c;
		else 
			ty = ty/c+1;
		if(tx *c >= ty)
			return work(x, ty) + 1;
	}
}

int main() {
	int tc, t, ans;
	scanf("%d", &tc);
	for(t=1; t<=tc; t++){
		cin >> L >> P >> c;
		ans = work(L, P);
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}


#pragma warning(disable:4996)

#include <iostream>

int n, res;

template <typename Tp>
inline Tp max(Tp x, Tp y){
	return ((x < y) ? y : x);
}

void process(){
	int i, d, bl = 1, or = 1, lb = 0, lo = 0;
	char c;
	res = 0;
	scanf("%d ", &n);
	for(i = 0; i < n; i++){
		scanf("%c %d ", &c, &d);
		if(c == 'B'){
			res += max(0, abs(bl - d) - (res - lb));
			lb = ++res;
			bl = d;
		}
		else{
			res += max(0, abs(or - d) - (res - lo));
			lo = ++res;
			or = d;
		}
	}
}

int main(){
	int t, k;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for(k = 0; k < t; k++){
		process();
		printf("Case #%d: %d\n", k + 1, res);
	}
	fcloseall();
	return 0;
}
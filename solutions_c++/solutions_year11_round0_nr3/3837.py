#pragma warning(disable:4996)

#include <iostream>

#define N (15 + 5)

int n, res, sum;

int num[N] = {0, };

template <typename Tp>
inline Tp max(Tp x, Tp y){
	return ((x < y) ? y : x);
}

void back(int d, int s, int x, int y){
	if(d == n){
		if(x == y && s < sum){
			res = max(res, s);
		}
		return;
	}
	back(d + 1, s + num[d], x ^ num[d], y);
	back(d + 1, s, x, y ^ num[d]);
}

void process(){
	int i, s = 0;
	sum = res = 0;
	scanf("%d", &n);
	for(i = 0; i < n; i++){
		scanf("%d", &num[i]);
		s ^= num[i];
		sum += num[i];
	}
	if(s){
		return;
	}
	back(0, 0, 0, 0);
}

int main(){
	int i, t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for(i = 0; i < t; i++){
		process();
		if(res){
			printf("Case #%d: %d\n", i + 1, res);
		}
		else{
			printf("Case #%d: NO\n", i + 1);
		}
	}
	fcloseall();
	return 0;
}
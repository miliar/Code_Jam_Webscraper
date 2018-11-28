#include<iostream>

using namespace std;

/*
 * Get the greatest power of 10 less than n
 */
int tenPow(int n){
	int ans = 1;
	while(n >= 10){
		n /= 10;
		ans *= 10;
	}
	return ans;
}

int rotateOnce(int n, int pow){
	return pow * (n % 10) + n/10;
}

int main(){
	int T;
	scanf("%d\n", &T);
	for(int q = 1; q <= T; q++){
		int a, b;
		cin >> a >> b;
		int count = 0;
		int pow = tenPow(a);
		for(int i = a; i < b; i++){
			int cpy = i;
			while(true){
				cpy = rotateOnce(cpy, pow);
				if(cpy == i) break;
				if(cpy > i && cpy <= b) count++;
			}
		}
		printf("Case #%d: %d\n", q, count);
	}
}

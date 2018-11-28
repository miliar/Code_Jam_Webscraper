#include<stdio.h>
#include<set>

using namespace std;

int len = 0, put = 1;

int test(int a, int b) {
	int val = a, nr = 0;
	set<int> dif_num;
	for( int i = 1; i <= len; ++i) {
		val = val / 10 + (val % 10) * put;
		if( val <= b && val > a)
			dif_num.insert(val);
	}
	return dif_num.size();
}
int main() {
	
	freopen("numb.in", "r", stdin);
	freopen("numb.out", "w", stdout);
	
	int tt;
	scanf("%d", &tt);
	
	for( int i = 1; i <= tt; ++i) {
		int a, b, sol = 0;
		len = 0, put = 1;
		printf("Case #%d: ", i);
		scanf("%d %d", &a, &b);
		int atemp = a;
		while(a) 
			a/=10,len++, put *= 10;
		put/= 10;
		a = atemp;
		for( int j = a; j <= b; ++j){ 
			sol += test(j,b);
		}
		printf("%d\n", sol);
	}
	
	
	
	return 0;
}

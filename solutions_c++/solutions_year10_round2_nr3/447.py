#include <iostream>
#include <algorithm>
using namespace std;

int __builtin_popcount(unsigned x){
	int res = 0;
	while(x){
		++res;
		x &= x - 1;
	}
	return res;
}

int rank(int n, int s){
	return __builtin_popcount(((1 << (n - 1)) - 1) & s);
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	int CASE;
	scanf("%d", &CASE);
	for(int cas = 1; cas <= CASE; ++cas){
		int n, res = 0;
		scanf("%d", &n);
		for(int i = (1 << (n - 2)) - 1; i >= 0; --i){
			int s = i | (1 << (n - 2)), m = n;
			while(m > 1){
				if(!(s & (1 << (m - 2)))) break;
				m = rank(m, s);
			}
			if(m == 1) ++res;
		}
		res %= 100003;
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}
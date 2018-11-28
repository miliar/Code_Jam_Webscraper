#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

template <class Z>
Z gcd(Z a, Z b) {
	return b==0 ? a : gcd(b, a%b);
}

template <class Z> 
Z euclid(Z a, Z b, Z &x, Z &y) {
	if (b) { Z d = euclid(b, a % b, y, x);
		return y -= a/b * x, d; }
	return x = 1, y = 0, a;
}

int mod = 100003;
template<class Z> struct Mod {
	Z x;
	Mod(Z xx) : x(xx) {}
	Mod operator+(Mod b) { return Mod((x + b.x) % mod); }
	Mod operator-(Mod b) { return Mod((x - b.x + mod) % mod); }
	Mod operator*(Mod b) { return Mod((x * b.x) % mod); }
	Z inver(Z a) {
		Z x, y;
		euclid(a, Z(mod), x, y);
		return (mod + x) % mod;
	}
	Mod operator/(Mod b) {
		return Mod((x * inver(b.x)) % mod);
	}
};


template<class T>
T choose(int n, int k) {
	if(k>n || k<0) return T(0);
	k = min(k, n-k);
	T c(1);
	for(int i = 1; i <= k; ++i)
		c = c * T(n - i + 1) / T(i);
	return c;
}


template<class T>
T chooseModP(T m, T n/*, int p*/) { // Modified!!!
//	if(m==n) return 1;
	Mod<T> c(1);// mod = p;
	while((m + n) && c.x != 0) {
		c = c * choose<Mod<T> >(m % mod, n % mod);
		m /= mod; n /= mod;
	}
	return c.x;
}


int main() {
	int ways[550][550], ans[550];
	memset(ways, 0, sizeof(ways));
	memset(ans, 0, sizeof(ans));
	ways[1][0] = 1;
	ans[2]=ways[2][1] = 1;
	for(int n=3;n<50;++n) {
//		printf("%d\n",n);
		for(int i=0;i<n;++i) {
			// Suppose n has rank i in S
			for(int j=0;j<i;++j) {
				// i (in S) has rank j in ways[i][j] ways
				// i.e. can choose i-j-1 elements from n-i-1
				ways[n][i]+=choose<int>(n-i-1, i-j-1)*ways[i][j];
				ways[n][i]%=mod;
			}
			ans[n]+=ways[n][i], ans[n]%=mod;
		}
	}
/*	for(int i=0;i<26;++i)
		printf("%2d: %5d\n", i, ans[i]);
	for(int i=0;i<10;++i) {
		printf("%d:",i);
		for(int j=0;j<=i;++j) {
			printf("%4d ", ways[i][j]);
		}
		printf("\n");
	}*/
	int T;
	scanf("%d", &T);
	for(int t=0;t<T;++t) {
		int n;
		scanf("%d",&n);
		printf("Case #%d: %d\n", t+1, ans[n]);
	}
}
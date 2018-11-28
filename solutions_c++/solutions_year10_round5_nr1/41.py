#include <stdio.h>
#include <memory.h>
#include <vector>
#include <string>
#include <algorithm>
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define abs(x) ((x)>0?(x):-(x))
#define Bint long long
using namespace std;
int D, K;
int d[10];
pair<Bint,Bint> solve(Bint a, Bint b) {
	if (a % b == 0) return make_pair(0,1);
	pair<Bint,Bint> re = solve(b,a%b);
	re.second %= b; if (re.second < 0) re.second += b;
	return make_pair(re.second,(1-re.second*a)/b);
}
Bint gcd(Bint a, Bint b)
{return a % b ? gcd(b,a%b) : b;}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t, T, r, re;
	Bint i, j, k, A, B, a, b, c;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		scanf("%d%d",&D,&K);
		for (i = 0; i < K; i++) scanf("%d",&d[i]);
		if (K == 1) printf("I don't know.\n");
		else if (d[0] == d[1]) printf("%d\n",d[0]);
		else if (K == 2) printf("I don't know.\n");
		else {
			k = 1; for (i = 0; i < D; i++) k *= 10; D = k;			
			k = 2;
			for (i = 0; i < K; i++) {
				if (k < d[i]+1) k = d[i]+1;
			}
			r = -1;
			for (; k <= D; k++) {
				for (i = 2; i*i <= k; i++) {
					if (k % i == 0) break;
				}
				if (i*i <= k) continue;
//				printf("\np=%d:",k);
				a = (d[0]-d[1]+k)%k; b = k; c = d[1]-d[2];
				j = gcd(a,b);
				if (c % j == 0) {
					a /= j; b /= j; c /= j;
					A = (solve(a,b).first*c)%k; if (A < 0) A += k;
					B = (d[1]-A*d[0])%k; if (B < 0) B += k;
					re = (d[K-1]*A+B)%k; if (re < 0) re += k;
					for (i = 0; i+1 < K; i++) {
						if ((d[i]*A+B)%k != d[i+1]) break;
					}
					if (i+1 >= K) {
						if (r == -1) r = re;
						else if (r != re) {
							r = -1;
							break;
						}
					}
				}
			}
			if (r == -1) printf("I don't know.\n");
			else printf("%d\n",r);
		}
	}
	return 0;
}
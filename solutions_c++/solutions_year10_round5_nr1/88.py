#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
using namespace std;

#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define CLEAR(a,v) memset((a), (v), sizeof(a))

const double eps = 1e-9;
const int INF = 1000000000;
const long long LLINF = (long long)INF * INF;
const double PI = 2 * acos(.0);

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

const int MAXN = 1001000;
int prime[MAXN], plist[MAXN], pl;

int exp_mod(int a, int b, int p) {
	int s = 1;
	while (b) {
		if (b&1) {s = (int)((LL)s * a % p);}
		a = (int)((LL)a * a % p);
		b >>= 1;
	}
	return s;
}

inline int inv(int a, int p) {
	return exp_mod(a, p-2, p);
}

void initp() {
	int i, j;
	pl = 0;
	for (i = 2 ; i * i < MAXN ; i++)
		if (prime[i] == 0)
			for (j = i * i ; j < MAXN ; j += i)
				prime[j] = 1;
	for (i = 2 ; i < MAXN ; i++)
		if (prime[i] == 0) plist[pl++] = i;
}

int a[MAXN];
int k;

int check(int A, int B, int P) {
	int i;
	for (i = 1 ; i < k ; i++) {
		int tmp = (int)(((LL)a[i-1] * A + B) % P);
		if (tmp != a[i]) return 0;
	}
	return 1;
}

int main() {
	//freopen("a-small-attempt1.in","r",stdin);
	//freopen("a-small-attempt1.out","w",stdout);
	freopen("a-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	initp();
	int T, ca = 0, i, D;
	scanf("%d",&T);
	while (T--) {
		scanf("%d%d",&D,&k);
		int maxp = 1;
		for (i = 0 ; i < D ; i++)
			maxp *= 10;
		int maxa = 0;
		for (i = 0 ; i < k ; i++) {
			scanf("%d",&a[i]);
			maxa >?= a[i];
		}
		printf("Case #%d: ",++ca);
		if (k == 1) {
			printf("I don't know.\n");
			continue;
		} else if (k == 2) {
			if (a[0] == a[1]) printf("%d\n",a[0]);
			else printf("I don't know.\n");
			continue;
		} else {
			int ans = -1, flg = 1;
			for (i = 0 ; i < pl && plist[i] < maxp ; i++) {
				if (plist[i] <= maxa) continue;
				int P = plist[i];
				int t1 = ((a[1] - a[0]) % P + P) % P;
				int t2 = ((a[2] - a[1]) % P + P) % P;
				if (t1 == 0 || t2 == 0) {

				}
				int A = (int)((LL)t2 * inv(t1, P) % P);
				int B = (((LL)a[1] - (LL)A * a[0]) % P + P) % P;
				//printf("P:%d A:%d B:%d\n",P,A,B);
				if (check(A,B,P) == 0) continue;

				int next = (int)(((LL)a[k-1] * A + B) % P);

				if (ans == -1) {
					//printf("A:%d B:%d\n",A,B);
					ans = next;
				}
				else if (ans != next) {flg = 0; break;}
			}
			//if (flg == 0 || ans == -1) printf("I don't know.\n");
			if (flg == 0) printf("I don't know.\n");
			else printf("%d\n",ans);
		}
	}
	return 0;
}
/*
3
2 10
0 1 2 3 4 5 6 7 8 9
3 1
13
1 5
6 6 6 6 6
*/

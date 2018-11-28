#include<algorithm>
#include<cstdio>
#include<set>
#include<sstream>
#include<string>
#include<vector>
using namespace std;

const int MAXN=501;
const int SSIZE=MAXN;
int cache[MAXN];
int buf[MAXN];
int ranks[MAXN];

int extract(int x) {
	int i=0, n=2;
	while(x) {
		if (x&1)
			buf[i++] = n;
		x/=2;
		n++;
	}
	return i;
}

void rank(int sz) {
	fill(ranks, ranks+MAXN, -1);
	int x=1;
	for (int i=0; i<sz; i++) 
		ranks[buf[i]] = x++;	
}

bool is_pure(int x) {
	int sz = extract(x);
	rank(sz);
	int n = ranks[buf[sz-1]];
	while (n > 1) {
		n = ranks[n];
	}
	return n == 1;
}

int main() {
	int T;
	scanf("%d", &T);
	fill(cache, cache+MAXN, -1);
	for (int t=1; t<=T; t++) {
		int n; 
		scanf("%d", &n);
		if (cache[n]==-1) {
			int res=0;
			for (int i=(1<<(n-2)); i<(1<<(n-1)); i++) 
				if (is_pure(i))
					res++;
			cache[n] = res;
		}
		printf("Case #%d: %d\n", t, cache[n]%100003);
	}
	return 0;
}
#include <cstdio>
#include <cstring>
#include <algorithm>
#define maxn 27

using namespace std;

int v[maxn], n, i, j, tt, q, x[maxn];
char s[maxn];
bool ok;

void afis(int v[]) {
	int i;
	printf("Case #%d: ", q);
	for (i = 1; i <= n; i++)
		printf("%d", v[i]);
	printf("\n");
}

inline void hswap(int &a, int &b) {
	int aux;
	aux = a; a = b; b = aux;
}

inline bool posibil(int p) {
	int i, j, poz, min;
	bool ok = 0;
	min = 2000000000;
	for (i = p + 1; i <= n; i++)
		if (v[i] > v[p] && v[i] <= min) {
			min = v[i];
			poz = i;
			ok = 1;
		}
		
	if (ok) {
		hswap(v[poz], v[p]);
		sort(v + p + 1, v + n + 1);
		return true;
	}
	return false;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);	
	
	scanf("%d", &tt);
	for (q = 1; q <= tt; q++) {
		scanf(" %s ", s);
		n = 0;
		
		for (i = 0; s[i] != 0; i++) 
			v[++n] = s[i] - 48;
		memcpy(x, v, sizeof(v));
		ok = false;
		
		for (i = n - 1; i >= 1; i--) {
			memcpy(v, x, sizeof(v));
			if (posibil(i)) {
				afis(v);
				ok = true;
				break;
			}
		}
		
		if (!ok) {
			n++;
			v[n] = 0;
			sort(v + 1, v + n + 1);
			for (i = 1; i <= n; i++)
				if (v[i] != 0) {
					hswap(v[i], v[1]);
					break;
				}
			afis(v);
		}
	}
	
	return 0;
}
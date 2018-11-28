#include <cstdio>
#include <cstring>

const int maxn = 10000;

int casei, cases, h0, h1, h2, h3, w0, w1, w2, w3, n, m;
int n1[maxn], n2[maxn], n3[maxn];
char st[10000], lies[10000];

inline void init() {
	scanf("%d", &n);
	gets(lies);
	for (int i = 0; i < n; ++i) {
		gets(lies);
		sscanf(lies, "%d%d %s", &n1[i], &n2[i], st);
		if (st[0] == 'B') n3[i] = 1;
		else n3[i] = 0;
	}
}

inline int process() {
	h0 = -1; h1 = -1; h2 = -1; h3 = 1000000000;
	w0 = -1; w1 = -1; w2 = -1; w3 = 1000000000;
	for (int i = 0; i < n; ++i) 
		if (n3[i]) {
			if (h1 == -1) {
				h1 = n1[i]; h2 = n1[i];
			}
			h2 >?= n1[i];
			h1 <?= n1[i];
			
			if (w1 == -1) {
				w1 = n2[i]; w2 = n2[i];
			}
			w2 >?= n2[i];
			w1 <?= n2[i];
		}
		
	for (int i = 0; i < n; ++i) 
		if (!n3[i]) {
			if (n1[i] <= h2 && n1[i] >= h1 && n2[i] <= w2 && n2[i] >= w1) return -1;
		}
		
	return 1;
}


inline void print() {
	printf("Case #%d:\n", casei);

	scanf("%d", &m);
	int tmp1, tmp2, r1, r2;
	++n;
	for (int i = 0; i < m; ++i) {
		scanf("%d%d", &tmp1, &tmp2);
		n1[n - 1] = tmp1; n2[n - 1] = tmp2; 
		
		n3[n - 1] = 1;
		r1 = process();
		n3[n - 1] = 0;
		r2 = process();
		
		if (r1 == 1 && r2 == -1) printf("BIRD\n");
		else
			if (r1 == -1 && r2 == 1) printf("NOT BIRD\n");
			else printf("UNKNOWN\n");
	}
}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("la.out", "w", stdout);
	
	
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}
	
	return 0;
}

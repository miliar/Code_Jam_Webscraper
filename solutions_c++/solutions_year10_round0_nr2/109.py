#include <stdio.h>
#include <string.h>

#define MAXN 150000

int l[MAXN], r[MAXN], c[MAXN], cl[MAXN], cr[MAXN], des[MAXN];

void init(int k, int b, int e){
	l[k] = b;
	r[k] = e;
	c[k] = cl[k] = cr[k] = e - b + 1;
	if(b == e) return;
	int m = (l[k] + r[k]) >> 1;
	init(k << 1, b, m);
	init((k << 1) + 1, m + 1, e);
}

void update(int k, int pos, int v){
	if(l[k] == r[k]){
		c[k] = cl[k] = cr[k] = v;
		return;
	}
	int m = (l[k] + r[k]) >> 1;
	if(pos <= m) update(k << 1, pos, v);
	else update((k << 1) + 1, pos, v);
	c[k] = c[k << 1] > c[(k << 1) + 1]? c[k << 1]: c[(k << 1) + 1];
	if(cl[k << 1] == m - l[k] + 1) cl[k] = m - l[k] + 1 + cl[(k << 1) + 1];
	else cl[k] = cl[k << 1];
	if(cr[(k << 1) + 1] == r[k] - m) cr[k] = r[k] - m + cr[k << 1];
	else cr[k] = cr[(k << 1) + 1];
	if(cr[k << 1] + cl[(k << 1) + 1] > c[k]) c[k] = cr[k << 1] + cl[(k << 1) + 1];
}

int query(int k, int pos){
	if(l[k] == r[k]) return c[k];
	int m = (l[k] + r[k]) >> 1;
	if(pos <= m){
		if(m - cr[k << 1] + 1 <= pos) return cr[k << 1] + cl[(k << 1) + 1];
		else return query(k << 1, pos);
	}
	else{
		if(cl[(k << 1) + 1] + m >= pos) return cr[k << 1] + cl[(k << 1) + 1];
		else return query((k << 1) + 1, pos);
	}
}

int main(){
	int n, m, top = 0;
	char s[2];
	scanf("%d%d", &n, &m);
	init(1, 1, n);
	for(int i = 0; i < m; ++i){
		scanf("%s", s);
		if(s[0] == 'D'){
			scanf("%d", &n);
			update(1, n, 0);
			des[top++] = n;
		}
		else if(s[0] == 'Q'){
			scanf("%d", &n);
			printf("%d\n", query(1, n));
		}
		else
			update(1, des[--top], 1);
	}
	return 0;
}
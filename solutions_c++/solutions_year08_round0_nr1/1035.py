#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define nsize 110

char ch[100][nsize], qstr[nsize];
int m, flag[nsize];

int cmp(const void *a, const void *b) {
	return strcmp((char *)a, (char *)b);
}

int bsearch() {
	int pre = 0, post = m, mid;
	while ( pre <= post ) {
		mid = (pre+post)>>1;
		if ( strcmp(ch[mid], qstr) < 0 ) pre = mid + 1;
		else post = mid - 1;
	}
	return pre;
}

int main() {
	//*
	freopen("inSave.txt", "r", stdin);
	freopen("ansSave.txt", "w", stdout);
	//*/
	
	int n, s, q, res, cnt, i;	
	scanf("%d", &n);
	for ( int kase = 1; kase <= n; kase++ ) {
		scanf("%d", &s);
		m = s - 1;
		fgets(qstr, nsize, stdin);
		for ( i = 0; i < s; i++ ) {
			fgets(ch[i], nsize, stdin);
		}
		qsort(ch, s, sizeof(char)*nsize, cmp);
		
		scanf("%d", &q);
		fgets(qstr, nsize, stdin);
		res = 0; cnt = 0;
		memset(flag, 0, sizeof(flag));
		while ( q-- ) {
			fgets(qstr, nsize, stdin);
			i = bsearch();
			if ( !flag[i] ) {
				flag[i] = 1; cnt++;
			}
			if ( cnt == s ) {
				memset(flag, 0, sizeof(flag));
				flag[i] = 1; cnt = 1; res++;
			}
		}		
		printf("Case #%d: %d\n", kase, res);
	}
	return 0;
}

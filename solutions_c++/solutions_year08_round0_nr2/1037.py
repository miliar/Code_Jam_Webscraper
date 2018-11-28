#include <stdio.h>
#include <stdlib.h>

int time[200][3], m, t;

int cmp(const void *a, const void *b) {
	int *aa = (int *)a;
	int *bb = (int *)b;
	if ( aa[1] == bb[1] ) return aa[2] - bb[2];
	return aa[1] - bb[1];
}

int bsearch(int i) {
	int pre, mid, post;	
	int flag = !time[i][0];
	int dst = time[i][2] + t;
	time[i][0] = 2;
	pre = i + 1; post = m - 1;
	while ( pre <= post ) {
		mid = (pre+post)>>1;
		if ( time[mid][1] < dst ) pre = mid + 1;
		else post = mid - 1;
	}
	for ( i = pre; i < m; i++ ) {
		if ( time[i][0] == flag ) break;
	}
	return i;
}

int main() {
	//*
	freopen("B-large.in", "r", stdin);
	freopen("ansTrainLarge.txt", "w", stdout);
	//*/
	int n, na, nb;
	
	int i, j, h, s;
	scanf("%d", &n);
	for ( int kase = 1; kase <= n; kase++ ) {
		scanf("%d %d %d", &t, &na, &nb);
		m = na + nb;
		for ( i = 0; i < m; i++ ) {
			if ( i < na ) time[i][0] = 0;
			else time[i][0] = 1;
			
			scanf("%d:%d", &h, &s);
			time[i][1] = h*60 + s;
			
			scanf("%d:%d", &h, &s);
			time[i][2] = h*60 + s;
		}
		qsort(time, m, sizeof(time[0]), cmp);
		
		na = 0; nb = 0;
		for ( i = 0; i < m; i++ ) if ( 2 != time[i][0] ) {
			if ( !time[i][0] ) na++;
			else nb++;
			j = i;
			while ( j < m ) {
				j = bsearch(j);
			}			
		}
		printf("Case #%d: %d %d\n", kase, na, nb);
	}
	return 0;
}

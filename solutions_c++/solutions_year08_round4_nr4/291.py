#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

int k;
char s[1 << 10];
char b[1 << 10];
int a[8];

void read() {
	scanf ("%d",&k);
	scanf ("%s",s);
}

void solve() {
	int i , j;
	int cur;
	int ans = (1<<30);
	int n = (int)strlen ( s );
	
	for (i=0;i<k;i++) a[i] = i;
	
	do {
		for (i=0;i<n;i+=k)
			for (j=0;j<k;j++)
				b[i + j] = s[ i + a[j] ];
		
		cur = 1;
		for (i=1;i<n;i++)
			if ( b[i] != b[i - 1] ) 
				++ cur; 
		if ( cur < ans ) ans = cur;
	} while ( next_permutation ( a , a + k ) );
	
	printf ("%d\n",ans);
}

int main() {
	int k;
	int i;
	
	scanf ("%d",&k);
	
	for (i=1;i<=k;i++) {
		printf ("Case #%d: ",i);
		read();
		solve();
	}

	return 0;
}

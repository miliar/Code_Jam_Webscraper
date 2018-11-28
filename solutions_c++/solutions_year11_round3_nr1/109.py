#include <stdio.h>
#include <string.h>
char in[100][100];
int main () {
	freopen ("A-large.in","r",stdin);
	freopen ("a-large.out","w",stdout);
	int t;
	scanf ("%d",&t);
	for (int ca=1;ca<=t;ca++) {
		int n,m;
		scanf ("%d%d",&n,&m);
		for (int i=0 ;i<n;i++) {
			scanf ("%s",in[i]);
		}
		printf ("Case #%d:\n",ca);
		bool ok = 1;
		for (int i=0;i<n;i++) {
			for (int j=0;j<m;j++) {
				if (in[i][j] == '#') {
					if (i==n-1 || j == m-1) {
						printf ("Impossible\n");
						ok=0;
						break;
					}
					if (in[i][j+1]!='#' || in[i+1][j]!='#' || in[i+1][j+1]!='#') {
						printf ("Impossible\n");
						ok=0;
						break;
					}
					in[i][j]='/';
					in[i][j+1]='\\';
					in[i+1][j]='\\';
					in[i+1][j+1]='/';
				}
			}
			if (ok == 0) break;
		}
		if (ok) {
			for (int i=0;i<n;i++) {
				printf ("%s\n",in[i]);
			}
		}					
	}
	
	return 0;
}

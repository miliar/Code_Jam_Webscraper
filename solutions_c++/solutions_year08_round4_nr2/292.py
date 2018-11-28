#include <cstdio>

int n , m , cp;

void read() {
	scanf ("%d%d%d",&n,&m,&cp);
}

void solve() {
	int i , j , k , d;
	
	for (i=0;i<=n;i++)
		for (j=0;j<=m;j++)
			for (k=0;k<=n;k++)
				for (d=0;d<=m;d++)
					if ( i * d - j * k == cp || i * d - j * k == -cp ) {
						printf ("0 0 %d %d %d %d\n",i,j,k,d);
						return ;
					}
					
	printf ("IMPOSSIBLE\n");
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

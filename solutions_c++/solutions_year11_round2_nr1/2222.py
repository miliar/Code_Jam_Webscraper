// kronig 	thiagokronig@gmail.com

#include <cstdio>

int main() {

	int tt;
	int T;
	
	int i,j;
	
	int n;
	
	int x[1000][1000];
	int z[1000][1000];
	char s[1000];
	
	double games;
	
	double a[1000];
	double b[1000];
	double c[1000];
	double g[1000];
		
	scanf("%d", &T);
	
	for (tt=1; tt<=T; tt++) {

		scanf("%d",&n);
		
		for (i=0; i<n; i++) {
			scanf("%s", s);
			for (j=0; j<n; j++) {
				z[i][j] = (s[j] != '.');
				x[i][j] = (s[j] == '1');
			}
		}
		
		for (i=0; i<n; i++) {
			g[i] = 0;
			for (j=0; j<n; j++) {
				g[i] += z[i][j];
			}
		}
		
		for (i=0; i<n; i++) {
			a[i] = 0;
			for (j=0; j<n; j++) {
				a[i] += x[i][j] * z[i][j];
			}
			if (g[i])
				a[i] /= g[i];
			else
				a[i] = 0.0;
		}
		
		for (i=0; i<n; i++) {
			b[i] = 0;
			for (j=0; j<n; j++) {
				b[i] += (g[j] - z[j][i]) == 0 ? 0 : z[i][j] * (a[j] * g[j] - x[j][i] * z[j][i]) / (g[j] - z[j][i]);
			}
			if (g[i])
				b[i] /= g[i];
			else
				b[i] = 0.0;
		}
		
		for (i=0; i<n; i++) {
			c[i] = 0;
			for (j=0; j<n; j++) {
				c[i] += b[j] * z[i][j];
			}
			if (g[i])
				c[i] /= g[i];
			else
				c[i] = 0.0;
		}
		
		printf("Case #%d:\n", tt);
		for (i=0; i<n; i++) {
			printf("%.10lf\n", 0.25 * a[i] + 0.5 * b[i] + 0.25 * c[i]);
		}
		
	}

	return 0;
}
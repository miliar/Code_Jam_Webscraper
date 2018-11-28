#include <iostream>

using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define N 110

char a[N][N];
int n;

double ans[N], owp[N], wp[N], oowp[N];

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);

    int tk;
    scanf("%d\n", &tk);

    for (int tc = 1; tc <= tk; ++tc) {
    	printf("Case #%d:\n", tc);
    	scanf("%d\n", &n);

    	forn(i, n)
    		gets(a[i]);

    	forn(i, n) {
    		int w = 0, t = 0;
    		forn(j, n) {
    			if (a[i][j] != '.') ++t;
    			if (a[i][j] == '1') ++w;
    		}
    		wp[i] = 1.0 * w / t;
    		ans[i] = 0.25 * wp[i];
    		double s = 0;
    		double op = 0;
    		forn(j, n) {
    			if (j == i || a[i][j] == '.') continue;
    			
    			w = t = 0;
    			forn(k, n)
    				if (k != i) {
    					if (a[j][k] != '.') ++t;
		    			if (a[j][k] == '1') ++w;
    				}
    			s += 1.0 * w / t;
    			op++;
    		}
    		owp[i] = s / op;
    		ans[i] += 0.5 * owp[i];
    	}

    	forn(i, n) {
    		double s = 0;
    		double op = 0;
    		forn(j, n)
    			if (j != i && a[i][j] != '.') {
    				s += owp[j];
    				++op;
    			}

    		ans[i] += 0.25 * s / op;
    	}
		    		
    	forn(i, n)
    		printf("%.12lf\n", ans[i]);
    	printf("\n");

    	fprintf(stderr, "Solved %d\n", tc);
    }
	
	return 0;
}
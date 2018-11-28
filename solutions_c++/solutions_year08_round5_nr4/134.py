#include <iostream>
using namespace std;

const int mx=200, mdl=10007;
const int dr[2][2] = { 2,1, 1,2 };

int g[mx][mx], done[mx][mx];
int ts, n, m, num, x, y, i, j, o, k;

main() {
       freopen("b.in", "r", stdin);
       freopen("b.out", "w", stdout);
       
       for (cin >> ts; ++o <= ts;) {
           cin >> n >> m >> num;
		   memset(done, 0, sizeof(done));
		   memset(g, 0, sizeof(g)); 
           g[1][1] = 1;
		   for (i=1; i<=num; i++) {
               cin >> x >> y;
			   done[x][y] = 1;
		    }

		    for (i=1; i<=n; i++) for (j=1; j<=m; j++) if (!done[i][j]) {
			    for (k=0; k<=1; k++)
			    if (i-dr[k][0]>=1 
                 && j-dr[k][1]>=1 
                 && !done[i-dr[k][0]][j-dr[k][1]]) 
				    g[i][j] += g[i-dr[k][0]][j-dr[k][1]],
                    g[i][j] %= mdl;
		    }
           cout << "Case #" << o << ": " << g[n][m] << endl;
       }
}

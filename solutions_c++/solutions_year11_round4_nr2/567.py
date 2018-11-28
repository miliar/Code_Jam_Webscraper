#include <iostream>
#include <string>
#include <cmath>
using namespace std;
const double zero = 1e-6;
const int MAXN = 1000 + 100; 
char map[MAXN][MAXN];
double w[MAXN][MAXN], Xw[MAXN][MAXN], Yw[MAXN][MAXN];
int n,m,d,tests, test;

bool judge( int l ){
    int i, j; 
	for ( i = l; i <= n; ++i )
		for ( j = l; j <= m; ++j ){
			double sumx = Xw[i][j]-Xw[i-l][j]-Xw[i][j-l]+Xw[i-l][j-l]-map[i][j]*i-map[i-l+1][j]*(i-l+1)-map[i][j-l+1]*i-map[i-l+1][j-l+1]*(i-l+1);
			double sumy = Yw[i][j]-Yw[i-l][j]-Yw[i][j-l]+Yw[i-l][j-l]-map[i][j]*j-map[i-l+1][j]*j-map[i][j-l+1]*(j-l+1)-map[i-l+1][j-l+1]*(j-l+1);
			double sumw = w[i][j]-w[i-l][j]-w[i][j-l]+w[i-l][j-l]-map[i][j]-map[i-l+1][j]-map[i][j-l+1]-map[i-l+1][j-l+1];
			if ( fabs(sumx*2-(i+i-l+1)*sumw)<zero && fabs(sumy*2-(j+j-l+1)*sumw)<zero ) return true;
		}
	return false;
}

int main(){
    freopen("2.in","r",stdin); 
    freopen("2.out","w",stdout);
    
    scanf("%d",&tests);
     int i, j, ans; char ch; 
    for (test = 1; test <= tests; ++test){
		scanf("%d %d %d",&n,&m,&d);
		for ( i=1; i<=n; ++i )
			for ( j=1; j<=m; ++j ){
				scanf(" %c", &ch);
				map[i][j] = ch - '0';
				w[i][j] = map[i][j] + w[i-1][j] + w[i][j-1] - w[i-1][j-1];
				Xw[i][j] = map[i][j] * i + Xw[i-1][j] + Xw[i][j-1] - Xw[i-1][j-1];
				Yw[i][j] = map[i][j] * j + Yw[i-1][j] + Yw[i][j-1] - Yw[i-1][j-1];
			}
		ans = 0; 
		
		for ( int k = min(n,m); k > 2; --k )
			if ( judge(k) ){
				ans = k; break;
			}

		if (!ans) printf("Case #%d: IMPOSSIBLE\n", test); else
               printf("Case #%d: %d\n", test, ans);    
	}
}

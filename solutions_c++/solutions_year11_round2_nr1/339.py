#include <cstdio>
#include <cstring>

int n;
char a[128][128];
double wp[128] , owp[128] , oowp[128] , rpi[128];

void read() {
	int i;
	
	scanf ( "%d" , &n );
	for (i = 0; i < n; i++)
		scanf ( "%s" , a[i] );
}

void solve() {
	int i , j , k;
	double wins , all , all2 , tot;
	
	for (i = 0; i < n; i++) {
		wins = all = 0;
		
		for (j = 0; j < n; j++)
			if ( a[i][j] != '.' ) {
				++ all;
				if ( a[i][j] == '1' )
					++ wins;
			}
			
		wp[i] = wins / all;
	}
	
	for (i = 0; i < n; i++) {
		all = 0;
		tot = 0;
		
		for (j = 0; j < n; j++) 
			if ( a[i][j] != '.' ) {
				wins = 0;
				all2 = 0;
				
				for (k = 0; k < n; k++)
					if ( k != i )
						if ( a[j][k] != '.' ) {
							all2 ++;
							
							if ( a[j][k] == '1' )
								++ wins;
						}
						
				++ all;
				tot += wins / all2;
			}
			
		owp[i] = tot / all;
	}
	
	for (i = 0; i < n; i++) {
		all = 0;
		tot = 0;
		
		for (j = 0; j < n; j++)
			if ( a[i][j] != '.' ) {
				++ all;
				tot += owp[j];
			}
			
		oowp[i] = tot / all;
		rpi[i] = wp[i] / 4 + owp[i] / 2 + oowp[i] / 4;
		printf ( "%.10lf\n" , rpi[i] );
	}
}

int main() {
	int i , cases;
	
	scanf ( "%d" , &cases );
	for (i = 1; i <= cases; i++) {
		read();
		printf ( "Case #%d:\n" , i );
		solve();
	}
	
	return 0;
}

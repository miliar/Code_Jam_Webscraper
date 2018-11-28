#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");
#define cin fin
#define cout fout

int t, n, test = 1;
double wp[200], owp[200];
int cnt[200];
char mp[200][200];

int main() {
	for( cin >> t; t--; ) {
		memset( wp, 0, sizeof wp );
		memset( owp, 0, sizeof owp );
		memset( cnt, 0, sizeof cnt );
		cin >> n;
		for( int i = 0; i < n; i++ )
			for( int j = 0; j < n; j++ )
				cin >> mp[i][j];
		cout << "Case #" << test++ << ":" << endl;
		for( int i = 0; i < n; i++ ) {
			int tot = 0, w = 0;
			for( int j = 0; j < n; j++ ) {
				if( mp[i][j] != '.' )	cnt[i]++;
				if( mp[i][j] == '1' )	w++;
			}
			wp[i] = (double) w / cnt[i];
			for( int j = 0; j < n; j++ ) {
				if( mp[i][j] == '.' )	continue;
				tot = w = 0;
				for( int k = 0; k < n; k++ ) {
					if( i == k )	continue;
					if( mp[j][k] != '.' )	tot++;
					if( mp[j][k] == '1' )	w++;
				}
				owp[i] += (double) w / tot;
			}
			owp[i] /= (double)cnt[i];
		}
		for( int i = 0; i < n; i++ ) {
			double oowp = 0.;
			for( int j = 0; j < n; j++ ) {
				if( mp[i][j] == '.' )	continue;
				oowp += owp[j];
			}
			oowp /= cnt[i];
			cout.precision( 8 );
			cout.setf(ios::fixed | ios::showpoint);
			cout << wp[i] / 4. + owp[i] / 2. + oowp / 4 << endl;
		}
	}
	return 0;
}
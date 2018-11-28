#include <iostream>
#include <fstream>
#define cin fin
#define cout fout
#define MAX 10006
using namespace std;

int cnt[MAX];
int n, l, h;
ifstream fin( "C-small-attempt0.in" );
ofstream fout( "o.txt" );

int main(){
	int t, res;
	cin >> t;
	for( int T = 1; T <= t; T++ ){
		cin >> n >> l >> h;
		res = -1;
		memset( cnt, 0, sizeof cnt );
		for( int i = 0; i < n; i++ ){
			int num;
			cin >> num;
			for( int i = l; i <= h; i++ )
				if( i % num == 0 || num % i == 0 )
					cnt[i]++;
		}
		for( int i = l; i <= h; i++ ){
			//cout << cnt[i] << endl;
			if( cnt[i] == n ){
				res = i;
				break;
			}
		}
		cout << "Case #" << T << ": ";
		if( res == -1 )
			cout << "NO" << endl;
		else cout << res << endl;
	}
	return 0;
}
#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

ifstream fin("D-large.in");
ofstream fout("D-large.out");
#define cin fin
#define cout fout

int arr[20];
bool mark[20];
int any[20];
double res[2000];
int t, n, test = 1;

int main() {
	for( cin >> t; t--; ) { 
		cin >> n;
		int res = n;
		for( int i = 0; i < n; i++ ) {
			cin >> arr[i];
			if( arr[i] == i + 1 )
				res--;
		}
		
		cout << "Case #" << test++ << ": " << res << endl;
	}
	/*res[1] = 0;
	for( int i = 2; i <= 6; i++ ) {
		for( int j = 1; j < i; j++ )
			res[i] += res[j] / j;
		res[i]++;
		res[i] *= (double)i / (i - 1);
		cout << res[i] << endl;
	}
	cin >> n;*/
	/*while( cin >> n ) {
		memset( any, 0, sizeof any );
		for( int i = 0; i < n; i++ )
			arr[i] = i;
		do {
			memset( mark, false, sizeof mark );
			for( int i = 0; i < n; i++ ) {
				if( !mark[i] ) {
					int cnt = 0;
					int cur = i;
					while( !mark[cur] ) {
						cnt++;
						mark[cur] = true;
						cur = arr[cur];
					}
					any[cnt]++;
				}
			}
		} while( next_permutation( arr, arr + n ) );
		for( int i = 1; i <= n; i++ )
			cout << any[i] << ' ';
		cout << endl;
	}*/
	return 0;
}
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <fstream>

#define MAX ( 1 << 20 )
using namespace std;
#define cout fout
#define cin fin
ofstream fout( "codeJC.txt" );
ifstream fin( "C-large.in" );
int arr[2000];
int n;
int Xarr[MAX];
int need[MAX];


int main()
{
	int t;
	cin >> t;
	for( int T = 1; T <= t; T++ ){
		int X = 0, sm = 0;
		cin >> n;
		memset( Xarr, -1, sizeof Xarr );
		for( int i = 0;i < n; i++ ){
			//scanf( "%d", &arr[i] );
			fin >> arr[i];
			sm += arr[i];
			X ^= arr[i];
		}
		cout << "Case #" << T << ": ";
		Xarr[0] = 0;
		if( X != 0 )
			cout << "NO" << endl;
		else{
			for( int i = 0;i < n; i++ ){
				memset( need, -1, sizeof need );
				for( int j = 0;j < MAX; j++ )
					if( Xarr[j] != -1 ){
						int val = j ^ arr[i];
						if( Xarr[val] == -1 || ( arr[i] + Xarr[j] != sm ) )
							need[val] = max( Xarr[val], arr[i] + Xarr[j] );
					}
				for( int j = 0;j < MAX; j++ )
					if( need[j] != -1 )
						Xarr[j] = need[j];
				/*for( int j = 0;j < 15; j++ )
					cout << Xarr[j] << ' ';
				cout << endl;
				*/
			}
			int res = 0;
			for( int i = 0;i < MAX; i++ )
				res = max( res, Xarr[i] );
			cout << res << endl;
		}
	}
	return 0;
}
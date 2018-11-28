#include <iostream>
#include <fstream>

#define MAX 1000007
using namespace std;
#define cin fin
#define cout fout

ifstream fin( "C-large(2).in" );
ofstream fout( "o.txt" );

bool mark[MAX];
int id[MAX], ptr = 0;
int pr[MAX];
int fact[MAX][20];
int how[MAX][20];
int deg[MAX];
long long test, n;
int arr[MAX];

long long getSq( long long v ){
	long long l = 1, r = 1000000, res = -1;
	while( l <= r ){
		long long mid = ( l + r ) / 2;
		if( mid * mid >= v )
			res = mid, r = mid - 1;
		else l = mid + 1;
	}
	return res;
}

int main()
{
	for( int i = 2; i < MAX; i++ )
		if( !mark[i] ){
			id[i] = ptr;
			pr[ptr++] = i;
			for( int j = i; j < MAX; j += i ){
				mark[j] = true, fact[j][deg[j]] = i;
				int tmp = j;
				while( tmp % i == 0 )
					tmp /= i, how[j][deg[j]]++;
				deg[j]++;
			}
		}
	//cout << "HERE " << endl;
	cin >> test;
	for( int T = 1; T <= test; T++ ){
		memset( arr, 0, sizeof arr );
		cin >> n;
		long long s = getSq( n );
		long long mx = 0, mn = 0;
		for( int i = 0;i < ptr; i++ ){
			if( pr[i] > s )
				break;
			long long p = 0, now = 1;
			long long pp = n;
			while( pp )
				p++, pp /= pr[i];
			p--;
			if( p )
				mn++;
			mx += p;
		}
		cout << "Case #" << T << ": ";
		if( n == 1 )
			cout << 0 << endl;
		else cout << mx - mn + 1 << endl;
	}
	return 0;
}
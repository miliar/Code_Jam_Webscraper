#include<algorithm>
#include<cstdio>
#include<vector>
#include<string>

using namespace std;

int k, ss;
string s;


bool Read(){
	char buf[50005];
	scanf("%d%d", &k, &ss);
	scanf("%s", buf );
	s = buf;
	return true;
}

vector<int> d;
string sn;
int res;

int dp( int t ){
	if( t == k - 1 ){
		for(int i = 0; i < s.size(); ++i){
			sn[ i ] = s[ i - i%k + d[i%k] ];
		}
		int r = 1;
		for(int i = 1; i < sn.size(); ++i){
			if( sn[i] != sn[i-1] )r++;
		}
		res = min( res, r );
		return 0;
	}
	for(int i = t; i < k; ++i){
		swap( d[i], d[t] );
		dp( t + 1 );
		swap( d[i], d[t] );
	}
	return 0;
}

int Solve(){
	d.assign( k, 0 );
	res = s.size();
	sn = s;
	for(int i = 0; i < k; ++i){
		d[i] = i;
	}
	dp( 0 );

	return res;
}

void Write( int num, int ans ){
	printf( "Case #%d: %d\n", num, ans );
}

int main(){
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	int n;
	scanf( "%d", &n );
	for(int i = 0; i < n; ++i){
		Read();
		Write( i+1, Solve() );
	}

	return 0;
}
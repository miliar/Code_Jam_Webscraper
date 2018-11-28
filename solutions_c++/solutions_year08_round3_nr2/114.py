#include<algorithm>
#include<cstdio>
#include<vector>
#include<string>

using namespace std;

string s;

bool Read(){
	char buf[500];
	scanf( "%s", buf );
	s = buf;
	return true;
}

long long Solve(){
	vector< vector<long long> > ms;
	ms.assign( s.size(), vector<long long>( 210, 0 ) );
	int zero = 210;
	long long res = 0;
	for(int i = 0, ost = 0; i < s.size(); ++i ){
		ost = (ost * 10 + s[i] - '0') % 210;
		ms[i][ost] = 1;
	}
	for(int i = 1; i < s.size(); ++i){
		for(int j = 0; j < 210; ++j ){
			if( ms[i-1][j] != 0 ){
				ms[i][ (210 + j + (s[i] - '0')) % 210 ] += ms[i-1][j];
				ms[i][ (210 + j - (s[i] - '0')) % 210 ] += ms[i-1][j];
				for(int k = i + 1, ost = (s[i] - '0'); k < s.size(); ++k ){
					ost = ( ost * 10 + s[k] - '0' ) % 210;
					ms[k][ (210 + j + ost ) % 210 ] += ms[i-1][j];
					ms[k][ (210 + j - ost ) % 210 ] += ms[i-1][j];
				}
			}
		}
	}	
	int rr = 0;
	for(int i = 0; i < 210; ++i){
		if( ms[s.size()-1][i] != 0 ) rr += ms[s.size()-1][i];
		if( i % 7 == 0 || i%5 == 0 || i % 3 == 0 || i % 2 == 0 )res += ms[s.size() - 1 ][i];
	}
	return res;
}

void Write( int num, long long ans ){
	printf( "Case #%d: %lld\n", num, ans );
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
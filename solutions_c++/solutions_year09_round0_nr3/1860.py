#include <iostream>
#include <string>
using namespace std;

string s;
const int MOD = 10000;
const string msg = "welcome to code jam";
int cache[500][20];
int doit( int i, int j ) {
	int &ret = cache[i][j];
	if( ret != -1 ) return ret;
	if(j==msg.size()) return 1;
	if( i >= s.size() ) return 0;
	ret = 0;
	if( s[i] == msg[j] ) {
		ret = ( ret + doit( i+1, j+1 ) ) % MOD;
	}
	ret = ( ret + doit( i+1, j ) ) % MOD;
	return ret;
}

int main() {
	freopen("pc.in","r",stdin);
	int tn;
	cin >> tn;
	getline(cin,s);
	for(int cc=1;cc<=tn;++cc) {
		getline(cin,s);
		memset( cache, -1, sizeof cache );
		printf("Case #%d: %04d\n", cc, doit(0,0) );
	}
}

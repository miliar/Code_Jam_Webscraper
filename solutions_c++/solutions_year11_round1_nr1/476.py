#include <fstream>
#include <string>
using namespace std;

typedef long long ll;

ifstream in;
string solve(){
	ll n;
	int pD, pG;
	
	in>>n>>pD>>pG;

	int div = 100;
	int pD1 = pD;
	for( int i = 2; i < 100; i++){
		while( div%i ==0 && pD1%i==0 ){
			div /= i;
			pD1  /= i;
		}
	}

	if( div<=n ){
		if( pD==0 || pG>0 ){
			if( pG!=100 )
				return "Possible";
			if( pG==100 && pD==100 )
				return "Possible";
		}
	}

	return "Broken";
}

int main(){
	in = ifstream ("A-small.in");
	ofstream out ("A-small.out");

	int T;
	in>>T;

	for( int i = 1; i <= T; i++)
		out<<"Case #"<<i<<": "<<solve()<<endl;
}

#include <iostream>
#include <vector>

using namespace std;

typedef struct chicken{
	int pos;
	int vec;
}C;

int N,K,B,T;
vector<C> cv;;
int pass,res;

bool ok( int s , int v ){

	return s/v < T || ( s%v == 0 && s/v == T );
}
int solve( void ){

	if ( ok( B - cv[cv.size()-1].pos , cv[cv.size()-1].vec ) ){

		cv.pop_back();
		return 0;
	}

	for( int i = cv.size() - 2 ; i >= 0 ; i -- )
		if( ok( B - cv[i].pos , cv[i].vec ) ){
			cv.erase( cv.begin() + i );		
			return cv.size()-i;
		}

	return -1;
}

int main( void ){

	//freopen( "B-small-attempt0.in" , "r" , stdin );
	//freopen( "B-small-attempt0.out" , "w" , stdout );

	freopen( "B-large.in" , "r" , stdin );
	freopen( "B-large.out" , "w" , stdout );

	int cases;

	cin>>cases;
	for( int testcases = 1 ; testcases <= cases ; testcases ++ ){

		cin>>N>>K>>B>>T;

		cv.clear();
		for( int i = 0 ; i < N ; i ++ ){
			C newC;		
			cin>>newC.pos;
			cv.push_back( newC );
		}
		for( int i = 0 ; i < N ; i ++ )
			cin>>cv[i].vec;

		pass = 0;
		res = 0;
		while( pass < K ){

			int tres = solve();
			if( tres >= 0 ){
				res += tres;
				pass++;
			}
			else{
				res = -1;
				break;
			}
		}

		if( res >= 0 )
			cout<<"Case #"<<testcases<<": "<<res<<endl;
		else
			cout<<"Case #"<<testcases<<": IMPOSSIBLE"<<endl;
	}

	return 0;
}
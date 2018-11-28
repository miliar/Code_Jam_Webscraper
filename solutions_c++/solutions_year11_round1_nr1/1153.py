#include<cstdio>
using namespace std;
int num_deal( int p, long long& up, long long& down ){
	up = (long long)p;
	down = 100;
	if( up % 2 == 0 ){ up /= 2; down /= 2;}
	if( up % 2 == 0 ){ up /= 2; down /= 2;}
	if( up % 5 == 0 ){ up /= 5; down /= 5;}
	if( up % 5 == 0 ){ up /= 5; down /= 5;}
	return p;
}
int main(){
	int T, _case = 0;
	scanf( "%d", &T );
	while( _case < T ){
		bool brok;
		long long N;
		int Pg, Pd;
		long long dup, ddown;
		scanf( "%lld %d %d", &N, &Pd, &Pg );
		num_deal( Pd, dup, ddown );
		if( ddown > N ){
			brok = true;
		}else{
			long long gup, gdown;
			long long dl, gl;
			num_deal( Pg, gup, gdown );
			dl = ddown - dup;
			gl = gdown - gup;
			if( gup == 0 ){
				if( dup == 0 ){
					brok = false;
				}else{
					brok = true;
				}
			}else{
				if( gl == 0 ){
					if( dl == 0 ){
						brok = false;
					}else{
						brok = true;
					}
				}else{
					brok = false;
				}
			}
		}
		printf( "Case #%d: %s\n", ++ _case, brok ? "Broken" : "Possible" );
	}
	return 0;
}

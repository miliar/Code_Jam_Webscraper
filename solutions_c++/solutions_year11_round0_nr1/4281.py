#include <iostream>
#define ABS( x ) (( (x) < 0 ) ? (-(x)) : (x))
using namespace std;
int main(){
	freopen( "input.txt","r",stdin );
	freopen( "output.txt","w",stdout );
	int T,res = 0;
	cin >> T;	
	char c;
	int mv,cp;
	
	for( int i = 0; i < T; i++ ){
		int o = 1;
		int b = 1;
		int om = 0;
		int bm = 0;
		cin >> mv;
		res = 0;
		while( mv-- ){
			cin >> c;
			cin >> cp;
			switch ( c){
				case 'O':					
					if( bm <  ABS( cp - o ) ){
						res += ABS( cp - o ) + 1 - bm;
						om += ABS( cp - o ) + 1 - bm;
					}else {
						res++;
						om++;
					}
					bm = 0;
					o = cp;					
					break;
				case 'B':
					if( om <  ABS( cp - b ) ){						
						res += ABS( cp - b ) + 1 - om;
						bm += ABS( cp - b ) + 1 - om;
					} else {
						res++;
						bm++;
					}
					om =  0;
					b = cp;		
					break;
			}
		}
		cout << "Case #"<< (i+1) <<": "<< res << endl;
	}

}
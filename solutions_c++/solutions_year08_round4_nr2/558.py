#include <iostream>
using namespace std ;
int main(){
	int tc ;
	cin >> tc ;
	for(int t = 1 ; t <= tc ; t++){
		int n , m , A ;
		cin >>  n>>m>>A ;
		int a , b , c , d ;
		int check = 0 ;
		for(int x1 = 0 ; x1 <= n ; x1++){
			for(int x2 = 0 ; x2 <= n ; x2++){
				for(int y1 = 0 ; y1 <= m ; y1++){
					for(int y2 = 0 ; y2 <= m ; y2++){
						int dd = x1*y2 - x2*y1 ;
						if(dd < 0 ) dd = -dd ;
						if(dd == A){
							a = x1 , b = y1 , c = x2 , d = y2 ;
							check = 1 ;
						}
					}
				}
			}
		}
		cout <<"Case #"<< t << ": " ;
		if(check)
			cout << "0 0 " << a << ' ' << b << ' ' << c << ' ' << d << endl ;
		else 
			cout << "IMPOSSIBLE" << endl ;
	}
}

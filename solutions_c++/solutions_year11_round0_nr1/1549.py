#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int T, N;
	char R;
	int P;
	
	cin >> T;
	for (int t=1; t<=T; t++){
		cin >> N;
		
		int ans = 0;
		int bp = 1, bt=0;
		int op = 1, ot=0;
		for (int i=0; i<N; i++){
			cin >> R >> P;
			
			if ( R == 'B' ){
				bt += ( P - bp < 0 ) ? bp - P : P - bp;
				bt = (bt > ot) ? bt+1 : ot+1;
				bp = P;
			}
			else{
				ot += ( P - op < 0 ) ? op - P : P - op;
				ot = ( bt > ot ) ? bt+1 : ot+1;
				op = P;
			}
		}
		
		cout << "Case #" << t << ": " << max(bt, ot) << endl;
	}
	
	return 0;
}

#include <iostream>

#define INF 0x3f3f3f3f

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	
	int test, t=1, n, aux, bits, min, sum;
	
	cin >> test;
	while (test--){
		bits = sum = 0;
		min = INF;
		
		cin >> n;
		for (int i=0; i<n; i++){
			cin >> aux;
			if (aux < min) min = aux;
			sum += aux;
			bits = (bits ^ aux);
		}
		
		if (bits) cout << "Case #" << t++ << ": NO\n";
		else cout << "Case #" << t++ << ": " << (sum - min) << "\n";
	}
	return 0;
}
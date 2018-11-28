#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main(void){
	int T;
	cin >> T;
	
	for(int t=1; t<=T; t++){
		int A, B;
		cin >> A >> B;
		
		double E = 1 + B+1; // give up
		double e = A + B + 1; // backspace all
		
		if(e < E) E = e;
		
		double P = 1;
		for(int a=1; a<=A; a++){
			// leave a not backspaced
			double p;
			cin >> p;
			
			P *= p;
			
			e = A-a + A-a + B-A + 1 + (B+1) * (1-P);
			
			if(e < E) E = e;
		}
		// finish typing is a=A (leave all not backspaced)
		
		cout << "Case #" << t << ": " << setprecision(8) << fixed << showpoint << E << endl;
	}
	
	return 0;
}

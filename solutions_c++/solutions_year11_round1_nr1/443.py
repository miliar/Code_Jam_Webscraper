#include <iostream>

using namespace std;

int main (int argc, char * const argv[]) {
	
	long long i,j,k,N,T,PD,PG;
	bool possible;
    
	cin >> T;
	
	for (i=0; i<T; i++) {
		cin >> N >> PD >> PG;
		possible = true;
		
		switch (PG) {
			case 0:
				if (PG!=PD) {
					possible = false;
				}
				break;
			case 100:
				if (PG!=PD) {
					possible = false;
				}
				break;
			default:
				j = 100;
				for (k=0; k<2; k++) {
					if (PD % 2 == 0) {
						j = j / 2;
						PD = PD /2;
					}
				}
				
				for (k=0; k<2; k++) {
					if (PD % 5 == 0) {
						j = j / 5;
						PD = PD /5;
					}
				}
				if (j > N) {
					possible = false;
				}
				break;
		}
		
		cout << "Case #" << i+1 <<": ";
		if (possible) {
			cout << "Possible" <<endl;
		} else {
			cout << "Broken" <<endl;
		}

	}
    return 0;
}

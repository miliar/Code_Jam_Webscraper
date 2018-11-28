/*#include <iostream>

using namespace std;

int main() {
	cout << "Start" << endl;
}
*/

#include <iostream>
#include <stdlib.h>
using namespace std;

int main ()
{
	int cases;
	cin >> cases;

	for ( int t = 1; t <= cases; t++) {
		int C;
		cin >> C;
		
		char* c1 = new char[C];
		char* c2 = new char[C];
		char* c3 = new char[C];
		for (int j=0;  j < C; j++ ) {
			cin >> c1[j] >> c2[j] >> c3[j];
		}
		


		int D;
		cin >> D;
		
		char* d1 = new char[D];
		char* d2 = new char[D];

		for (int j=0; j<D; j++) {
			cin >> d1[j] >> d2[j];
		}
		
		int I;
		cin >> I;
		
		char* response = new char[I];
		int ctr = 0;

		int* cstart = new int[C];
		for (int j=0; j<C; j++)
			cstart[j] = -10;


		char* cchar = new char[D];
		char* dchar = new char[D];
		
		int* dstart = new int[D];
		for (int j=0; j<D; j++) {
			dstart[j]=-10;
		}
		
		char input;

		for (int i = 0; i < I ; i++) {
				cin >> input;
				bool iter_complete = false;
			  	for (int j = 0 ; j < C ; j++) {
					if (input == c1[j] || input == c2[j]) {
						if ((cstart[j] == ctr-1) && (input != cchar[j] || c1[j] == c2[j])) {  // prev char was also a match
							response[cstart[j]] = c3[j];
							ctr = cstart[j]+1;
							for (int jd = 0 ; jd < D; jd++) {
								if ( dstart[jd] == ctr-1) {
									dstart[jd] = -10;
									for (int k = ctr-1; k >= 0; k--) {
										if (response[k] == d1[jd] || response[k] == d2[jd]) {
											dchar[jd] = response[k];
											dstart[jd] = k;
											break;
										}
									}
								}
							}
							for (int jc = 0 ; jc < C; jc++) {
								if ( cstart[jc] == ctr-1) {
									cstart[jc] = -10;
									for (int k = ctr-1; k > ctr-2; k--) {
										if (response[k] == c1[jc] || response[k] == c2[jc]) {
											cchar[jc] = response[k];
											cstart[jc] = k;
											break;
										}
									}
								}
								// cout << " new cstarts " << cstart[jc] << endl;
							}
							cstart[j] = -10;
							input = c3[j];
							j = -1;
							/*cout << "itemp response [";
							for (int i = 0; i < ctr-1; i++) {
								cout << response[i] << ", " ;
							}	
							cout << response[ctr-1] << "]" << endl;
							*/
							iter_complete = true;	
						} else {
							cchar[j] = input;
							cstart[j] = ctr;
						}
					}
				} 
				for ( int j = 0; j<D & !iter_complete; j++ ) {
					if (input == d1[j] || input == d2[j]) {
						if ((dstart[j] >= 0) && (input != dchar[j])) { // match!
							ctr = 0;
							for (int jc = 0; jc < C; jc++) {
								cstart[j] = -10;
							}
							for ( int jd = 0; jd < D; jd++) {
								dstart[jd] = -10;
							}
							iter_complete = true;
						} else {
							dchar[j] = input;
							dstart[j] = ctr;
						}
					}
				} 
				if( !iter_complete){
					response[ctr] = input;
					ctr++;
				}
				/*cout << "response [";
				for (int i = 0; i < ctr-1; i++) {
					cout << response[i] << ", " ;
				}	
				cout << response[ctr-1] << "]" << endl;
				cout << cstart[0] << " c:d " << dstart[0] << endl;		
				*/
			} // end of input
			
		cout << "Case #" << t << ": [";
		for (int i = 0; i < ctr-1; i++) {
			cout << response[i] << ", " ;
		}
		if(ctr >= 1) {
			cout << response[ctr-1] << "]" << endl;
		} else {
			cout << "]" << endl;
		}

	} // end of all cases


}

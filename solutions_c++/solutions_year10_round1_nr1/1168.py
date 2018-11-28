//-------------------------------------------------------------------------------------------
//  TEMPLATE.CPP
//
//-------------------------------------------------------------------------------------------


//-------------------------------------------------------------------------------------------

//#define INPUT_FILE "x.in"
//#define OUTPUT_FILE "x.out"

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;

//-------------------------------------------------------------------------------------------
// GLOBALS 
//
//ifstream in(INPUT_FILE);
//ofstream out(INPUT_FILE);

int G_T, 
    G_N,
	G_K;
char G_IB[50][50],	
     G_FB[50][50];

//-------------------------------------------------------------------------------------------
// TEST Prototypes
//


//-------------------------------------------------------------------------------------------
// FOO 
//
bool hor(char c, int K){
	int kk,ll,mm;
	bool win;
	
	// search for 'c'
	for (kk = 0; kk < G_N; kk++)
		for(ll = 0; ll <= (G_N-K); ll++){
			
			if (G_FB[ll][kk] == c){
				mm = 1;
				win = true;
				while (mm < K && win){
					if (G_FB[ll+mm][kk] != c)
						win = false;
					
					mm++;
				}
				if (win)
					return true;
			}	
							
		}
		
	return false;
}


bool ver(char c, int K){
// going down...
	int kk,ll,mm;
	bool win;
	
	// search for 'c'
	for (kk = 0; kk <= (G_N-K); kk++)
		for(ll = 0; ll < G_N; ll++){
			
			if (G_FB[ll][kk] == c){
				mm = 1;
				win = true;
				while (mm < K && win){
					if (G_FB[ll][kk+mm] != c)
						win = false;
					
					mm++;
				}
				if (win)
					return true;
			}	
							
		}
		
	return false;
}


bool diag1(char c, int K){
// going down...
	int kk,ll,mm;
	bool win;
	
	// search for 'c'
	for (kk = 0; kk <= (G_N-K); kk++)
		for(ll = 0; ll <= (G_N-K); ll++){
			
			if (G_FB[ll][kk] == c){
				mm = 1;
				win = true;
				while (mm < K && win){
					if (G_FB[ll+mm][kk+mm] != c)
						win = false;
					
					mm++;
				}
				if (win)
					return true;
			}	
							
		}
		
	return false;
}

bool diag2(char c, int K){
// going down...
	int kk,ll,mm;
	bool win;
	
	// search for 'c'
	for (kk = 0; kk <= (G_N-K); kk++)  // ok
		for(ll = (K-1); ll < G_N; ll++){
			
			if (G_FB[ll][kk] == c){
				mm = 1;
				win = true;
				while (mm < K && win){
					if (G_FB[ll-mm][kk+mm] != c)
						win = false;
					
					mm++;
				}
				if (win)
					return true;
			}	
							
		}
		
	return false;
}


// ################################################################################
// ################################################################################
// ################################################################################
// ################################################################################

int main(){
	int i,k,l,m;
	int cc, rr;
	unsigned long ns;
	bool wblue, wred;

	cerr << "Hello Rotate!!" << endl;
	
	cin >> G_T;
	cerr << "No. of cases = " << G_T << endl;

	for(i = 0; i < G_T; i++){
		cin >> G_N >> G_K;
		cerr << "<" << G_N << "," << G_K <<  ">" << endl;
				


		// fill input array
		for (k = 0; k < 50; k++)
			for (l = 0; l < 50; l++)
				 G_IB[l][k] = '.';

		// fill final array
		for (k = 0; k < 50; k++)
			for (l = 0; l < 50; l++)
				 G_FB[l][k] = '.';


		// read array
		for (k = 0; k < G_N; k++)
			for (l = 0; l < G_N; l++)
				cin >> G_IB[l][k];
						
		// build rotated array.
		cerr << "rot" << endl;
		cc = 0;
		for (k = (G_N-1); k >= 0; k--){
	 		rr = G_N-1;
			for (l = (G_N-1); l >= 0; l--){
				if ( G_IB[l][k] != '.'){
					G_FB[cc][rr] = G_IB[l][k];
					rr--;
				}
				//cerr << G_IB[l][k];}
			}
			cc++;
		}
		//cerr << endl;
		
		//print input array array
		cerr << "input board" << endl;
		for (k = 0; k < G_N; k++){
			for (l = 0; l < G_N; l++){
				cerr << G_IB[l][k];
			}
			cerr << endl;
		}
		cerr << endl;
		
		//print rotated array
		cerr << "rotated board" << endl;
		for (k = 0; k < G_N; k++){
			for (l = 0; l < G_N; l++){
				cerr << G_FB[l][k];
			}
			cerr << endl;
		}
		cerr << endl;
		
		// search blue
		
		// search red
		
		wblue = hor('B', G_K) || ver('B', G_K) || diag1('B', G_K) || diag2('B', G_K);
		cerr << "Blue Win? " << wblue << endl;
		
		wred = hor('R', G_K) || ver('R', G_K) || diag1('R', G_K) || diag2('R', G_K);
		cerr << "Red Win? " << wred << endl;
		
		cout << "Case #" << (i+1) << ": ";
		if (wblue && wred) cout << "Both";
		else if (wblue) cout << "Blue";
		else if (wred) cout << "Red";
		else cout << "Neither";
		cout << endl;
	}

	return 0;
}

// ################################################################################
// ################################################################################
// ################################################################################
// ################################################################################


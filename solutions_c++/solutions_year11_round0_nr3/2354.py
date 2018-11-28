//-------------------------------------------------------------------------------------------
//  PEGGAME.CPP
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
int T;
int N;
int Candy[1000];
int Sean[1000];
int PatLeft[1000];
int PatRight[1000];

//-------------------------------------------------------------------------------------------
// TEST Prototypes
//


//-------------------------------------------------------------------------------------------
// FOO 
//

//-------------------------------------------------------------------------------------------
// FOO 
//
int max(int a, int b)
{
	return a > b ? a : b;
}
//-------------------------------------------------------------------------------------------
// FOO
//
void cerrArray(int *A){
	int k;
	
	cerr << "[ ";
	for (k = 0; k < N; k++){
		cerr << A[k];
		if (k+1 < N) cerr << ", ";   
	}
	cerr << " ]" << endl;
}


//-------------------------------------------------------------------------------------------
// FOO
//


// ################################################################################
// ################################################################################
// ################################################################################
// ################################################################################

int main(){
	int i,k,l,m;
	string ss;
	
	cerr << "Hello Candy!!" << endl;

	cin >> T;
	cerr << "No. of cases = " << T << endl;
	
	for(i = 0; i < T; i++){
						//** Read Case's input
		cin >> N;
		for(k = 0; k < N; k++){
			cin >> Candy[k];		
		}
		cerrArray(Candy);
		std::sort( Candy, Candy + N );
		cerrArray(Candy);
		
						//** Populate extra data arrays
		Sean[0] = Candy[0];
		PatLeft[0] = Candy[0];
		for(k = 1; k < N; k++){
			Sean[k] = Sean[k-1] + Candy[k];
			PatLeft[k] = PatLeft[k-1] ^ Candy[k];
		}
		PatRight[N-1] = Candy[N-1];
		for(k = N-2; k >= 0; k--){
			PatRight[k] = PatRight[k+1] ^ Candy[k];
		}
		
		cerrArray(Sean);
		cerrArray(PatLeft);
		cerrArray(PatRight);
		
		
						//** Find Solution in Patrick's sums
		int alpha = 0;
		int l,r,beta;
		for(k = 0; k < N-1; k++){
			if (PatLeft[k] == PatRight[k+1]){
				l = Sean[k];
				r = Sean[N-1] - l; 
				beta = max(l,r);
				alpha = max(alpha,beta);
			} 
		}

		cout << "Case #" << (i+1) << ": ";
		if (alpha) { cout << alpha << endl; }
		else { cout << "NO" << endl; }
		

	} //Case

	return 0;
}

/*
int bak(){

		//---- Clear State
		for(k = 0; k < 26; k++)
			for(l = 0; l < 26; l++){
				comb[k][l] = ' ';
				opps[k][l] = false;
			}
		for(k = 0; k < 110; k++)
			manalist[k] = ' ';
		manak = 0;
		for(k = 0; k < 26; k++)
			manaset[k] = false;
		//----
		
		cin >> G_C;
		for(k = 0; k < G_C; k++){
			cin >> ss;
			p = ord(ss[0]);
			q = ord(ss[1]);
			comb[p][q] = ss[2];
			comb[q][p] = ss[2];		
		}
		cin >> G_D;
		for(k = 0; k < G_D; k++){
			cin >> ss;
			p = ord(ss[0]);
			q = ord(ss[1]);
			opps[p][q] = true;
			opps[q][p] = true;
			//cerr << ss << endl;
		}
		cin >> G_N;
		cin >> ss;
				
		cerr << "<" << G_C << "," << G_D << "," << G_N << "> ";
		cerr << ss << endl;
				
		// PROCESS
		for(k = 0; k < G_N; k++){
			e = ss[k];
			cerr << "*** " << e << endl;

			//push e
			manalist[manak] = e; manak++; manaset[ord(e)] = true;
			
			errmanaprint();
			errmanasetprint();

			//combine
			p = ord(e);
			q = - 1;
			if ( (manak - 2) >= 0 ) q = ord(manalist[manak-2]);	 			
			//cerr << p << "," << q << endl;
			
			if (q >= 0)
			{
			if ( comb[p][q] != ' ' ){
				//pop twice
				manaset[ord(manalist[manak-1])] = false;
				manaset[ord(manalist[manak-2])] = false;
				manak = manak -2;

				//push new element
				manalist[manak] = comb[p][q]; manak++; manaset[ord(comb[p][q])] = true;
			}
			// eliminate
			else {
					for (l = 0; l < 26; l++){
						if (opps[p][l] && manaset[l] ) {
							//clear list
							//cerr << "-!"<< p << "," << l << endl;
							manak = 0;
							for(m = 0; m < 26; m++)
								manaset[m] = false;
						}
					}
			}
			}

			//print manalist
			errmanaprint();
			errmanasetprint();
		} // of PROCESS
		
		
		manaprint();
		
}
*/
/*
void dummy(){
	for(i = 0; i < G_T; i++){
		cin >> G_R >> G_k >> G_N;
		cerr << "<" << G_R << "," << G_k << "," << G_N << ">" << endl;
		
		for(k = 0; k < G_N; k++){
			cin >> G_gi[k];
		}
		euros = 0;
		first = 0;
		table();
		
		for(k = 0; k < G_N; k++){
			cerr << "  " << G_gi[k];	cerr << ", "; } cerr << endl;
		for(k = 0; k < G_N; k++){
			cerr << "  " << G_load[k];	cerr << ", "; } cerr << endl;
		for(k = 0; k < G_N; k++){
			cerr << "  " << G_nextg[k];	cerr << ", "; } cerr << endl;
			
		for(l = 0; l < G_R; l++){
			euros += G_load[first];
			first = G_nextg[first];  
		}
		
		cout << "Case #" << (i+1) << ": " << euros << endl;
	}

	//euros = 100000000;
	//euros *= euros;
	//cout << "* " << euros << endl;

	return 0;
}
*/

// ################################################################################
// ################################################################################
// ################################################################################
// ################################################################################


// --------------------------------

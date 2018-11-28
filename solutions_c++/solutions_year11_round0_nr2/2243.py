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
int G_T;
int G_C, G_D, G_N;
char comb[26][26];
bool opps[26][26];

string manalist;

//-------------------------------------------------------------------------------------------
// TEST Prototypes
//


//-------------------------------------------------------------------------------------------
// FOO 
//
int ord(char x){
	return (int)x - 'A';
}


//-------------------------------------------------------------------------------------------
// FOO
//
void manaprint(){
	int k, n;

	n = manalist.size();
	cout << "[";
	for (k = 0; k < n; k++){
		cout << manalist[k];
		if (k+1 < n) cout << ", ";   
	}
	cout << "]" << endl;
}

//-------------------------------------------------------------------------------------------
// FOO
//
void errmanaprint(){
	int k, n;
	
	n = manalist.size();
	cerr << "[";
	for (k = 0; k < n; k++){
		cerr << manalist[k];
		if (k+1 < n) cerr << ", ";   
	}
	cerr << "]" << endl;
}





// ################################################################################
// ################################################################################
// ################################################################################
// ################################################################################

int main(){
	int i,k,l,m;
	int p,q;
	char e;
	string ss;

	cerr << "Hello Magicka B!!" << endl;
	
	cin >> G_T;
	cerr << "No. of cases = " << G_T << endl;
	
	for(i = 0; i < G_T; i++){
		
		//---- Clear State
		for(k = 0; k < 26; k++)
			for(l = 0; l < 26; l++){
				comb[k][l] = ' ';
				opps[k][l] = false;
			}
			
		manalist.clear();
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
			manalist.append(1,e);
			
			errmanaprint();

			//combine
			m = manalist.size();
			if ( m > 1 )
			{
			p = ord(manalist[m-1]);
			q = ord(manalist[m-2]);
			if ( comb[p][q] != ' ' ){
				//pop twice
				manalist.erase(m-2);
				//push new element
				manalist.append(1,comb[p][q]);
			}
			// eliminate
			else {
				p = ord(e);
				char x;
				for (l = 0; l < 26; l++){
					if (opps[p][l]) {
						x = (char)(l + 'A');
						cerr << "x= " << x;
						int loc1 = manalist.find(x, 0);
						cerr << " @= " << loc1 << endl;
						if (loc1 >= 0){
							//clear list
							manalist.clear();
						}
					}
				}
			}
			}
			//print manalist
			errmanaprint();
		} // of PROCESS
		
		cout << "Case #" << (i+1) << ": ";
		manaprint();
		
	}

	return 0;
}

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

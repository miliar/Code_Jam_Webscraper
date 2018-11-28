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

unsigned long G_T,
		      G_R,
	          G_k,
	 		  G_N;
	
	
unsigned long G_gi[1000];
unsigned long G_load[1000];
unsigned long G_nextg[1000];


//-------------------------------------------------------------------------------------------
// TEST Prototypes
//
void test_inc();


//-------------------------------------------------------------------------------------------
// FOO inc
//
int inc(int i){
	i++;
	if (i == G_N) return 0;
	return i;
}

//-------------------------------------------------------------------------------------------
// FOO table
//
void table(){
	for (int k = 0; k < G_N; k++){
		G_load[k] = G_gi[k];
		G_nextg[k] = inc(k);
		while ( (G_load[k] + G_gi[ G_nextg[k] ] <= G_k) &&
		         G_nextg[k] != k ){
			G_load[k] += G_gi[ G_nextg[k] ];
			G_nextg[k] = inc( G_nextg[k] );
		}
	}
}

// ################################################################################
// ################################################################################
// ################################################################################
// ################################################################################

int main(){
	int i,k,l,m;
	unsigned long long euros;
	unsigned long first;

	cerr << "Hello World!!" << endl;
	
	cin >> G_T;
	cerr << "No. of cases = " << G_T << endl;

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

// ################################################################################
// ################################################################################
// ################################################################################
// ################################################################################


// --------------------------------
void test_inc(){
	cout << "---" << endl;
	int i = G_N - 4;
	for (int k = 0; k < 10; k++){
		cout << i << "- ";
		i = inc(i);
	}
	cout << endl;
}

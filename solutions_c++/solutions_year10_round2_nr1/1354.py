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
	G_M;

vector < string > G_fs;

//-------------------------------------------------------------------------------------------
// TEST Prototypes
//


//-------------------------------------------------------------------------------------------
// FOO 
//
string bestmatch(string ss){
	int kk;
	int aix = 0;
	int asc = 0;
	int bsc = 0;
		
	for(kk = 0; kk < G_fs.size(); kk++){
		
		bsc = 0;
		while ( bsc < ss.size() &&
				bsc < ss.size() &&
				ss[bsc] == (G_fs[kk])[bsc]){
			bsc++;
		}
		
		if (bsc > asc){
			asc = bsc;
			aix = kk;
		}		
	} 
	return G_fs[aix];
}

int ccost(string ss, string bm){
	int xi;
	int s;

	xi = 0;
	while ( xi < ss.size() &&
			xi < bm.size() &&
			ss[xi] == bm[xi]){
		xi++;
	}
		
	//cerr << "xi == " << xi << endl;
	
    if (xi == ss.size() && xi >= bm.size())  // path already created
		return 0;
		
    if (xi == ss.size() && bm[xi] == '/')  // path already created
		return 0;
	
	
	
	//count slashes 
	s = 0;
	if ( xi < ss.size() && ss[xi] == '/') xi++;  // skip head slash??
	while (xi < ss.size()){
		if (ss[xi] == '/')
			s++;
		xi++;
	}
	
	return s+1;
}


// ################################################################################
// ################################################################################
// ################################################################################
// ################################################################################

int main(){
	int i,k,l,m;
	int sol;
	string ss;
	string bestm; 
	int cost;

	cerr << "Hello Fix-It!!" << endl;
	
	cin >> G_T;
	cerr << "No. of cases = " << G_T << endl;

	for(i = 0; i < G_T; i++){
		cin >> G_N >> G_M;
		cerr << "<" << G_N << "," << G_M <<  ">" << endl;
		
		G_fs.clear();
		sol = 0;
				
		// fill input array
		G_fs.push_back("/");
		for (k = 0; k < G_N; k++){
			cin >> ss;
			G_fs.push_back(ss);
		}

		cerr << "-- Current" << endl;
		// out
		for (k = 0; k < G_fs.size(); k++){
			cerr << "-" << G_fs[k] << endl;
		}

		// process new
		for (k = 0; k < G_M; k++){
			cin >> ss;
			bestm = bestmatch(ss);
			cerr << "best of " << endl << ss << " is " << endl << bestm << endl;
			cost =  ccost(ss,bestm);
			cerr << "create cost " << cost << endl;
			sol += cost;
			G_fs.push_back(ss);
		}

		//cerr << " ? " << G_fs[1][100] << endl;

		cerr << "Case #" << (i+1) << ": ";
		cerr << sol;
		cerr << endl;
		cout << "Case #" << (i+1) << ": ";
		cout << sol;
		cout << endl;
	}

	return 0;
}

// ################################################################################
// ################################################################################
// ################################################################################
// ################################################################################


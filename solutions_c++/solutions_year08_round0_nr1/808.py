/*
 * Competition Template
 * 
 * All main libraries are included, 
 * Typedefs to increase readability
 * #define to deal with STL
 */
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <climits>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
using namespace std;

/* CONSTANTS ======================================================================
 */
#define TRUE		 1
#define FALSE		 0
#define PI           3.14159265358979
#define PI2          1.57079632679489        
#define SQRT2        1.41421356237309
#define ISQRT2       0.70710678118654
#define INF          INT_MAX
#define BigINF       LLONG_MAX

/* TYPES  =========================================================================
 */
typedef vector < int >          IntVector;
typedef vector < IntVector >    IntMatrix;
typedef long long               BigInt;
typedef vector < BigInt >       BigIntVector;
typedef vector < BigIntVector > BigIntMatrix;
typedef double                  Real;
typedef vector < Real >         RealVector;
typedef vector < RealVector >   RealMatrix;
typedef vector < string >       StringVector;
typedef istringstream        ISS;  

/* MACROS  ========================================================================
 */
// Readibility Macros ----------------------------------------
#define FORC(i,n)   for (int i=0; i<n; ++i)
#define FORTO(counter,begin,end)   for (int counter=begin; counter<=end; ++counter)
#define FORDOWNTO(counter,begin,end)   for (int counter=begin; counter>=end; --counter)

// STL Macros  -----------------------------------------------
// Let X be a container
#define ADD push_back
#define JAM push_front
#define REM pop_back
#define ALL(X)   X.begin(),X.end()
#define FORALL(iter, X)   for(__typeof(X.begin()) iter = X.begin(); iter != X.end(); ++iter)
#define FOREACH(iter, X, cond)   FORALL(iter, X) if (cond)
#define SIZE(x)   (int)x.size()
#define PRINTV(X)   cout << "< "; FORALL(elem,X) cout << (*elem) << ", "; cout << ">" << endl;  // assumes 'elem' is printable
//#define PRINTM(X)   cout << "[ "; FORALL(row,X) PRINTV(row) << ", "; cout << "]" << endl;      // assumes 'row' is a vector of printables

// Maps  -----------------------------------------------
template < class K, class V > bool MAPFIND( map < K, V > themap, K key, V &value) {
	__typeof(themap.begin()) iter = themap.find(key);
	if (iter != themap.end()){ value = (*iter).second; return TRUE; }
    return FALSE; 
}


// Printing Macros -----------------------------------------------

/* ideas for queue */


// ============================================================================
// ============================================================================
// ============================================================================
// ============================================================================
// ============================================================================

// TYPES ------------------------------------

typedef struct state{
	int loc;
	int w;
};

class Prioritize {
public:
     int operator() ( const state &s1,
                      const state &s2 ) {
         return s1.loc < s2.loc;
     }
};

// GLOBALS ------------------------------------

int n_se;
int n_qs;

map<string, int> se;
IntVector qs;

// ----------------------------------------------------
int runquery(int loc, int eng){
	int k;
	
	for(k = loc; k < qs.size(); k++){
		if(qs[k] == eng){
			return k;
		}
	}
	return k;
}

// ----------------------------------------------------
int best_first (){
	
	vector<state> fs;
	state s;
	
	int alpha = 0;
	
	FORC(k,n_se){
		s.loc = runquery(0,k);
		s.w = 0;
		fs.ADD(s);
	}
	
	//FORALL(item, fs)
	//	cout << "%% -> " << (*item).loc << endl;
	
	priority_queue < state, vector<state>, Prioritize > pq( ALL(fs) );
	
	bool done = false;
	while(!pq.empty() && !done){
		s = pq.top(); pq.pop();
		/*if (s.loc > alpha){
			alpha = s.loc;
			cout << "%% best loc = " << alpha << endl;
		}*/
		if (s.loc == qs.size()){
			done = true;
			return s.w;
		}
		else{
			FORC(k,n_se){
				if(k != qs[s.loc]){
					state dmy;
					dmy.loc = runquery(s.loc,k); 
					dmy.w = s.w + 1;
					pq.push(dmy);
				}
			}
		}		
	} // while
	if (!done) cout << "%% PANIC at best_first" << endl;
	return 666;
	/*
	
	s.loc = -1;
	s.w = 5;
	fs.ADD(s);
	
	s.loc = -2;
	s.w = 10;
	fs.ADD(s);
	
	while ( !pq. empty() ) { 
         cout << "%% " << pq.top().loc << "@" << pq.top().w << endl;
         pq.pop();
     }
	*/
}


// ----------------------------------------------------
// ----------------------------------------------------
// ----------------------------------------------------
int main(){

	int nnn;
	int best;
	
	string s;

	//cout << "%% Hello Universe" << endl;
	
	cin >> nnn;
	//cout << "%% "<< nnn << " cases" << endl; 
	
	FORTO(casen, 1, nnn){
		//cout << "%% Case #" << casen << endl;

		cin >> n_se;
		//cout << "%% "<< n_se << " engines" << endl; 

		getline(cin,s); // read dummy
		FORC(k,n_se){
			getline(cin,s);
			//cout << "%% s = "<< s << endl; 
			se[s] = k;
		}

		//FORALL(item, se){
		//	cout << "%% < " << (*item).first << ", " << (*item).second << "> ";
		//}
		//cout << endl;

		cin >> n_qs;
		//cout << "%% "<< n_qs << " queries" << endl;

		getline(cin,s); // read dummy
		FORC(k,n_qs){
			getline(cin,s);
			qs.ADD(se[s]);
		}	
		//cout << "%% "; PRINTV(qs)

		//cout << "%% rq(0,0) = "<< runquery(0,0) << endl;
		//cout << "%% rq(0,3) = "<< runquery(0,3) << endl;	

		best = 9999;
		best = best_first();
		cout << "Case #" << casen << ": " << best << endl;


		se.clear();
		qs.clear();		
	}
	
	
	//cout << "%% Done!" << endl;

    return 0;
}

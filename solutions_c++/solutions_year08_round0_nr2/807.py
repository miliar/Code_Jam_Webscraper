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

#define CityA 0
#define CityB 1
#define Tdep  0
#define Ttu   1
#define thecity(I) (( I == 0 ) ? 'A' : 'B') 

#define Time2Int(h,m)  (((h)*60) + (m))
#define IntHor(I)      ( (I)/60 )
#define IntMin(I)      ( (I)%60 )


typedef struct event{
	int tim;
	int typ;
	int cty;
};

class Prioritize {
public:
     int operator() ( const event &a,
                      const event &b ) {
         if (a.tim != b.tim){
				return a.tim > b.tim;
		 }
		else return a.typ < b.typ;
     }
};


// GLOBALS ------------------------------------
int turnaround;
int na;
int nb;

int need[2];
int at[2];

vector<event> evv;

// ----------------------------------------------------
void Simulate()
{
	event ee;
	
	priority_queue < event, vector<event>, Prioritize > pq( ALL(evv) );
	
	while(!pq.empty()){
		ee = pq.top(); pq.pop();
		if (ee.typ == Tdep){
			//cout << "%% Train Departs from " << thecity(ee.cty) << " at " 
			//     << IntHor(ee.tim) << ":" << IntMin(ee.tim) << endl;
			if (at[ee.cty] > 0)  at[ee.cty]--;
			else                 need[ee.cty]++;
		}
		else{  // turnaround
			//cout << "%% Train Available at " << thecity(ee.cty) << " at " 
			//     << IntHor(ee.tim) << ":" << IntMin(ee.tim) << endl;
			at[ee.cty]++;
		}		
	} // while
}



// ----------------------------------------------------
// ----------------------------------------------------
// ----------------------------------------------------
int main(){

	int nnn;

	//cout << "%% Trains Universe" << endl;
	
	cin >> nnn;
	//cout << "%% "<< nnn << " cases" << endl; 
	
	int casen = 1;
	FORTO(casen, 1, nnn){
		//cout << "%% Case #" << casen << endl;

		at[0] = at[1] = need[0] = need[1] = 0;
		// read input
		cin >> turnaround;
		cin >> na;
		cin >> nb;

		//cout << "%% " << turnaround << ", " << na << ", " << nb << endl;

		int h1, h2, m1, m2;
		char ccc;
		event e1, e2;
		FORC(k,na){
			//cout << "%% to A" << endl;
			cin >> h1 >> ccc >> m1 >> h2 >> ccc >> m2;
			//cout << "%% " << h1 << "-" << m1 << " to " << h2 << "-" << m2 << endl;
			
			e1.tim = Time2Int(h1,m1); e1.typ = Tdep; e1.cty = CityA;
			evv.ADD(e1);
			e2.tim = Time2Int(h2,m2+turnaround); e2.typ = Ttu; e2.cty = CityB;
			evv.ADD(e2);
			
		}
		FORC(k,nb){
			//cout << "%% to B" << endl;
			cin >> h1 >> ccc >> m1 >> h2 >> ccc >> m2;
			//cout << "%% " << h1 << "-" << m1 << " to " << h2 << "-" << m2 << endl;
			e1.tim = Time2Int(h1,m1); e1.typ = Tdep; e1.cty = CityB;
			evv.ADD(e1);
			e2.tim = Time2Int(h2,m2+turnaround); e2.typ = Ttu; e2.cty = CityA;
			evv.ADD(e2);
		}
		
		Simulate();
		
		cout << "Case #" << casen << ": " << need[0] << " " << need[1] << endl;
		
		//-- clear vars;
		evv.clear();
	}
	
	
	//cout << "%% Done!" << endl;

    return 0;
}

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

/* ******** CONSTANTS
 */
#define TRUE		 1
#define FALSE		 0
#define PI           3.14159265358979
#define PI2          1.57079632679489        
#define SQRT2        1.41421356237309
#define ISQRT2       0.70710678118654
#define INF          INT_MAX
#define BigINF       LLONG_MAX

/* ******** TYPES
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

/* ******** MACROS
 */
// --- Statement Macros
#define FORC(i,n)   for (int i=0; i<n; ++i)
#define FORTO(counter,begin,end)   for (int counter=begin; counter<=end; ++counter)
#define FORDOWNTO(counter,begin,end)   for (int counter=begin; counter>=end; --counter)

// --- STL Macros  
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


/* ******** Data Structures
 */
template < class K, class V > bool MAPFIND( map < K, V > themap, K key, V &value) {
	__typeof(themap.begin()) iter = themap.find(key);
	if (iter != themap.end()){ value = (*iter).second; return TRUE; }
    return FALSE; 
}
/* ideas for queue */


bool cmp( int a, int b ) {
   return a > b;
 }


// ============================================================================
// ============================================================================
// ============================================================================
// ============================================================================
// ============================================================================

IntVector a, b;

int main(){

	int nnn;
	int lll, xx;

	cerr << "%% Vectors" << endl;
	
	cin >> nnn;
	//cout << "%% "<< nnn << " cases" << endl; 
	
	
	int casen = 1;
	FORTO(casen, 1, nnn){
		cout << "%% Case #" << casen << endl;
		cin >> lll;
		
		FORC(k,lll){ 
			cin >> xx;
			a.ADD(xx);
		}
		FORC(k,lll){ 
			cin >> xx;
			b.ADD(xx);
		}
		
		sort(ALL(a));
		sort(ALL(b), cmp);
		
		cout << "%%"; PRINTV(a);
		cout << "%%"; PRINTV(b);
		
		BigInt res = 0;
		FORC(k,lll){
			res += (a[k]*b[k]);
		}
		
		cout << "Case #" << casen << ": " << res << endl;
		
		a.clear();
		b.clear();
	}

    return 0;
}

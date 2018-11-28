/* Power := ( ), ON := +, OFF := -
 *    1  2  3  4  ...
 * 0: -  -  -  -  ...
 * 1:(+) -  -  -  ... first time snapper 1 is ON with power
 * 2: -  +  -  -  ... == state 0 for snapper 1
 * 3:(+)(+) -  -  ... first time snapper 2 is ON with power
 * 4: -  -  +  -  ... == state 0 for snapper 1,2
 * 5:(+) -  +  -  ...
 * 6: -  +  +  -  ...
 * 7:(+)(+)(+) -  ... first time snapper 3 is ON with power
 * 8: -  -  -  +  ... == state 0 for snapper 1,2,3
 * so you can see the pattern:
 * first time that snapper i is on is (1<<i)-1
 * and it repeats every (1<<i)'th step 
 * so you can see the first N bits of K have to be set to ON
 * to achive a burning light                                   */


#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>


 
using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

int main(){
	int tcam;
	cin >> tcam;
	FOR(tnr,1,tcam+1){
		int N; int K;
		cin >> N >> K;
		int bits = (1<<N)-1;
		if((bits&K)==bits)cout << "Case #" << tnr << ": ON\n";
		else cout << "Case #" << tnr << ": OFF\n";
	}
	return 0;
}

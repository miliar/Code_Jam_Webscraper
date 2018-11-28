#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <algorithm>	// require sort next_permutation count __gcd reverse etc.
#include <cstdlib>	// require abs exit
#include <cstdio>	// require scanf printf
#include <functional>
#include <numeric>	// require accumulate
#include <cmath>
#include <climits>
#include <limits>
#include <cfloat>
#include <iomanip>	// require setw
#include <sstream>	// require stringstream 
#include <cstring>	// require memset
#include <cctype>	// require tolower, toupper
#include <fstream>	// require freopen
#include <ctime>
#define rep(i,n) for(int i=0;i<(n);i++)
#define ALL(A) A.begin(), A.end()

using namespace std;

typedef long long ll;
typedef pair<int, int> P;

int main()
{
//	cut here before submit 
//	freopen ("testcase.speaking_in_tongues", "r", stdin );
	freopen ("A-small-attempt0.in", "r", stdin );
	int cnt;
	string s = "";
	getline (cin, s );
	stringstream sn (s );
	sn >> cnt;
	map<char,char> t;
	t['a']= 'y', t['b']= 'h', t['c']= 'e', t['d']= 's', t['e']= 'o', t['f']= 'c';
	t['g']= 'v', t['h']= 'x', t['i']= 'd', t['j']= 'u', t['k']= 'i', t['l']= 'g';
	t['m']= 'l', t['n']= 'b', t['o']= 'k', t['p']= 'r', t['q']= 'z', t['r']= 't';
	t['s']= 'n', t['t']= 'w', t['u']= 'j', t['v']= 'p', t['w']= 'f', t['x']= 'm';
	t['y']= 'a', t['z']= 'q';
	
	for (int Case = 1; Case <= cnt; Case++ ){
		string g = "";
		getline (cin, g );
		string res = "";
		rep (i, g.length() ){
			if (g[i] == ' ' ){
				res += g[i];
			}else{
				res += t[g[i]];
			} // end if
		} // end rep
		cout << "Case #" << Case << ": " << res << endl;
	} // end loop

//	cout << res << endl;	
		
	return 0;
}

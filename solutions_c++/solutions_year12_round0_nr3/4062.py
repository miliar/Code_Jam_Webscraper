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

string itos (int n )
{
	stringstream ss;
	ss << n;

	return ss.str();
}
int stoi (string s )
{
	stringstream ss (s );
	int res;
	ss >> res;

	return res;
}

int main()
{
//	cut here before submit 
//	freopen ("testcase.recycled_numbers", "r", stdin );
	freopen ("C-small-attempt0.in", "r", stdin );
	set<int> ri[1001];
//	rep (i, 1001 ) ri.clear();

	for (int i = 1; i <= 1000; i++ ){
		string si = itos (i );
		for (int j = si.length()-1, k = 1; j > 0; j--, k++ ){ 
			string s = si.substr (0, j );
			string t = si.substr (j, k );
			string u = t + s;
			int nu = stoi (u );
			if (nu <= i ) continue;
			ri[i].insert (nu );
//			cout << si << ": " << t << ' ' << s << endl;
		} // end for
	} // end rep
/*
	for (int i = 1; i <= 1000; i++ ){
		set<int>::iterator it = ri[i].begin();
		cout << i << ": ";
		for (; it != ri[i].end(); it++ ){
			cout << (*it) << ' ';
		} // end for
		cout << endl;
	} // end for
*/
	int t;
	cin >> t;
	for (int Case = 1; Case <= t; Case++ ){

		int A, B;
		cin >> A >> B;
		int res = 0;
		for (int i = A; i <= B; i++ ){
			if (ri[i].empty() ) continue;				
			set<int>::iterator it = ri[i].begin();
			for (; it != ri[i].end(); it++ ){
				if ((*it) <= B ) res++;
			} // end for
		} // end for
		cout << "Case #" << Case << ": " << res << endl;
	} // end loop

//	cout << res << endl;	
		
	return 0;
}

#include <algorithm>
#include <bitset>
#include <cmath>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
 
using namespace std ;

#define all(n) n.begin(), n.end()
#define fb(i, n) fv (i, 0, n)
#define fe(i, n) fb (i, n.size())
#define fi(i, n) for (typeof (n.begin()) i = n.begin() ; i != n.end() ; i++)
#define fv(i, s, n) for ( int i = s ; i < n ; i++ )
#define LOG cerr << "[" << __LINE__ << "] "
#define pb push_back

const string M = "yhesocvxduiglbkrztnwjpfmaq" ;

int main()
{
	int n ; cin >> n ;
	cin.ignore() ;

	fb (i, n)
	{
		string q ; getline(cin, q) ;
		fe (i, q) if (q[i] != ' ') q[i] = M[ q[i] - 'a' ] ;
		printf ("Case #%d: %s\n", i + 1, q.c_str()) ;
	}

	return 0 ;
}


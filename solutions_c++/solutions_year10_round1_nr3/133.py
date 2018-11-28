/* C Libs */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <ctime>
/* IOstream Libs */
#include <iostream>
#include <fstream>
#include <sstream>
/* String Libs */
#include <string>
/* STL Containers */
#include <bitset>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>
/* STL Algorithm */
#include <algorithm>
/* Miscellaneous */
#include <complex>
#include <functional>
#include <iterator>
//#include <limits>
#include <numeric>
#include <typeinfo>
#include <utility>
#include <valarray>

using namespace std;

#define REP(i,s,t) for(int _t=t,i=s;i<_t;i++ )
#define REPP(i,s,t) for(int _t=t,i=s;i<=_t;i++)

template<class T>
void check_max( T&a, T b ){
	if ( a <  b ) a = b;
}
template<class T>
void check_min( T&a, T b ){
	if ( a > b ) a = b;
}

//#define debug
double up,down;
int t( int x ){
	//[0,x]
	int res = 0;
	if ( x > up )
		res += x - int( floor(up ) ) + int( floor(down) );
	else if ( x > down )
		res += int( floor(down) );
	else res += x;
}
int main(){
	int T;
	cin >> T;
	REP(Case,1,T+1){
		int a1,b1,a2,b2;
		cin >> a1>>a2>>b1>>b2;
		long long ans = 0;
		double ratio = (sqrt(5)-1)/2;
		for( int i = a1; i <= a2; i++ ){
			down = i*ratio;
			up = i/ratio;
			ans += t(b2) - t(b1-1);
		}
		printf("Case #%d: ",Case);
		cout << ans << endl;
	}
	return 0;
}

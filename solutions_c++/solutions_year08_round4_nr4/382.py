#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <cmath>
#include <sstream>
using namespace std;
typedef long long LL;
typedef vector < int > VI;
#define SZ(X) ((int)X.size())
int calc ( string  A) {
	int res = 0;
	for ( int i=0;i< A.length() ; i++ ) {
		char c = A[i];
		res ++;
		while ( i < A.length() && A[i] == c ) i ++;
		i --;
	}
	return res;
}
vector < int > V;
string doit ( string inp ) {
	string res ;
	int k = SZ(V);
	for ( int i=0;i<inp.size();i++ ) {
		res += inp[(i/k)*k + V[i%k]];
	}
	return res;
}
int main() {
	int t;
	cin >> t;
	for ( int n__ = 1 ; n__ <= t; n__ ++ ) {
		cout << "Case #" << n__ <<": " ;
		int res = 1 << 30;
		int k;
		cin >> k;
		string inp;
		cin >> inp;
		V.clear();
		string tmp;
		for (int i=0;i<k;i++ ) V.push_back ( i );
		do {
			tmp = doit ( inp );
			res = min ( res , calc ( tmp ) );
		} while ( next_permutation ( V.begin() , V.end() ) );
		cout << res << endl;
	}
	return 0;
}

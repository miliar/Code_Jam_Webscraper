#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <set>
#include <iomanip>
#include <utility>

#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

#define fori(i, n) for ( int i = 0; i < (n); ++i )
#define forr(i, a, b) for ( int i = (a); i <= (b); ++i )
#define tr(T, i) for (typeof(T.begin()) i = T.begin(); i != T.end(); ++i )
#define sz size()
#define all(x) (x).begin(),(x).end()
#define _sort(x) sort(all(x))
#define pb push_back

template<class T> string a2s(T x) { ostringstream o; o << x; return o.str(); }
template<class T> T s2a(string s) { istringstream i(s); T x; i >> x; return x; }

const double EPS = 1e-9;

int cmp(double x, double y = 0, double tol = EPS)
{
    return ( x <= y + tol ) ? ( x + tol < y ) ? -1 : 0 : 1;
}

int findvec(const vector<int> &vec, int n) {
	int j;
	for(int i = 0; i < vec.size(); i++) {
		if( n == vec[i] ) {
			return i;
		}
	}

	return -1;
}

unsigned long long int recfind(int P, const vector<int> &pris, vector<int> &order) {
	if( order.size() == pris.size() ) {
		vector<int> allpris(P, 1);
		unsigned long long int bribe = 0;
		//cout << "s ";
		//for(int i = 0; i < order.size(); i++) cout << order[i] << " ";
		//cout << endl;
		
		for(int i = 0; i < order.size(); i++) {
			int oi = order[i];
			//cout << oi << " ";
			allpris[ oi ] = 0;

			for(int j = oi+1; j < allpris.size() && allpris[j] == 1; j++) bribe++;
			for(int j = oi-1; j >= 0 && allpris[j] == 1; j--) bribe++;

			//cout << bribe << endl;
		}
		//cout << endl;
		return bribe;
	}

	unsigned long long int min_bribe = LONG_MAX;
	for(int i = 0; i < pris.size(); i++) {
		if( findvec(order, pris[i]) == -1 ) {
			
			order.push_back(pris[i]);
			unsigned long long int bribe = recfind(P, pris, order);
			order.pop_back();

			if( bribe < min_bribe ) min_bribe = bribe;
		}
	}

	return min_bribe;
}

int main()
{
	int T, C;
	cin >> T;
	for(C = 1; C <= T; C++) {
		int P, Q;
		cin >> P >> Q;

		vector< int > pris;
		for(int i = 0; i < Q; i++) {
			int x; 
			cin >> x;
			pris.push_back(x-1);
		}

		vector< int > order;
		unsigned long long int min_bribe = recfind(P, pris, order);

		cout << "Case #" << C << ": " << min_bribe << endl;
	}

    return 0;
}

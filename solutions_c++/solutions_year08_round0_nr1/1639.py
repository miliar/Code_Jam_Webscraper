// Tim Malone
// Google Code Jam Qualifier
// Problem A

#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef vector<int> vi;
typedef set<int> si;
typedef vector<string> vs;
typedef vector< vector<int> > vvi;
typedef pair<int, int> ii;
#define allof(c) (c).begin(), (c).end()
#define allofr(c) (c).rbegin(), (c).rend()
#define forall(it, c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define loop while(1)
#define add push_back
template<typename T> T maxv() { return numeric_limits<T>::max(); }
template<typename T> T minv() { return numeric_limits<T>::min(); }
template<typename T, typename E> int contains(T& c, E x) {
	return find(allof(c), x) != c.end(); }
template<typename E> int contains(set<E>& c, E x) {
	return c.find(x) != c.end(); }
template<typename K, typename E> int contains(map<K, E>& c, K x) {
	return c.find(x) != c.end(); }

int main() {

	ifstream in("A.in");
	ofstream out("A.out");

	int N; in >> N;
	for (int k = 0; k < N; k++) {

		int switches = 0;
		string s;

		vector<string> engines;
		vector<string> queries;

		int S; in >> S;
		engines.reserve(S);
		getline(in, s);
		for (int i = 0; i < S; i++) {
			getline(in, s);
			engines.push_back(s);
		}

		int Q; in >> Q;
		queries.reserve(Q);
		getline(in, s);
		for (int i = 0; i < Q; i++) {
			getline(in, s);
			queries.push_back(s);
		}

		set<string> engineSet;
		engineSet.insert(engines.begin(), engines.end());

		set<string> enginesLeft = engineSet;
		forall(q, queries) {
			if (contains(enginesLeft, *q)) {
				enginesLeft.erase(*q);
				if (enginesLeft.empty()) {
					enginesLeft = engineSet;
					enginesLeft.erase(*q);
					switches++;
				}
			}
		}

		out << "Case #" << (k+1) << ": " << switches << endl;
	}

}

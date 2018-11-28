
// C++ template

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
#include <iomanip>

using namespace std;

typedef vector<int> vi;
typedef set<int> si;
typedef vector<string> vs;
typedef vector< vector<int> > vvi;
typedef pair<int, int> ii;
#define allof(c) (c).begin(), (c).end()
#define allofr(c) (c).rbegin(), (c).rend()
#define forall(it, c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define forallr(it, c) for(typeof((c).rbegin()) it = (c).rbegin(); it != (c).rend(); it++)
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

		multiset<long> freq;
		int P, K, L; in >> P >> K >> L;

		for (int i = 0; i < L; i++) {
			long f; in >> f;
			freq.insert(f);
		}

		long sum = 0;
		int numP = 1;
		int keys = K;
		int imp = 0;
		forallr(it, freq) {
			if (numP > P) imp = 1;
			sum += (*it) * numP;
			keys--;
			if (keys == 0) {
				numP++;
				keys = K;
			}
		}

		//if (imp)
		out << "Case #" << (k+1) << ": ";
		if (!imp)
			out << /*setiosflags(ios::fixed) << setprecision(0) <<*/ sum << endl;
		else out << "Impossible" << endl;
	}
}

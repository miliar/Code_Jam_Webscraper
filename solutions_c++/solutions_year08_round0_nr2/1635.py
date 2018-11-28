// Tim Malone
// Google Code Jam Qualifier
// Problem B

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

int parseTime(string s);

int main() {

	ifstream in("B.in");
	ofstream out("B.out");

	int N; in >> N;
	for (int k = 0; k < N; k++) {

		int T, NA, NB; in >> T >> NA >> NB;

		set<int> times;
		map<int, ii> events;

		for (int i = 0; i < NA; i++) {
			string s; in >> s;
			int departTime = parseTime(s);
			in >> s;
			int arriveTime = parseTime(s) + T;

			times.insert(departTime);
			times.insert(arriveTime);

			if (!contains(events, departTime))
				events[departTime] = ii(0, 0);
			if (!contains(events, arriveTime))
				events[arriveTime] = ii(0, 0);

			events[departTime].first += -1;
			events[arriveTime].second += 1;
		}

		for (int i = 0; i < NB; i++) {
			string s; in >> s;
			int departTime = parseTime(s);
			in >> s;
			int arriveTime = parseTime(s) + T;

			times.insert(departTime);
			times.insert(arriveTime);

			if (!contains(events, departTime))
				events[departTime] = ii(0, 0);
			if (!contains(events, arriveTime))
				events[arriveTime] = ii(0, 0);

			events[departTime].second += -1;
			events[arriveTime].first += 1;
		}

		int Atrains = 0;
		int Btrains = 0;
		int Amin = 0;
		int Bmin = 0;
		forall(t, times) {
			ii e = events[*t];
			Atrains += e.first;
			Btrains += e.second;
			if (Amin > Atrains) Amin = Atrains;
			if (Bmin > Btrains) Bmin = Btrains;
		}

		out << "Case #" << (k+1) << ": " << (-Amin) << " " << (-Bmin) << endl;
	}

}

int parseTime(string s) {

	int h = (s[0] - '0')*10 + (s[1] - '0');
	int min = (s[3] - '0')*10 + (s[4] - '0');
	return h*60 + min;
}

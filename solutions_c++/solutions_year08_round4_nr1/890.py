#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>
#include <iterator>

using namespace std;

template<typename X> class sequence_lister;		// Forward reference

template<typename InIter>
inline ostream& operator<<(ostream& os, sequence_lister<InIter> const& sl) {
//	copy(sl._first, sl._last, ostream_iterator<typename InIter::value_type>(os, sl._delim));
	for (InIter i = sl._first; i != sl._last; ++i) {
		if (i != sl._first) {
			os << sl._delim;
		}
		
		os << *i;
	}
	
	return os;
}

template<typename InIter>
class sequence_lister {
public:
	sequence_lister(InIter first, InIter last, char* delim = "") :
		_first(first),
		_last(last),
		_delim(delim)
	{}
	
	// Also allow construction from any container supporting begin() and end()
	template<typename Cont>
	sequence_lister(Cont& cont, char* delim = "") :
		_first(cont.begin()),
		_last(cont.end()),
		_delim(delim)
	{}
	
	sequence_lister(sequence_lister const& x) :
		_first(x._first),
		_last(x._last),
		_delim(x._delim)
	{}
	
	sequence_lister& operator=(sequence_lister const& x) {
		_first = x._first;
		_last = x._last;
		_delim = x._delim;
	}
	
	friend ostream& operator<< <>(ostream& os, sequence_lister<InIter> const& sl);
	
private:
	InIter _first, _last;
	char* _delim;
};

template<typename InIter>
inline sequence_lister<InIter> list_sequence(InIter first, InIter last, char* delim = "") {
	return sequence_lister<InIter>(first, last, delim);
}

template<typename Cont>
inline sequence_lister<typename Cont::const_iterator> list_sequence(Cont& cont, char* delim = "") {
	return sequence_lister<typename Cont::const_iterator>(cont, delim);
}

class  {
public:
	
};

#define GOR 0
#define GAND 1
#define INF 10001

vector<int> _cache[2];

int solve(int i, int want, int m, vector<int> const& gate, vector<int> const& changeable) {
//	cerr << "solve(i=" << i << ", want=" << want << ") called.\n";
	if (i - 1 >= (m - 1) / 2) {
//		cerr << "i=" << i << " is a leaf with value " << gate[i] << ".\n";
		if (want == gate[i]) {
			return 0;
		} else {
			return INF;
		}
	}
	
	if (_cache[want][i] == -1) {
//		cerr << "This node has not been computed yet.\n";
		int bestCost = INF;
		if (want == 0) {
			// Can either use an AND, with either sub-branch 0, or an OR, with both
			// sub-branches 0.
			if (gate[i] == GOR) {
				int cost = solve(2 * i, 0, m, gate, changeable) + solve(2 * i + 1, 0, m, gate, changeable);
				bestCost = min(bestCost, cost);
			} else {
				int cost = min(solve(2 * i, 0, m, gate, changeable), solve(2 * i + 1, 0, m, gate, changeable));
				bestCost = min(bestCost, cost);
			}
			
			if (changeable[i]) {
				if (gate[i] == GAND) {
					// Change it to OR
					int cost = 1 + solve(2 * i, 0, m, gate, changeable) + solve(2 * i + 1, 0, m, gate, changeable);
					bestCost = min(bestCost, cost);
				} else {
					// Change it to AND
					int cost = 1 + min(solve(2 * i, 0, m, gate, changeable), solve(2 * i + 1, 0, m, gate, changeable));
					bestCost = min(bestCost, cost);
				}
			}
		} else {
			// Can either use an AND, with both sub-branches 1, or an OR, with either
			// sub-branches 1.
			if (gate[i] == GOR) {
				int cost = min(solve(2 * i, 1, m, gate, changeable), solve(2 * i + 1, 1, m, gate, changeable));
				bestCost = min(bestCost, cost);
			} else {
				int cost = solve(2 * i, 1, m, gate, changeable) + solve(2 * i + 1, 1, m, gate, changeable);
				bestCost = min(bestCost, cost);
			}
			
			if (changeable[i]) {
				if (gate[i] == GAND) {
					// Change it to OR
					int cost = 1 + min(solve(2 * i, 1, m, gate, changeable), solve(2 * i + 1, 1, m, gate, changeable));
					bestCost = min(bestCost, cost);
				} else {
					// Change it to AND
					int cost = 1 + solve(2 * i, 1, m, gate, changeable) + solve(2 * i + 1, 1, m, gate, changeable);
					bestCost = min(bestCost, cost);
				}
			}
		}
		
//		cerr << "About to assign " << bestCost << " to _cache...\n";
		_cache[want][i] = bestCost;
	}
	
//	cerr << "solve(i=" << i << ", want=" << want << ") returning " << _cache[want][i] << ".\n";
	return _cache[want][i];
}

int main(int argc, char **argv) {
	int nCases;
	{ string s; getline(cin, s); istringstream iss(s); iss >> nCases; }
	
	for (int iCase = 1; iCase <= nCases; ++iCase) {
		int m, v;
		{ string s; getline(cin, s); istringstream iss(s); iss >> m >> v; }
		
		vector<int> gate(m + 1);
		vector<int> changeable(m + 1);
		for (int i = 0; i < (m - 1) / 2; ++i) {
			int g, c;
			{ string s; getline(cin, s); istringstream iss(s); iss >> g >> c; }
			gate[i + 1] = g;
			changeable[i + 1] = c;
		}
		
		for (int i = (m - 1) / 2; i < m; ++i) {
			int x;
			{ string s; getline(cin, s); istringstream iss(s); iss >> x; }
			gate[i + 1] = x;
		}
		
		_cache[0].clear();
		_cache[1].clear();
		_cache[0].resize(m + 1, -1);
		_cache[1].resize(m + 1, -1);
//		cerr << "About to call solve()...\n";
		int result = solve(1, v, m, gate, changeable);
//		cerr << "Called solve().\n";
		
		cout << "Case #" << iCase << ": ";
		if (result == INF) {
			cout << "IMPOSSIBLE";
		} else {
			cout << result;
		}
		
		cout << endl;
	}
	
	return 0;
}

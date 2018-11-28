#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>
#include <iterator>
#include <map>
#include <cassert>

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

vector<vector<int> > _cache;		// DP memoization cache

void clearCache(int nEngines, int nQueries) {
	_cache.clear();
	_cache.resize(nEngines, vector<int>(nQueries + 1, -1));
//	cerr << "Inside clearCache():\n";
//cerr << "nEngines = <" << nEngines << ">\n";		//DEBUG
//cerr << "nQueries = <" << nQueries << ">\n";		//DEBUG
//cerr << "_cache.size() = <" << _cache.size() << ">\n";		//DEBUG
//cerr << "_cache[0].size() = <" << _cache[0].size() << ">\n";		//DEBUG
}

// Calculate the minimum number of engine changes so far, given that after
// iQueries queries we are in engine iEng.
int f(int iEng, int iQueries, int nEngines, vector<int> const& queries) {
	int retVal;
	
//cerr << "_cache.size() = <" << _cache.size() << ">\n";		//DEBUG
//cerr << "_cache[0].size() = <" << _cache[0].size() << ">\n";		//DEBUG

	assert(_cache.size() == nEngines);
	assert(_cache[0].size() == queries.size() + 1);
	
//	cerr << "f(iEng=" << iEng << ", iQueries=" << iQueries << ") called.\n";
	if (iQueries == 0) {
		retVal = 0;		// No charge for choosing the initial engine
	} else {
		if (_cache[iEng][iQueries] != -1) {
			return _cache[iEng][iQueries];
		} else {
//			if (iQueries < queries.size() && iEng == queries[iQueries]) {
			if (iEng == queries[iQueries - 1]) {
				// This is not allowed!
				retVal = numeric_limits<int>::max();
			} else {
				int best = numeric_limits<int>::max();
				for (int j = 0; j < nEngines; ++j) {
					int x = f(j, iQueries - 1, nEngines, queries);
					if (j != iEng) {
						// Avoid integer wraparound
						if (x != numeric_limits<int>::max()) {
							++x;
						}
					}
					
					best = min(best, x);
				}
				
				retVal = best;
			}
		}
		
		_cache[iEng][iQueries] = retVal;
	}
	
//	cerr << "f(iEng=" << iEng << ", iQueries=" << iQueries << ") returning " << retVal << ".\n";
	
	return retVal;
}

int main(int argc, char **argv) {
	int nCases;
	string s;
	getline(cin, s);
	{ istringstream iss(s); iss >> nCases; }
	
	for (int iCase = 0; iCase < nCases; ++iCase) {
		int nEngines;
		getline(cin, s);
		{ istringstream iss(s); iss >> nEngines; }
		
//		cerr << "nEngines = <" << nEngines << ">\n";		//DEBUG
	
		vector<string> engineNames;
		map<string, int> engineNameToIndex;
		for (int i = 0; i < nEngines; ++i) {
			getline(cin, s);
			engineNames.push_back(s);
			engineNameToIndex[s] = i;
		}
		
		int nQueries;
		getline(cin, s);
		{ istringstream iss(s); iss >> nQueries; }
		
//		cerr << "nQueries = <" << nQueries << ">\n";		//DEBUG
	
		vector<int> queries;
		for (int i = 0; i < nQueries; ++i) {
			getline(cin, s);
			queries.push_back(engineNameToIndex[s]);
		}
		
//		cerr << list_sequence(queries, "\n") << endl;
		
		clearCache(nEngines, nQueries);
		
		int best = numeric_limits<int>::max();
		for (int i = 0; i < nEngines; ++i) {
			best = min(best, f(i, nQueries, nEngines, queries));
		}
		
		cout << "Case #" << (iCase + 1) << ": " << best << endl;
	}
	
	return 0;
}

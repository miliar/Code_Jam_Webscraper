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

int main(int argc, char **argv) {
	int nCases;
	{ string s; getline(cin, s); istringstream iss(s); iss >> nCases; }
	
	for (int iCase = 1; iCase <= nCases; ++iCase) {
		int n, m;
		{ string s; getline(cin, s); istringstream iss(s); iss >> n; }
		{ string s; getline(cin, s); istringstream iss(s); iss >> m; }
		
		vector<bool> makeMalted(n, false);
		int nMakeMalted = 0;
		vector<vector<int> > likesUnmalted(m, vector<int>());
		vector<int> likesMalted(m, -1);
		for (int i = 0; i < m; ++i) {
			string s;
			getline(cin, s);
			istringstream iss(s);
			
			int t;
			iss >> t;
//cerr << "t = <" << t << ">\n";		//DEBUG
			for (int j = 0; j < t; ++j) {
				int x, y;
				iss >> x >> y;
				--x;		// Use 0-based indices dammit!
				if (y) {
					likesMalted[i] = x;
//					if (!makeMalted[x]) {
//						makeMalted[x] = true;
//						++nMakeMalted;
//					}
				} else {
					likesUnmalted[i].push_back(x);
				}
			}
			
//			if (likesMalted[i] != -1 && likesUnmalted[i].empty()) {
//				// This customer only likes one flavour, and it's malted.
//				cerr << "Customer " << i << " only likes one flavour (" << likesMalted[i] << ") and he likes it malted.\n";
//				makeMalted[likesMalted[i]] = true;
//			}
		}
		
		int i = 0;
		bool possible = true;
		vector<bool> satisfiedByMalted(m, false);
		while (possible && i < m) {
//			cerr << "Top of cust-check loop...\n";
			for (i = 0; i < m; ++i) {
				// Does this customer like only unmalted flavours that are already
				// required to be malted?
				if (!satisfiedByMalted[i]) {
					bool ok = false;
					for (int j = 0; j < likesUnmalted[i].size(); ++j) {
						if (!makeMalted[likesUnmalted[i][j]]) {
							ok = true;
							break;
						}
					}
					
					if (!ok) {
						// We have to try to satisfy the customer using his malted
						// flavour, if possible
						if (likesMalted[i] != -1) {
//							cerr << "Customer " << i << " needs flavour " << likesMalted[i] << " in malted.\n";
							satisfiedByMalted[i] = true;
							makeMalted[likesMalted[i]] = true;
							break;
						} else {
							possible = false;
							break;
						}
					}
				}
			}
		}
		
		cout << "Case #" << iCase << ":";
		if (possible) {
			for (int i = 0; i < n; ++i) {
				cout << ' ' << static_cast<int>(makeMalted[i]);
			}
			cout << endl;
		} else {
			cout << " IMPOSSIBLE" << endl;
		}
	}
	
	return 0;
}

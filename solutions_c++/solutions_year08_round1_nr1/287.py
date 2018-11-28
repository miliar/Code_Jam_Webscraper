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
	
	for (int i = 0; i < nCases; ++i) {
		int n;
		{ string s; getline(cin, s); istringstream iss(s); iss >> n; }
		
		vector<int> v[2];
		for (int j = 0; j < 2; ++j) {
			string s;
			getline(cin, s);
			istringstream iss(s);
			copy(istream_iterator<int>(iss), istream_iterator<int>(), back_inserter(v[j]));
			sort(v[j].begin(), v[j].end());
		}
		
		int total = 0;
		for (int k = 0; k < n; ++k) {
			total += v[0][k] * v[1][n - k - 1];
		}
		
		cout << "Case #" << (i + 1) << ": " << total << endl;
	}
	
	return 0;
}

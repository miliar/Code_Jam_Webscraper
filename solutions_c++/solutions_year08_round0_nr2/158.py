#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <limits>
#include <iterator>
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

int timeToMinute(string s) {
	assert(s.size() == 5);
	assert(s[2] == ':');
	
	return ((s[0] - '0') * 10 + (s[1] - '0')) * 60 + (s[3] - '0') * 10 + s[4] - '0';
}

template<typename T>
class SortAscByFirst {
public:
	bool operator()(T a, T b) {
		return a.first < b.first;
	}
};

// Assumes that fromA and fromB are both sorted in ascending order by departure
// time.
pair<int, int> solve(vector<pair<int, int> > *from, int turnTime) {
	if (from[0].empty()) {
		return make_pair<int, int>(0, from[1].size());
	} else if (from[1].empty()) {
		return make_pair<int, int>(from[0].size(), 0);
	} else {
		// At least one train departing from each station.
		int x = 0;
		if (from[1].front().first < from[0].front().first) {
			x = 1;
		}
		
//		int y = 1 - x;
		
		int nT[2] = { 0, 0 };
		nT[x] = 1;
		
		int nextReadyTime = 0;
		
		// Find the greedy route for the next train from station A, and delete
		// all trips visited.
		int i[2] = { 0, 0 };
		while (i[x] < from[x].size()) {
			if (nextReadyTime <= from[x][i[x]].first) {
				nextReadyTime = from[x][i[x]].second + turnTime;
				from[x].erase(from[x].begin() + i[x]);
				x = 1 - x;
			} else {
				++i[x];
			}
		}
		
		pair<int, int> subResult = solve(from, turnTime);
		subResult.first += nT[0];
		subResult.second += nT[1];
		return subResult;
	}
}

int main(int argc, char **argv) {
	int nCases;
	{ string s; getline(cin, s); istringstream iss(s); iss >> nCases; }
	
	for (int iCase = 0; iCase < nCases; ++iCase) {
		int turnTime;
		{ string s; getline(cin, s); istringstream iss(s); iss >> turnTime; }
		
		int nTrips[2];
		{ string s; getline(cin, s); istringstream iss(s); iss >> nTrips[0] >> nTrips[1]; }
		
		vector<pair<int, int> > from[2];
		for (int iStation = 0; iStation < 2; ++iStation) {
			for (int i = 0; i < nTrips[iStation]; ++i) {
				string depStr, arrStr;
				{ string s; getline(cin, s); istringstream iss(s); iss >> depStr >> arrStr; }
				
				int depMin = timeToMinute(depStr);
				int arrMin = timeToMinute(arrStr);
				
				from[iStation].push_back(make_pair(depMin, arrMin));
			}
		}
		
		SortAscByFirst<pair<int, int> > sorter;
		sort(from[0].begin(), from[0].end(), sorter);
		sort(from[1].begin(), from[1].end(), sorter);
		pair<int, int> result = solve(from, turnTime);
		
		cout << "Case #" << (iCase + 1) << ": " << result.first << ' ' << result.second << endl;
	}
	
	return 0;
}

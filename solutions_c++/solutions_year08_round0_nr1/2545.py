#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class myVector {
	int _count, _semicount;
	typedef vector<pair<string, bool>*> List;
	List vs;
	bool _locked;

public:

	class LockedException {};

	myVector(): _count(0), _semicount(0), _locked(false) {}

	~myVector() {
		for(List::iterator i=vs.begin(); i!=vs.end(); ++i) {
			delete *i;
		}

	}

	void add(string s) {
		if (_locked) throw new LockedException();

		for(List::iterator i=vs.begin(); i!=vs.end(); ++i) {
			if ((*i)->first == s) return;
		}

		vs.push_back(new pair<string, bool>(s, false));
		++_count; ++_semicount;
	}

	void reset() {
		_semicount = _count;
		for(List::iterator i=vs.begin(); i!=vs.end(); ++i) {
			(*i)->second = false;
		}
	}

	bool remove(string s) {
		if (!_locked) lock();

		for(List::iterator i=vs.begin(); i!=vs.end(); ++i) {
			if ((*i)->first == s) {
				//already removed
				if ((*i)->second) return false;

				//still on the list
				--_semicount;
				(*i)->second = true;
				if (_semicount == 0) {
					reset(); --_semicount; (*i)->second=true;
					return true;
				}
				break;
			}
		}
		return false;
	}

	void clear() {
		_count=0;
		reset();
		_locked=false;
		vs.clear();
	}

	inline void lock() {
		_locked = true;
	}

};

typedef vector<string>::iterator vsi;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	//ifstream fin("A-small.in");
	//ofstream fout("A-small.out");

	unsigned int nCases, nEngines, nTerms, j, final=0;
	myVector engines;
	vector<string> terms;
	string temp;

	fin >> nCases;

	for (unsigned int i=0; i < nCases; ++i) {
		fin >> nEngines;
		getline(fin, temp);

		for (j=0; j < nEngines; ++j) {
			getline(fin, temp);
			engines.add(temp);
		}

		fin >> nTerms;
		getline(fin, temp);

		for (j=0; j < nTerms; ++j) {
			getline(fin, temp);
			terms.push_back(temp);
		}

		vsi it;
		j=0;
		for(it=terms.begin(); it != terms.end(); ++it) {
			if(engines.remove(*it)) ++j;
		}

		fout << "Case #" << i+1 << ": " << j << endl;

		engines.clear();
		terms.clear();
	}

	return 0;
}
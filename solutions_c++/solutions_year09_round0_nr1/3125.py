#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <stdlib.h>
#include <list>
#include <map>
#include <vector>
using namespace std;

list<int> listunion(list<int>& a, list<int>& b ) {
	list<int> result;
	result.clear();
	list<int>::iterator ia = a.begin();
	list<int>::iterator ib = b.begin();
	while (ia != a.end() || ib != b.end()) {
		if (ia == a.end() && ib != b.end()) {
			if (*ib != *(result.rbegin()))
				result.push_back(*ib);
			++ib;
		}
		else if (ia != a.end() && ib == b.end()) {
			if (*ia != *(result.rbegin()))
				result.push_back(*ia);
			++ia;
		}
		else if (*ia == *ib) {
			if (*ia != *(result.rbegin()))
				result.push_back(*ia);
			++ia;
			++ib;
		}
		else if (*ia < *ib) {
			if (*ia != *(result.rbegin()))
				result.push_back(*ia);
			++ia;
		}
		else if (*ia > *ib) {
			if (*ib != *(result.rbegin()))
				result.push_back(*ib);
			++ib;
		}
	}
	return result;
}

list<int> listintersect(list<int>& a, list<int>& b ) {
	list<int> result;
	result.clear();
	list<int>::iterator ia = a.begin();
	list<int>::iterator ib = b.begin();
	while (ia != a.end() && ib != b.end()) {
		if (*ia == *ib) {
			if (*ia != *(result.rbegin()))
				result.push_back(*ia);
			++ia;
			++ib;
		}
		else if (*ia < *ib) {
			++ia;
		}
		else if (*ia > *ib) {
			++ib;
		}
	}
	return result;
}


int main(int argc, char** argv) {
	if (argc != 2) {
		return -1;
	}
	char filename[256] = {0};
	strcpy(filename, argv[1]);

	ifstream ifs(filename);
	int L = 0, N = 0, D = 0;
	ifs >> L >> N >> D;
	//cout << L << " " << N << " " << D << endl;

	vector<map<char, list<int> > > all;

	all.resize(L);
	string instr = "";
	for (int i = 0; i < N; ++i) {
		ifs >> instr;
		for (int j = 0 ; j < L; ++j) {
			char c = instr[j];
			all[j];
			map<char, list<int> >::iterator imap = all[j].find(c);
			if (imap == all[j].end()) {
				list<int> newlist;
				newlist.push_back(i);
				all[j].insert(make_pair(c, newlist));
			}
			else {
				imap->second.push_back(i);
			}
		}
	}
	/*
	for (int i = 0; i < L; ++i) {
		cout << i << ":" << endl;
		map<char, list<int> >::iterator imap;
		for (imap = all[i].begin(); imap != all[i].end(); ++imap) {
			cout << "\t" << imap->first << "=";
			list<int>::iterator il;
			for (il = imap->second.begin(); il != imap->second.end(); ++il) {
				cout << *il << " ";
			}
			cout << endl;
		}
		cout << endl;
	}
	*/

	for (int i = 0; i < D; ++i) {
		ifs >> instr;
		int len = instr.length();
		list<int> result;
		list<int> posresult;
		int inbrac = 0;
		int poscount = 0;
		int lettercount = 0;
		for (int j = 0; j < len; ++j) {
			if (inbrac == 0 && instr[j] >= 'a' && instr[j] <= 'z') {
				posresult = all[poscount][instr[j]];
				if (poscount == 0) {
					result = posresult;
				}
				else {
					result = listintersect(result, posresult);
				}
				++poscount;
				lettercount = 0;
			}
			else if (instr[j] == '(') {
				posresult.clear();
				lettercount = 0;
				++inbrac;
			}
			else if (instr[j] == ')') {
				if (poscount == 0) {
					result = posresult;
				}
				else {
					result = listintersect(result, posresult);
				}
				++poscount;
				lettercount = 0;
				--inbrac;
			}
			else {
				if (lettercount == 0) {
					posresult = all[poscount][instr[j]];
				}
				else {
					posresult = listunion(posresult, all[poscount][instr[j]]);
				}
				++lettercount;
			}
			if (poscount > 0 && result.size() <= 0) {
				break;
			}
		}
		cout << "Case #" << (i+1) << ": " << result.size() << endl;
	}

	/*
	int length = 0, tempno = 0;;
	list<int> a;
	a.clear();
	ifs >> length;
	for (int i = 0; i < length; ++i) {
		ifs >> tempno;
		a.push_back(tempno);
	}

	list<int> b;
	b.clear();
	ifs >> length;
	for (int i = 0; i < length; ++i) {
		ifs >> tempno;
		b.push_back(tempno);
	}

	list<int> intersect = listintersect(a, b);
	cout << "intersection: ";
	for (list<int>::iterator i = intersect.begin(); i != intersect.end(); ++i) {
		cout << *i << " ";
	}
	cout << endl;
	list<int> lunion = listunion(a, b);
	cout << "union: ";
	for (list<int>::iterator i = lunion.begin(); i != lunion.end(); ++i) {
		cout << *i << " ";
	}
	cout << endl;
	*/

	return 0;
}


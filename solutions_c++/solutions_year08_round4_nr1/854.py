#include <windows.h>

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
using namespace std;

//#define PRINT_DEBUG

struct VoidStream {};
template<typename T>
inline VoidStream & operator<<(VoidStream &v, T t) {
	return v;
}

#ifdef PRINT_DEBUG
	#define OUT_DEBUG std::cout
#else
	VoidStream _vs_;
	#define OUT_DEBUG _vs_
#endif




class BooleanNode {
public:
	int gate_type;
	bool changeable;
	int value;

	BooleanNode *cL;
	BooleanNode *cR;

	inline BooleanNode(int G, int C) : gate_type(G), changeable(C==1), value(2) {}
	inline BooleanNode(int I) : value(I) {}

	bool isAND() { return (gate_type==1); }
	bool isOR() { return !isAND(); }
	bool isValue() { return (value != 2); }


	int getNumChangesToValue(int v) {
		// simplest case: a leaf
		if (isValue()) {
			return (v == value) ? 0 : -1;
		}

		int iL0 = cL->getNumChangesToValue(0);
		int iL1 = cL->getNumChangesToValue(1);
		int iR0 = cR->getNumChangesToValue(0);
		int iR1 = cR->getNumChangesToValue(1);

		int iNoChange = -1;
		int iWithChange = -1;

		if (v == 1) {
			if (isAND()) {
				if (iL1 >=0 && iR1 >=0)
					iNoChange = iL1 + iR1;
			} else {
				if (iL1 >=0 || iR1 >=0)
					iNoChange = (iL1 >=0) ? (iR1 >=0 ? (min(iL1, iR1)) : iL1) : iR1;
			}

			if (changeable) {
				if (isOR()) {
					// changed to AND
					if (iL1 >=0 && iR1 >=0)
						iWithChange = iL1 + iR1 + 1;
				} else {
					if (iL1 >=0 || iR1 >=0)
						iWithChange = ((iL1 >=0) ? (iR1 >=0 ? (min(iL1, iR1)) : iL1) : iR1) + 1;
				}
			}
		} else {
			// v == 0
			if (isOR()) {
				if (iL0 >=0 && iR0 >=0)
					iNoChange = iL0 + iR0;
			} else {
				if (iL0 >=0 || iR0 >=0)
					iNoChange = (iL0 >=0) ? (iR0 >=0 ? (min(iL0, iR0)) : iL0) : iR0;
			}

			if (changeable) {
				if (isAND()) {
					if (iL0 >=0 && iR0 >=0)
						iWithChange = iL0 + iR0 + 1;
				} else {
					if (iL0 >=0 || iR0 >=0)
						iWithChange = ((iL0 >=0) ? (iR0 >=0 ? (min(iL0, iR0)) : iL0) : iR0) + 1;
				}
			}
		}

		if (iNoChange < 0 && iWithChange < 0)
			return -1;
		if (iNoChange < 0)
			return iWithChange;
		if (iWithChange < 0)
			return iNoChange;
		return min(iNoChange, iWithChange);
	}
};

typedef vector<BooleanNode*> AllNodes;

	
	
	
void doCase(ifstream &in, int cnum) {
	unsigned int M, V;
	in >> M;
	in >> V;

	// read the nodes
	AllNodes all;
	unsigned int gates = (M-1)/2;
	for (unsigned int n = 0; n < gates; n++) {
		unsigned int G, C;
		in >> G >> C;
		BooleanNode *pNode = new BooleanNode(G, C);
		all.push_back(pNode);

		unsigned int parentIdx = (n+1) / 2;
		if (parentIdx > 0) {
			bool isLeft = ((parentIdx*2) == (n+1));
			if (isLeft)
				all[parentIdx-1]->cL = pNode;
			else
				all[parentIdx-1]->cR = pNode;
		}
	}

	for (unsigned int n = gates; n < M; n++) {
		unsigned int I;
		in >> I;
		BooleanNode *pNode = new BooleanNode(I);

		unsigned int parentIdx = (n+1) / 2;
		if (parentIdx > 0) {
			bool isLeft = ((parentIdx*2) == (n+1));
			if (isLeft)
				all[parentIdx-1]->cL = pNode;
			else
				all[parentIdx-1]->cR = pNode;
		}
	}

	int numChanges = all[0]->getNumChangesToValue(V);

	cout << "Case #" << cnum << ": ";
	if (numChanges < 0)
		cout << "IMPOSSIBLE";
	else 
		cout << numChanges;
	cout << endl;
}



int main(int agrc, char *argv[]) {
	OUT_DEBUG << "reading from file \"" << argv[1] << "\"\n";
	ifstream in(argv[1]);
	if (!in.is_open()) {
		cout << "Can't read from file\n";
		return 1;
	}

	unsigned int num_cases;
	in >> num_cases;
	OUT_DEBUG << "num of cases: " << num_cases << '\n';

	for (unsigned int i = 0; i < num_cases; i++) {
		doCase(in, i+1);
	}

	return 0;
}

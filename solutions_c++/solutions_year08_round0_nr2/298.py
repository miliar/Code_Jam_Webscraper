#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector <int> arrA, arrB, depA, depB;
int T;

int Tim(string s) {
	return atoi(s.c_str())*60 + atoi(s.c_str()+3);
}

void Zeile() {
	string Dep,Arr;
	cin >> Dep >> Arr;
	cerr << "#" << Dep << ", " << Arr << endl;
	depB.push_back(Tim(Dep));
	arrB.push_back(Tim(Arr) +T);
}

int follow(vector<int>& P,vector<int>& M) {
	sort(P.begin(),P.end());
	sort(M.begin(),M.end());
	vector <int>::iterator iP = P.begin();
	vector <int>::iterator iM = M.begin();
	int high = 0, ac =0;
	while (iP != P.end()) {
		int tM, tP;
		if (iM == M.end()) tM = 100000; else tM = *iM;
		tP = *iP;
		if (tP == tM) {
			cerr << "jit @" << (tP/60) << ":" << (tP%60) << endl;
			++iM; ++iP;
		} else if (tP < tM) {
			++ac;
			cerr << ":( @ " << (tP/60) << ":" << (tP%60) << endl;
			if (ac>high) {
				high=ac;
				cerr << "+zug @" << (tP/60) << ":" << (tP%60) << endl;
			}
			++iP;
		} else {
			cerr << ":) @ " << (tM/60) << ":" << (tM%60) << endl;
			--ac;
			++iM;
		}
	}
	return high;
}

void Fall(int run) {
		//cerr << "#" <<  i << endl;
		int NA, NB; 
		cin >> T; 
		cerr << "#T=" << T << endl;
		cin >> NA >> NB;
		cerr << "#NA=" << NA << ", NB=" << NB << endl;
		arrB.clear(); depB.clear();
		for (int i=0; i<NA; ++i) {
			Zeile();
		}
		arrA = arrB; depA = depB;
		arrB.clear(); depB.clear();
		for (int i=0; i<NB; ++i) {
			Zeile();
		}

		cerr << "A:" << depA.size() << "/" << arrB.size() << endl;
		int needA = follow(depA,arrB);
		cerr << "B:" << depB.size() << "/" << arrA.size() << endl;
		int needB = follow(depB,arrA);
		cout << "Case #" << run << ": " << needA << " " << needB << endl;
}

int main() {
	int N;
	
	char line[256];
	
	cin >> N;
	for (int run=1; run<=N; ++run) {
		Fall(run);
	}
}

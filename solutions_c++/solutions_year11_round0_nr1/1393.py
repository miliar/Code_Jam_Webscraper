
#include <iostream>
#include <vector>
using namespace std;


int next(int pos, int dest) {
	if(dest > pos) return pos+1;
	if(dest < pos) return pos-1;
	return pos;
}


int solve(vector<int> A, vector<int> B) {
	int posa = 1, posb = 1;
	int ia = 0, ib = 0, k = 0;
	int desta, destb;
/*
	for(int i = 0; i < A.size(); i++) cerr << A[i] << ' ';
	cerr << endl;
	for(int i = 0; i < B.size(); i++) cerr << B[i] << ' ';
	cerr << endl;
*/
	for(int t = 0; true; t++) {
//		cerr << t << " " << posa << " " << posb << " " << ia << " " << ib << endl;
		if(2*ia >= A.size() && 2*ib >= B.size()) return t;
		if(2*ia < A.size()) desta = A[2*ia];
		if(2*ib < B.size()) destb = B[2*ib];
//		cerr << t << " " << desta << " " << destb << endl;

		if(posa == desta && 2*ia < A.size() && k == A[2*ia+1]) {ia++; k++;}
		else if(posb == destb && 2*ib < B.size() && k == B[2*ib+1]) {ib++; k++;}

		posa = next(posa, desta);
		posb = next(posb, destb);
	}
}

int main() {
	int T, N, nb;
	string S;

	cin >> T;
	for(int t = 1; t <= T; t++) {
		cin >> N;
		vector<int> A, B;
		for(int i = 0; i < N; i++) {
			cin >> S >> nb;
			if(S == "O") {
				A.push_back(nb);
				A.push_back(i);
			}
			else {
				B.push_back(nb);
				B.push_back(i);
			}
		}
		cout << "Case #" << t << ": " << solve(A, B) << endl;
	}


}

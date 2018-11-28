#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <list>
using namespace std;

typedef long long lint;
typedef long long ulint;

static const unsigned IMPOSSIBLE = 20001;

struct scoreT {
	unsigned score[2];
	
	scoreT () {
		score[0] = IMPOSSIBLE;
		score[1] = IMPOSSIBLE;
	}
	
	scoreT (bool n) {
		if (!n) {
			score[0] = 0;
			score[1] = IMPOSSIBLE;
		} else {
			score[0] = IMPOSSIBLE;
			score[1] = 0;
		}
	}
};

int main(int argc, char const *argv[]) {
	unsigned nCases;
	cin >> nCases;
	for (unsigned N = 1; N <= nCases; N++) {
		unsigned M, V;
		cin >> M >> V;
		//cout << M << " " << V << endl;
		unsigned nInterior = (M - 1) / 2;
		unsigned nLeaves = (M + 1) / 2;
		
		bool gates[nInterior];
		bool changeable[nInterior];
		bool leaves[nLeaves];
		for (unsigned i = 0; i < nInterior; i++) {
			cin >> gates[i];
			cin >> changeable[i];
			//cout << gates[i] << " " << changeable[i] << endl;
		}
		for (unsigned i = 0; i < nLeaves; i++) {
			cin >> leaves[i];
			//cout << leaves[i] << endl;
		}
		scoreT nodes[M];
		for (unsigned i = nInterior; i < M; i++) {
			scoreT score(leaves[i - nInterior]);
			nodes[i] = score;
		}
		for (int i = nInterior - 1; i >= 0; i--) {
			int left = i * 2 + 1;
			int right = left + 1;
			for (int j = 0; j < 4; j++) {
				bool il = j % 2;
				bool ir = j / 2 % 2;
				bool result;
				if (gates[i]) {
					result = il & ir;
				} else {
					result = il | ir;
				}
				nodes[i].score[result] = min(nodes[i].score[result],
				                             nodes[left].score[il] +
                                             nodes[right].score[ir]);
				if (changeable[i]) {
					if (gates[i]) {
						result = il | ir;
					} else {
						result = il & ir;
					}
					nodes[i].score[result] = min(nodes[i].score[result],
					                             nodes[left].score[il] +
	                                             nodes[right].score[ir] + 1);
				}	
			}
		}
		
		
		cout << "Case #" << N << ": ";
		if (nodes[0].score[V] == IMPOSSIBLE)
			cout << "IMPOSSIBLE";
		else
			cout << nodes[0].score[V];
		cout << endl;
	}
	
	return 0;
}
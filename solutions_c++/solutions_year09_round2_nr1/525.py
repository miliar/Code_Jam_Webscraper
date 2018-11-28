// for MinGW g++ 3.4.5
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

using namespace std;

class decisionTree {
public:
	double weight;
	string feature;
	decisionTree *yesTree;
	decisionTree *noTree;
	decisionTree() : weight(0.0), feature(""), yesTree(0), noTree(0) {
	}
};

decisionTree * buildTree() {
	decisionTree *it = new decisionTree();
	char c = ' ';
	while (c <= ' ')	cin >> c;
	cin >> it->weight;
	c = ' ';
	while (c <= ' ')	cin >> c;
	if (c != ')') {
		cin.putback(c);
		string feature;
		cin >> feature;
		it->feature = feature;
		it->yesTree = buildTree();
		it->noTree  = buildTree();
		c = ' ';
		while (c <= ' ')	cin >> c;
	}
	return it;
}

int main(){
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": " << endl;

		int L;
		cin >> L;
		
		decisionTree * dt = buildTree();
		int A;
		cin >> A;
		string line;
		getline(cin, line);
		for (int a = 1; a <= A; a++) {
			string animal;
			cin >> animal;
			int C;
			cin >> C;
			vector<string> features;
			for (int c = 1; c <= C; c++) {
				string feature;
				cin >> feature;
				features.push_back(feature);
			}
			
			decisionTree * pDt = dt;
			double value = 1.0;
			for (;;) {
				value *= pDt->weight;
				if (pDt->yesTree == 0 && pDt->noTree == 0)	break;
				if (find(features.begin(), features.end(), pDt->feature) != features.end()) {
					pDt = pDt->yesTree;
				} else {
					pDt = pDt->noTree;
				}
			}
			cout << setiosflags(ios::fixed) << setprecision(7) << value << endl;
		}
	}
}

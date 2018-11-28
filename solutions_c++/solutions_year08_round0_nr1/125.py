/** GCJ 2008: Problem A **/

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <string>

using namespace std;


const int oo = 10000000, MAX_Q = 1007, MAX_S = 107;
int S, Q;
int item[MAX_Q];
int best[2][MAX_S];
map<string, int> id;


inline int process() {
	int cur = 0, prev = 1;
	for (int i = 0; i < S; i++) best[cur][i] = 0;

	int prevbest = 0;
	for (int p = Q - 1; p >= 0; p--) {
		cur = 1 - cur;
		prev = 1 - prev;
	
		//cout << "p: " << p << endl;
		int next_prevbest = oo;
		for (int k = 0; k < S; k++) {
			int &r = best[cur][k];
			if (item[p] != k) r = best[prev][k];
			else					r = 1 + prevbest;

			if (r < next_prevbest && (p == 0 || k != item[p - 1]))
				next_prevbest = r;

			//cout << "\tk: " << k << " best: " << r << endl;
		}

		prevbest = next_prevbest;
		//cout << "\t\tprevbest: " << prevbest << endl;
	}

	return prevbest;
}


int main() {
	int N;
	cin >> N;
	string line;
	for (int t = 1; t <= N; t++) {
		cin >> S;
		
		id.clear();

		getline(cin, line);
		for (int i = 0; i < S; i++) {
			getline(cin, line);
			id[line] = i;
		}

		cin >> Q;
		
		getline(cin, line);
		for (int i = 0; i < Q; i++) {
			getline(cin, line);
			item[i] = id[line];
		}

		//if (t != 9) continue;

		//cout << "S: " << S << " Q: " << Q << endl;

		
		//cout << "Printing queue:";
		//for (int i = 0; i < Q; i++) {
		//	cout << " " << item[i];
		//}
		//cout << endl;
		

		int ret = process();

		cout << "Case #" << t << ": " << ret << endl;
	}

	return 0;
}





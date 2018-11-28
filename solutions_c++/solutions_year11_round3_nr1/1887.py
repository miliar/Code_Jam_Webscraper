#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef long long int lli;
typedef pair<int, int> pi;

//void func1(vector <string> str) {

//}
void print_board(vector <vector <int> > v) {
	bool c_first = true;
	bool r_first = true;
	for (int i=0; i<v.size(); i++) {
		vector<int> vv = v[i];
		for (int j=0; j<vv.size(); j++) {
			switch (vv[j]) {
				case 0:
					cout << '.';
					break;
				case 1:
					cout << '/';
					break;
				case 2:
					cout << '\\';
					break;
				case 3:
					cout << '\\';
					break;
				case 4:
					cout << '/';
					break;
			}

		}
			cout << endl;

	}
}

int main(void) { 
	bool debug = false;
	int t, n, r, c;
	cin >> t;
	for (int i=0; i<t; i++) {
		cout << "Case #" << (i+1) << ": " << endl;
		cin >> r >> c;
		string str;
		vector<string> v;
		for (int j=0; j<r; j++) {
			cin >> str;
			v.push_back(str);
		}

		vector<int> prev;
		for (int j=0; j<c; j++) {
			prev.push_back(0);
		}

		vector < vector <int> > board;
		bool bexit = false;
		for (int j=0; j<r; j++) {
			//	func1(j, v, );

			string s = v[j];
			bool border = true;
			for (int k=0; k<c; k++) {
				char prevc = '.';
				if (debug) {
				if (border) cout << "|";
				else cout << "-";
				}
				switch (s.at(k)) {
					case '.':
						if (! border) {
							bexit = true;
							break;
						}
						if (prev[k] == 1 || prev[k] == 2) {
							bexit = true;
							break;
						}
						border = true;
						prev[k] = 0;
						break;
					case '#':
						if (!border) {
							if (prev[k] == 1) {
								bexit = true;
								break;
							} else if (prev[k] == 2) {
								prev[k] = 4;	

							} else {
								prev[k] = 2;
							}


							border = true;
						} else {
							if (prev[k] == 1) {
								prev[k] = 3;
							} else if (prev[k] == 2) {
								bexit = true;
								break;
							} else {
								prev[k] = 1;
							}
							border = !border;
						}
						break;
				}
				prevc = s.at(k);
				if (k == c-1) {
					if (prev[k] == 1 || prev[k] == 3) {
						bexit = true;
					}
				}
			}
			board.push_back(prev);

				if (debug) {
				cout << endl;
				}
			if (j == r-1) {
				for (int k=0; k<c; k++) {
					if (prev[k] == 1 || prev[k] == 2) {
						bexit = true;
						break;
					}
				}
			}
		}
		if (bexit) {
			cout << "Impossible" << endl;
			if (debug)	print_board(board);
		} else {
			print_board(board);
		}
	}

}

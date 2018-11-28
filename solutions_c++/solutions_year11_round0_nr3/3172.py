#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	freopen("C-large.in","r",stdin);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		long long sum = 0;
		long long min = 1000000000;
		long long xorr = 0;
		int n;
		cin >> n;
		long long a;
		for (int i = 0; i < n; ++i) {
			cin >> a;
			if (a < min) {
				min = a;
			}
			xorr ^= a;
			sum += a;
		}
		cout << "Case #" << t + 1 << ": ";
		if (xorr != 0) {
			cout << "NO" << endl;
		}
		else {
			cout << sum - min << endl;
		}
	}
	return 0;
}
//
//#include <iostream>
//#include <string>
//#include <vector>
//#include <set>
//#include <stack>
//
//using namespace std;
//
//vector<char> st;
//vector<set<char> > oppo;
//vector<vector<char> > form;
//vector<int> used;
//
//void add(char c) {
//	if (st.empty()) {
//		st.push_back(c);
//		used[c - 'A']++;
//	}
//	else {
//		if (form[c - 'A'][st.back() - 'A'] != 'n') {
//			char prev = st.back();
//			st.pop_back();
//			used[prev]--;
//			add(form[c - 'A'][prev - 'A']);
//		}
//		else {
//			for (set<char>::iterator it = oppo[c - 'A'].begin(); it != oppo[c - 'A'].end(); ++it) {
//				if (used[*it]) {
//					used.assign(26, 0);
//					st.resize(0);
//					return;
//				}
//			}
//			st.push_back(c);
//			used[c - 'A']++;
//		}
//	}
//}
//
//int main() {
//	int T;
//	cin >> T;
//	for (int t = 0; t < T; ++t){
//		form.assign(26, vector<char>(26, 'n'));
//		oppo.assign(26, set<char>());
//		st.resize(0);
//		used.assign(26, 0);
//		int C;
//		cin >> C;
//		string str;
//		for (int j = 0; j < C; ++j) {
//			cin >> str;
//			form[str[0] - 'A'][str[1] - 'A'] = form[str[1] - 'A'][str[0] - 'A'] = str[2];
//		}
//		int D;
//		cin >> D;
//		for (int j = 0; j < D; ++j) {
//			cin >> str;
//			oppo[str[0] - 'A'].insert(str[1] - 'A');
//			oppo[str[1] - 'A'].insert(str[0] - 'A');
//		}
//		int n;
//		cin >> n >> str;
//		for (int i = 0; i < n; ++i) {
//			add(str[i]);
//		}
//		cout << "Case #" << t + 1 << ": [";
//		for (int i = 0; i < st.size(); ++i) {
//			if (i)
//				cout << ", ";
//			cout << st[i];
//		}
//		cout << "]" << endl;
//	}
//}

//#include <iostream>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//int advance(int from, int to) {
//	if (to > from) {
//		return from + 1;
//	}
//	else {
//		return from - 1;
//	}
//}
//
//int main() {
//	int T;
//	cin >> T;
//	string str;
//	for (int t = 0; t < T; ++t) {
//		int n;
//		cin >> n;
//		vector<pair<int, int> > orange(0);
//		vector<pair<int, int> > blue(0);
//		for (int i = 0; i < n; ++i) {
//			cin >> str;
//			int b;
//			cin >> b;
//			if (str[0] == 'O')
//				orange.push_back(make_pair(b, i));
//			else
//				blue.push_back(make_pair(b, i));
//		}
//		int orange_cell = 1;
//		int blue_cell = 1;
//		int orange_order = 0;
//		int blue_order = 0;
//		int timer = 0;
//		int turn = 0;
//		while(turn < n) {//((orange_order < orange.size()) || (blue_order < blue.size())) {
//			bool ob = (orange_order < orange.size()) && (orange_cell == orange[orange_order].first);
//			bool bb = (blue_order < blue.size()) && (blue_cell == blue[blue_order].first);
//
//			if (ob && !bb) {
//				if (turn == orange[orange_order].second) {
//					++orange_order;
//					++turn;
//				}
//				if (blue_order < blue.size())
//					blue_cell = advance(blue_cell, blue[blue_order].first);
//			}
//			else if (!ob && bb) {
//				if (turn == blue[blue_order].second) {
//					++blue_order;
//					++turn;
//				}
//				if (orange_order < orange.size())
//					orange_cell = advance(orange_cell, orange[orange_order].first);
//			}
//			else if (ob && bb) {
//				if (orange[orange_order].second == turn) {
//					++orange_order;
//					++turn;
//				}
//				else {
//					++blue_order;
//					++turn;
//				}
//			}
//			else {
//				if (orange_order < orange.size())
//					orange_cell = advance(orange_cell, orange[orange_order].first);
//				if (blue_order < blue.size())
//					blue_cell = advance(blue_cell, blue[blue_order].first);
//			}
//
//			++timer;
//		}
//
//		cout << "Case #" << t + 1 << ": " << timer << endl;
//	}
//}

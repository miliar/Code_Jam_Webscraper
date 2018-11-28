#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>

using namespace std;

int func(int R, vector<int> X1, vector<int> Y1, vector<int> X2, vector<int> Y2) {
	set<pair<int,int> > hoge;
	for (int i = 0; i < R; ++ i) {
		for (int x = X1[i]; x <= X2[i]; ++ x) {
			for (int y = Y1[i]; y <= Y2[i]; ++ y) {
				hoge.insert(make_pair(x,y));
			}
		}
	}
	int t = 0;
	while (!hoge.empty()) {
		set<pair<int,int> > piyo;
		set<pair<int,int> > fuga;
		for (set<pair<int,int> >::iterator i = hoge.begin(); i != hoge.end(); ++ i) {
			int x = i->first;
			int y = i->second;
			if (hoge.find(make_pair(x-1,y)) != hoge.end() || hoge.find(make_pair(x,y-1)) != hoge.end()) {
				piyo.insert(make_pair(x, y));
			}
			if (hoge.find(make_pair(x+1,y)) == hoge.end()) fuga.insert(make_pair(x+1,y));
			if (hoge.find(make_pair(x,y+1)) == hoge.end()) fuga.insert(make_pair(x,y+1));
		}
		for (set<pair<int,int> >::iterator i = fuga.begin(); i != fuga.end(); ++ i) {
			int x = i->first;
			int y = i->second;
			if (hoge.find(make_pair(x-1,y)) != hoge.end() && hoge.find(make_pair(x,y-1)) != hoge.end()) {
				piyo.insert(make_pair(x, y));
			}
		}
		hoge.swap(piyo);
		++ t;
	}
	return t;
}

int main() {
	int C;
	cin >> C;
	for (int i = 1; i <= C; ++ i) {
		int R;
		cin >> R;
		vector<int> X1(R), Y1(R), X2(R), Y2(R);
		for (int j = 0; j < R; ++ j) {
			cin >> X1[j] >> Y1[j] >> X2[j] >> Y2[j];
		}
		cout << "Case #" << i << ": " << func(R, X1, Y1, X2, Y2) << endl;
	}
}

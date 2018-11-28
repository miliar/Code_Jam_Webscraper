#include <iostream>
#include <vector>

using namespace std;

vector <pair<int, int> > o, b;

int main() {
	int test;
	cin >> test;
	for (int itest = 1; itest <= test; itest++) {
		int n;
		cin >> n;
		o.clear();
		b.clear();
		for (int i = 0; i < n; i++) {
			char c;
			int k;
			cin >> c >> k;
			if (c == 'O') o.push_back(make_pair(i, k)); 
			else b.push_back(make_pair(i, k));
		}
		int co = 0;
		int cb = 0;
		int poso = 1;
		int posb = 1;
		int goal = 0;
		int t = 0;
		while (co < o.size() && cb < b.size()) {
			bool ig = false;
			if (poso < o[co].second) poso++; else
			if (poso > o[co].second) poso--; else
			if (goal == o[co].first) co++, ig=true;
			if (posb < b[cb].second) posb++; else
			if (posb > b[cb].second) posb--; else
			if (goal == b[cb].first) cb++, ig=true;
			if (ig) goal++;
			t++;
		}
		while (co < o.size()) {
			if (poso < o[co].second) poso++; else
			if (poso > o[co].second) poso--; else
			if (goal == o[co].first) co++, goal++;
			t++;
		}
		while (cb < b.size()) {
			if (posb < b[cb].second) posb++; else
			if (posb > b[cb].second) posb--; else
			if (goal == b[cb].first) cb++, goal++;
			t++;
		}
		
		cout << "Case #" << itest << ": " << t << endl;
	}
	return 0;
}

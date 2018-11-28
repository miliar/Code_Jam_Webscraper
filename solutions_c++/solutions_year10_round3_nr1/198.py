#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <set>
#include <sstream>
#include <map>

using namespace std;

int main() {
	int T; cin >> T;
	for (int t = 0; t < T; t++) {
		int N; cin >> N;
		vector<pair<int,int> > vec;
		for (int i = 0; i < N; i++) {
			int a, b; cin >> a >> b;
			vec.push_back(make_pair(a,b));
		}
		sort(vec.begin(),vec.end());
		int tot = 0;
		for (int i = 0; i < vec.size(); i++) {
			for (int j = i+1; j < vec.size(); j++) {
				if (vec[j].second < vec[i].second) tot++;
			}
		}
		cout << "Case #" << (t+1) << ": " << tot << "\n";
	}
	return 0;
}
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int max[31] = {0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10};
	bool surp[31] = {false,false,true,true,false,true,true,false,true,true,
					 false,true,true,false,true,true,false,true,true,false,
					 true,true,false,true,true,false,true,true,false,false,
					 false};
	int cases;
	cin >> cases;
	for (int caseno = 1; caseno <= cases; caseno++) {
		cout << "Case #" << caseno << ": ";
		int n,s,p,ti,ans;
		vector <int> scores;
		cin >> n >> s >> p;
		for (int i = 0; i < n; i++) {
			cin >> ti;
			scores.push_back(ti);
		}
		sort(scores.begin(), scores.end(), greater<int>());
		ans = 0;
		for (int i = 0 ; i < scores.size(); i++) {
			int x = max[scores[i]];
			if (x < p-1)
				break;
			if (x >= p) {
				ans++;
			} else if (s > 0 && surp[scores[i]] && x+1 >= p) {
				ans++;
				s--;
			}
		}
		cout << ans << endl;
	}
}
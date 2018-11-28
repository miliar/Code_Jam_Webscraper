#include <iostream>
#include <map>
#include <vector>
#include <utility>

using namespace std;

typedef pair<int,int> vine;

bool solve(vector<vine>& vines, int D, int idx, int radius) {
	//cerr << idx << " " << vines.size() << endl;
	int x = vines[idx].first;
	if (x+radius>=D)
		return true;

	bool result = false;
	for (int i=vines.size()-1; i>idx; i--) {
		int ox = vines[i].first;
		int ol = vines[i].second;
		int dx = ox - x;
		if (radius >= dx) {
			//cerr << x << " " << radius << " " << vines[i].first << endl;
			if (solve(vines,D,i,min(ol,dx))) {
				return true;
			}
		} 
	}
	return result;
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++) {
		int N, D;
		cin >> N;
		vector<vine> vines;
		for (int j=0; j<N; j++) {
			int d, I;
			cin >> d >> I;
			vine v(d,I);
			vines.push_back(v);
		}
		cin >> D;
		string result;
		if (solve(vines, D, 0, vines[0].first))
			result = "YES";
		else
			result = "NO";
		cout << "Case #" << i+1 << ": " << result << endl;
		
	}
}

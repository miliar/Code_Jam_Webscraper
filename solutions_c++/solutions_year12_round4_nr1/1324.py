//#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <map>
using namespace std;

ifstream cin("A-small.in");
ofstream cout("A-small.out");


vector <pair<int, int> > V;
int D;
map <pair<int, int>, int> M;

int rec (int ind, int len) {
	pair<int, int> pp = make_pair(ind, len);
	if (M.count(pp)) return M[pp];
	if (ind==V.size()) return 0;
	if (V[ind].first+len >= D) return 1;
	int ans = 0;
	for (int i=ind+1; i<V.size() && V[i].first<=V[ind].first+len; i++) {
		ans = max(ans, rec(i,min(V[i].first-V[ind].first, V[i].second)));
	}
	M[pp] = ans;
	return ans;
}

int main () {
	int T; cin >> T >> ws;
	for (int t=0; t<T; t++) {
		int N; cin>>N;
		V.clear(); M.clear();
		for (int i=0; i<N; i++) {
			int tmp1, tmp2;
			cin >> tmp1 >> tmp2;
			V.push_back(make_pair(tmp1,tmp2));
		}
		cin>>D;
		cout << "Case #" << t+1 << ": ";
		if (rec(0, V[0].first))
			cout << "YES";
		else cout << "NO";
		cout << endl;
	}
	return 0;
}

#include<iostream>
#include<cstdlib>
#include<vector>
#include<map>
#include<set>
#include<string>
#include<sstream> 

using namespace std;

map<string, int> mem;

int value(vector<int> & candies, string & pile, int pos, int sa, int sb, int va1, int vb1, int va2, int vb2) {
	if (pos > candies.size() - 1) 
		if (sa > 0 && sb > 0 && va2 == vb2) return max(va1, vb1);	
		else return -1;

	int best = -1;

	best = max(value(candies, pile, pos + 1, sa , sb , va1, vb1, va2, vb2), best);
	pile[pos] = 'B';
	best = max(value(candies, pile, pos + 1, sa - 1, sb + 1, va1 - candies[pos], vb1 + candies[pos], va2 ^ candies[pos], vb2 ^ candies[pos]), best);

	return best;
}

int solve() {
	int n; cin >> n;
	vector<int> candies;
	string pile;
	mem.clear();
	int va1 = 0, va2 = 0;
	for (int i = 0; i < n; i++) {
		int c; cin >> c;
		candies.push_back(c);
		va1 += c; va2 ^= c;
		pile += "A";
	}

	return value(candies, pile, 0, n, 0, va1, 0, va2, 0);
}

int main() {
	int tc; cin >> tc;

	for (int t = 1; t <= tc; t++) {
		int s = solve();
		if (s == -1) cout << "Case #" << t << ": NO" << endl;
		else cout << "Case #" << t << ": " << s << endl;
	}

	return 0;
}
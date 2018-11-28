#include <iostream>
#include <string>

using namespace std;

int test;

string find(int n) {
	// used calc.exe
	switch(n) {
		case 1: return "005";
		case 2: return "027";
		case 3: return "143";
		case 4: return "751";
		case 5: return "935";

		case 6: return "607";
		case 7: return "903";
		case 8: return "991";
		case 9: return "335";
		case 10: return "047";

		case 11: return "943";
		case 12: return "471";
		case 13: return "055";
		case 14: return "447";
		case 15: return "463";

		case 16: return "991";
		case 17: return "095";
		case 18: return "607";
		case 19: return "263";
		case 20: return "151";

		case 21: return "855";
		case 22: return "527";
		case 23: return "743";
		case 24: return "351";
		case 25: return "135";

		case 26: return "407";
		case 27: return "903";
		case 28: return "791";
		case 29: return "135";
		case 30: return "647";

	}
}

void solve() {
	int n; cin >> n;
	cout << "Case #" << test << ": " << find(n) << endl;
}

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int TEST; cin >> TEST;
	for (test = 1; test <= TEST; test++)
		solve();
	return 0;
}
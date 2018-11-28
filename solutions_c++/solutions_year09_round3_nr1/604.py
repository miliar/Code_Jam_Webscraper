#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>

#define FOR(i,a,b) for(int i=(a); i<(b); i++)

using namespace std;

int main() {
	int T;
	cin >> T;
	FOR(q,1,T+1) {
		string s;
		cin >> s;

		set<int> notUsed;
		FOR(i,0,100) notUsed.insert(i);

		int N = s.size();
		vector<int> out(N);
		map<char, int> mm;
		mm[s[0]] = 1;
		out[0] = 1;
		notUsed.erase(1);
		FOR(i,1,N) {
			int v = -1;
			if(mm.find(s[i]) == mm.end()) {
				v = *notUsed.begin();
				notUsed.erase(v);
				mm[s[i]] = v;
			}
			else {
				v = mm[s[i]];
			}

			out[i] = v;
		}

		int base = 100 - notUsed.size();
		if(base == 1) base = 2;

		unsigned long long ret = 0;
		FOR(i,0,N) {
			ret = ret * base + out[i];
		}
		cout << "Case #" << q << ": " << ret << endl;
	}
	return 0;
}
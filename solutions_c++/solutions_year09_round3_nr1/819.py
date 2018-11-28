#include <iostream>
#include <map>
#include <string>
using namespace std;


int main(int argc, char** argv) {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		typedef map<char, int> cdm_t;
		cdm_t cdm; // char digit map
		string s;
		cin >> s;
		size_t slen = s.size();
		for (size_t j = 0; j < slen; ++j) {
			char ch = s[j];
			cdm_t::iterator it = cdm.find(ch);
			if (it == cdm.end()) {
				if (cdm.size() == 0) {
					cdm[ch] = 1;
				} else if (cdm.size() == 1) {
					cdm[ch] = 0;
				} else {
					cdm[ch] = cdm.size();
				}
			}
		}
		for (cdm_t::iterator it = cdm.begin(), end = cdm.end(); it != end; ++it) {
			cerr << it->first << ", " << it->second << endl;
		}
		size_t base = cdm.size();
		if (base == 1) { base = 2; }
		long long ans = 0;
		for (size_t j = 0; j < slen; ++j) {
			ans = cdm[s[j]] + ans * base;
			cerr << ans << endl;
		}
		cout << "Case #" << (i + 1) << ": " << ans << endl;
	}
	return 0;
}

//zig
// 012
// 931
//  92
// 11001001
// 1+8+64+128=>201


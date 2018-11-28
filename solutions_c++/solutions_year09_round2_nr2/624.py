#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

string solve() {
	string num; cin >> num;

	vector<char> chrs;

	int nd[10];
	for (int i = 0; i < 10; i++) nd[i] = 0;

	for (int i = 0; i < num.length(); i++) {
		chrs.push_back(num[i]);
		if (num[i]!='0') {
			nd[num[i]-'0']++;		
		}	
	}

	if (!next_permutation(chrs.begin(), chrs.end())) {
		if (chrs[0] == '0') {
			for (int i = 0; i < chrs.size(); i++) if (chrs[i] != '0') {
				chrs[0] = chrs[i];
				chrs[i] = '0';
				break;
			}
		}
		vector<char>::iterator it = chrs.begin(); it++;
		chrs.insert(it, '0');
	}

	string ret = "";
	for (int i = 0; i < chrs.size(); i++) {
		ret += chrs[i];
	}

	return ret;
}

int main() {
	int t; cin >> t;
	for (int i = 1; i <= t; i++)
		cout << "Case #" << i << ": " << solve() << endl;
}

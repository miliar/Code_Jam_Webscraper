#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

ifstream fin("input");
ofstream fout("output");

int find_ans(string s, string dic_str, const vector<string> &dic, const vector<bool> &exist, const vector< vector<bool> > &ex_word)
{
	vector<bool> is_opened(dic_str.length(), false);
	int res = 0;
	vector<char> forbid;
	for (unsigned i = 0; i < s.length(); i++) {
		if (!exist[s[i] - 'a']) continue;
		for (unsigned j = 0; j < dic.size(); j++) {
			if (ex_word[j][s[i] - 'a'] && dic_str.length() == dic[j].length()) {
				bool can = true;
				for (unsigned r = 0; r < dic[j].length(); r++) {
					if (is_opened[r] && dic[j][r] != dic_str[r]) {
						can = false;
						break;
					}
				}
				for (unsigned r = 0; r < forbid.size(); r++) {
					if (ex_word[j][forbid[r] - 'a']) {
						can = false;
						break;
					}
				}
				if (can) {
					bool was_open = false;
					for (unsigned r = 0; r < dic_str.length(); r++) {
						if (dic_str[r] == s[i]) {
							is_opened[r] = true;
							was_open = true;
						}
					}
					if (!was_open) {
						res++;
						forbid.push_back(s[i]);
					}
					break;
				}
			}
		}
	}
	return res;
}

void solve()
{
	int n, k;
	fin >> n >> k;
	vector<string> dic(n);
	vector<bool> exist(26, false);
	vector< vector<bool> > ex_word(n, vector<bool> (26, false));
	for (int i = 0; i < n; i++) {
		string s;
		fin >> s;
		dic[i] = s;
		for (unsigned j = 0; j < s.length(); j++) {
			exist[s[j] - 'a'] = true;
			ex_word[i][s[j] - 'a'] = true;
		}
	}
	for (int j = 0; j < k; j++) {
		string t;
		fin >> t;
		string ans;
		int max_qnt = -1;
		for (unsigned i = 0; i < dic.size(); i++) {
			int qnt = find_ans(t, dic[i], dic, exist, ex_word);
			if (qnt > max_qnt) {
				max_qnt = qnt;
				ans = dic[i];
			}
		}
		fout << ans << ' ';
	}
}

int main()
{
	int t;
	fin >> t;
	for (int i = 0; i < t; i++) {
		fout << "Case #" << i + 1 << ": ";
		solve();
		fout << endl;
	}
	return 0;
}

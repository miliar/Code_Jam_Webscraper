#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <utility>
#include <algorithm>
#include <string>
using namespace std;
string print_list(vector<char> const & v) {
	string ret = "[";
	if (v.size() > 0) ret += v[0];
	for (size_t i = 1, ilen = v.size(); i < ilen; ++i)
		ret = ret + ", " + v[i];
	return ret + "]";
}
int main() {
	ifstream cin("test.txt");
	ofstream cout("out.txt");
	int tests; cin >> tests;
	for (int test = 0; test < tests; ++test) {
		int C; cin >> C;
		vector<string> nonbase(2*C);
		for (int i = 0; i < C; ++i) {
			string s; cin >> s;
			nonbase[i] = s;
			swap(s[0], s[1]);
			nonbase[i+C] = s;
		}
		int D; cin >> D;
		vector<string> opposed(2*D);
		for (int i = 0; i < D; ++i) {
			string s; cin >> s;
			opposed[i] = s;
			swap(s[0], s[1]);
			opposed[i+D] = s;
		}
		int N; cin >> N;
		string s; cin >> s;
		vector<char> ret;
		for (int i = 0; i < N; ++i) {
			ret.push_back(s[i]);
			//bool f = false;
			for (int j = 0; j < 2*C; ++j) {
				if (ret.size() >= 2 && ret.back() == nonbase[j][0] && ret[ret.size()-2] == nonbase[j][1]) {
					ret.pop_back();
					ret.back() = nonbase[j][2];
					//f = true;
					break;
				}
			}
			for (int j = 0; j < 2*D; ++j) { 
				if (opposed[j][0] == ret.back()) {
					for (int k = 0, klen = ret.size()-1; k < klen; ++k) {
						if (opposed[j][1] == ret[k]) {
							ret.clear();
							goto break2;
						}
					}
				}
			}
			break2:;
		}
		cout << "Case #" << (test + 1) << ": " << print_list(ret) << endl;
	}
	//system("pause");
}
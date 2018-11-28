#include <iostream>
#include <fstream>
#include <map>
using namespace std;

map<string, char> com;
map<string, bool> del;

int main() {
	int t, c, d, n;
	string s, tmp, dummy;
	string ans;
	
	ifstream fin("input_b.txt");
	ofstream fout("ans_b.txt");
	
	fin >> t;
	for (int x = 1; x <= t; x++) {
		ans = "";
		com.clear();
		del.clear();
		fin >> c;
		for (int i = 0; i < c; i++) {
			fin >> tmp;
			com[tmp.substr(0, 2)] = tmp[2];
			dummy = "";
			dummy += tmp[1];
			dummy += tmp[0];
			com[dummy] = tmp[2];
		}
		fin >> d;
		for (int i = 0; i < d; i++) {
			fin >> tmp;
			del[tmp] = true;
			dummy = "";
			dummy += tmp[1];
			dummy += tmp[0];
			del[dummy] = true;
		}
		fin >> n;
		fin >> s;
		for (int i = 0; i < n; i++) {
			ans += s[i];
			if (ans.length() > 1) {
				dummy = "";
				dummy += ans[ans.length()-1];
				dummy += ans[ans.length()-2];
				if (com[dummy]) {
					ans.erase(ans.length()-2, 2);
					ans += com[dummy];
				}
				else {
					for (int j = ans.length()-2; j >= 0; j--) {
						dummy = "";
						dummy += ans[j];
						dummy += ans[ans.length()-1];
						if (del[dummy]) {
							ans = "";
							break;
						}
					}
				}
			}
		}
		
		fout << "Case #" << x << ": [";
		for (int i = 0; i < ans.length(); i++) {
			if (i == 0)
				fout << ans[0];
			else
				fout << ", " << ans[i];
		}
		fout << "]\n";
	}
}

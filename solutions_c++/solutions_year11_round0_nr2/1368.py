#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool opp[222][222];
char com[222][222];
string s;
string p;

int main() {
	int test;
	cin >> test;
	for (int itest = 1; itest <= test; itest++) {
		memset(com, 0, sizeof(com));
		memset(opp, false, sizeof(opp));
		int c, d, n;
		cin >> c;
		for (int i = 0; i < c; i++) {
			string tmp;
			cin >> tmp;
			com[tmp[0]][tmp[1]] = tmp[2];
			com[tmp[1]][tmp[0]] = tmp[2];
		}
		cin >> d;
		for (int i = 0; i < d; i++) {
			string tmp;
			cin >> tmp;
			opp[tmp[0]][tmp[1]] = true;			
			opp[tmp[1]][tmp[0]] = true;			
		}
		cin >> n;
		cin >> s;
		p = "";
		for (int i = 0; i < s.size(); i++) {
			p = p + s[i];
			//cout << p << endl;
			if (p.size() >= 2 && com[p[p.size() - 1]][p[p.size() - 2]] != 0) {
				char c = com[p[p.size() - 1]][p[p.size() - 2]];
				p.erase(p.begin() + p.size() - 2, p.end());
				p = p + c;
			}
			
			for (int u = 0; u < p.size() - 1; u++) 
			for (int v = u + 1; v < p.size(); v++) if (opp[p[u]][p[v]]) {
				p = "";
				goto endd;
			}
			endd:{}
		}
		cout << "Case #" << itest << ": [";
		for (int i = 0; i < p.size(); i++) {
			if (i > 0) cout << ", ";
			cout << p[i];
		}
		cout << "]" << endl;		
	}
	return 0;
}

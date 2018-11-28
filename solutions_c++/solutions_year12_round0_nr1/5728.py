#include <iostream>
#include <vector>
#include <string>
#include <cstdio>

using namespace std;

int main() {

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	vector<pair<string, string> >v(3);
	v[0] = make_pair("ejp mysljylc kd kxveddknmc re jsicpdrysiqz", "our language is impossible to understandzq");
	v[1] = make_pair("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	v[2] = make_pair("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
	int T;
	string S, G;
	cin >> T;
	getline(cin, G);
	bool flag = false;
	for(int n = 0; n < T; n++) {
		G = "";
		getline(cin, S);

		for(unsigned int i = 0; i < S.size(); i++) {
			flag = false;

			if(S[i] == ' ') {
				G += ' ';
				continue;
			}

			for(unsigned int k = 0; k < v.size(); k++) {

				for(unsigned int q = 0; q < v[k].first.size(); q++) {

					if(v[k].first[q] == S[i]) {
						G += v[k].second[q];
						flag = true;
						break;
					}
				}
				if(flag) {
					break;
				}
			}

		}
		cout << "Case #" << n + 1 << ": " << G << endl;
	}



	return 0;
}

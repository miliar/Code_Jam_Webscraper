#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <fstream>
using namespace std;

#ifdef WIN32
//ifstream in("A-small.in");
ifstream in("A-large.in");
#define cin in
//ofstream out("A-small.out");
ofstream out("A-large.out");
#define cout out
#endif

int main()
{
	int l, d, n;
	vector<string> dict;
	string w;
	cin >> l >> d >> n;
	for (int i = 0; i < d; ++i) {
		cin >> w;
		dict.push_back(w);
	}

	for (int ca = 1; ca <= n; ++ca) {
		cin >> w;
		set <char> pos[15];
		for (int i = 0, j = 0; i < w.size(); ++j, ++i) {
			if (w[i] == '(') {
				for (++i; w[i] != ')'; ++i) {
					pos[j].insert(w[i]);
				}
			} else {
				pos[j].insert(w[i]);
			}
		}

		int res = 0;
		for (int i = 0, fl, j; i < d; ++i) {
			for (j = 0, fl = 1; fl && j < l; ++j) {
				if (pos[j].find(dict[i][j]) == pos[j].end()) {
					fl = 0;
				}
			}
			res += fl;
		}

		cout << "Case #" << ca << ": " << res << endl;
	}

	return 0;
}

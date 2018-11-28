#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main() {

	ifstream in("B-small-attempt0.in");
	ofstream out("out.txt");

	int t;
	in >> t;
	for (int tc = 1; tc <= t; ++tc) {
		int n, m;
		in >> n >> m;
		vector<string> v(n, "");
		string s;
		for (int i = 0; i < n; ++i) 
			in >> v[i];

		out << "Case #" << tc << ":";

		for (int i = 0; i < m; ++i) {
			in >> s;
			string bestCand;
			int best = -1;
			for (int j = 0; j < n; ++j) {
				string cand = v[j];
				vector<string> vs;
				for (int k = 0; k < n; ++k) {
					if (v[k].size() == cand.size()) 
						vs.push_back(v[k]);
				}

				int numOfLoss = 0;

				for (int k = 0; k < s.size(); ++k) {
					bool isVal = false;
					for (int a = 0; a < vs.size(); ++a) {
						if (vs[a].find(s[k]) != string::npos) {
							isVal = true;
							break;
						}
					}
					if (!isVal)
						continue;

					bool inCand = (cand.find(s[k]) != string::npos);
					vector<string> vss;

					if (inCand) {
						for (int m = 0; m < vs.size(); ++m) {
							bool isR = true;
							for(int b = 0; b < cand.size(); ++b) {
								if ((cand[b] == s[k] || vs[m][b] == s[k]) && cand[b] != vs[m][b]) {
									isR = false;
									break;
								}
							}

							if (isR) {
								vss.push_back(vs[m]);
							}
						}
					}
					else {
						++ numOfLoss;
						for (int m = 0; m < vs.size(); ++m) {
							if (vs[m].find(s[k]) == string::npos)
								vss.push_back(vs[m]);
						}
					}

					vs = vss;
				}

				if (numOfLoss > best) {
					best = numOfLoss;
					bestCand = cand;
				}
			}

			out<<" "<<bestCand;
		}
		out<<endl;
	}
	return 0;
}
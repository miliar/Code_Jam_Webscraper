#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <string>
#include <sstream>
#include <vector>
#include <set>
using namespace std;

string getnextline() {
	char buffer[100];
	gets(buffer);
	return string(buffer);
}

int main(void) {
	int nTests;
	scanf("%d", &nTests);
	for (int testNo = 1; testNo <= nTests; testNo++) {
		int lines;
		scanf("%d", &lines);
		getnextline();
		string str;
		while (lines--) {
			str += getnextline();
			str += " ";
		}
		for (unsigned pos=0; string::npos != (pos = str.find_first_of("()", pos)); pos+=3) {
			str.replace(pos, 1, " "+str.substr(pos, 1)+" ");
		}
		int N;
		scanf("%d", &N);
		vector< set<string> > features(N);
		vector<double> res(N, 1.0);
		for (int i = 0; i < N; i++) {
			int numFeatures;
			scanf("%*s%d", &numFeatures);
			while (numFeatures--) {
				char featurestr[100];
				scanf("%s", featurestr);
				features[i].insert(featurestr);
			}
		}
		vector<int> d(N);
		istringstream iss(str);
		int cd = 0;
		for (string token; iss >> token; ) {
			if (token == "(") {
				double val;
				iss >> val;
				for (int i = 0; i < N; i++) {
					if (d[i] != cd)
						continue;
					res[i] *= val;
				}
				++cd;
			} else if (token == ")") {
				--cd;
				for (int i = 0; i < N; i++) {
					if (d[i] == cd-1)
						d[i]++;
					else if (d[i] == cd) {
						d[i] = -1;
					}
				}
			} else {
				for (int i = 0; i < N; i++) {
					if (d[i] != cd-1)
						continue;
					if (features[i].find(token) != features[i].end())
						++d[i];
				}
			}
		}
		printf("Case #%d:\n", testNo);
		for (int i = 0; i < N; i++) {
			printf("%.7lf\n", res[i]);
		}
	}
	return 0;
}


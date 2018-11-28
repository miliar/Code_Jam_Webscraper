#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;

vector<string> tokenize(string s, string delim=" ") {
	vector<string> res;
	while (s.size()) {
		int i = s.find(delim);
		if (i == -1) {
			res.push_back(s);
			s = "";
			break;
		}
		string t = s.substr(0, i);
		if (t.length())	res.push_back(t);
		s = s.substr(i + delim.length());
	}
	return res;
}

#define WITHIN(i,mini,maxi) (i >= mini && i <= maxi)

vector<int> notbirdW;
vector<int> notbirdH;
int main() {
	int NTc;
	scanf("%d", &NTc);
	int i, j, k, m, n, h, w;
	char buf[1024];
	for (int tc = 0; tc < NTc; tc++) {
		printf("Case #%d:\n", tc+1);
		notbirdW.clear();
		notbirdH.clear();

		int H, W, N;
		scanf("%d", &N);
		char buf[1024];
		int minH = 10000000, maxH = 0;
		int minW = 10000000, maxW = 0;
		for (i = 0; i < N; i++) {
			scanf("%d %d %s", &h, &w, buf);
			if (strcmp(buf, "BIRD") == 0) {
				if (h < minH) minH = h;
				if (h > maxH) maxH = h;
				if (w < minW) minW = w;
				if (w > maxW) maxW = w;
			} else {
				scanf("%s", buf);
				notbirdW.push_back(w);
				notbirdH.push_back(h);
			}
		}
		int maxlowH_nb = 0, maxlowW_nb = 0;
		int minhiH_nb = 10000000, minhiW_nb = 10000000;

		N = notbirdW.size();
		for (i = 0; i < N; i++) {
			bool wvalid = WITHIN(notbirdW[i], minW, maxW);
			bool hvalid = WITHIN(notbirdH[i], minH, maxH);
			bool winvalid = notbirdW[i] <= maxlowW_nb || notbirdW[i] >= minhiW_nb;
			bool hinvalid = notbirdH[i] <= maxlowH_nb || notbirdH[i] >= minhiH_nb;

			if (wvalid && !hvalid) {
				if (notbirdH[i] < minH && notbirdH[i] > maxlowH_nb) {
					maxlowH_nb = notbirdH[i];
				}
				if (notbirdH[i] > maxH && notbirdH[i] < minhiH_nb) {
					minhiH_nb = notbirdH[i];
				}
			} else if (!wvalid && hvalid) {
				if (notbirdW[i] < minW && notbirdW[i] > maxlowW_nb) {
					maxlowW_nb = notbirdW[i];
				}
				if (notbirdW[i] > maxW && notbirdW[i] < minhiW_nb) {
					minhiW_nb = notbirdW[i];
				}
			}

		}
		//printf("BIRD W=%d-%d, H=%d-%d\n", minW, maxW, minH, maxH);
		//printf("NOTBIRD W<=%d W>=%d, H<=%d H>=%d\n", maxlowW_nb, minhiW_nb, maxlowH_nb, minhiH_nb);

		scanf("%d", &N);
		for (i = 0; i < N; i++) {
			scanf("%d %d", &h, &w);
			if (WITHIN(h, minH, maxH) && WITHIN(w, minW, maxW)) {
				printf("BIRD\n");
			} else if (h >= minhiH_nb || h <= maxlowH_nb) {
				printf("NOT BIRD\n");
			} else if (w >= minhiW_nb || w <= maxlowW_nb) {
				printf("NOT BIRD\n");
			} else {
				for (j = 0; j < notbirdW.size(); j++) {
					if (h == notbirdH[j] && w == notbirdW[j]) {
						printf("NOT BIRD\n");
						break;
					}

				}
				if (j == notbirdW.size()) {
					bool defnot = false;
					int newminH = minH;
					int newmaxH = maxH;
					int newminW = minW;
					int newmaxW = maxW;
					if (h > newmaxH) newmaxH = h;
					if (h < newminH) newminH = h;
					if (w > newmaxW) newmaxW = w;
					if (w < newminW) newminW = w;
					for (k = 0; k < notbirdW.size(); k++) {
						if (WITHIN(notbirdW[k], newminW, newmaxW) && WITHIN(notbirdH[k], newminH, newmaxH)) {
							defnot = true;
							break;
						}
					}
					if (defnot) {
						printf("NOT BIRD\n");
					} else {
						printf("UNKNOWN\n");
					}
				}
			}
		}
	}
	return 0;
}
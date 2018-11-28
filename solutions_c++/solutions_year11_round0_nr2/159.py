#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#define E(c) cerr<<#c
#define Eo(x) cerr<<#x<<" = "<<(x)<<endl

vector<string> trans, opp;
string all;
string str;

char buff[256];
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		trans.clear();
		opp.clear();
		int k;

		scanf("%d", &k);
		for (int i = 0; i<k; i++) {
			scanf("%s", buff);
			trans.push_back(buff);
		}

		scanf("%d", &k);
		for (int i = 0; i<k; i++) {
			scanf("%s", buff);
			opp.push_back(buff);
		}

		scanf("%d", &k);
		scanf("%s", buff);
		all = buff;

		str.clear();
		for (int i = 0; i<all.size(); i++) {
			str += all[i];

			if (str.size() >= 2) {
				char c1 = str[str.size() - 2];
				char c2 = str[str.size() - 1];
				string c12 = string() + c1 + c2;
				string c21 = string() + c2 + c1;
				for (int u = 0; u<trans.size(); u++)
					if (trans[u].substr(0, 2) == c12 || trans[u].substr(0, 2) == c21) {
						str = str.substr(0, str.size() - 2);
						str += trans[u][2];
						break;
					}
			}

			for (int j = 0; j<str.size()-1; j++) {
				char c1 = str[j];
				char c2 = str[str.size() - 1];
				string c12 = string() + c1 + c2;
				string c21 = string() + c2 + c1;
				for (int u = 0; u<opp.size(); u++)
					if (opp[u] == c12 || opp[u] == c21) {
						str.clear();
						break;
					}
				if (str.empty()) break;
			}
		}

		printf("Case #%d: ", tt);
		printf("[");
		for (int i = 0; i<str.size(); i++) {
			if (i) printf(", ");
			printf("%c", str[i]);
		}
		printf("]\n");
		fflush(stdout);
	}
	return 0;
}

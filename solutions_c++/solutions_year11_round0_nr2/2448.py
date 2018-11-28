#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define NMAX 128

map < pair<char,char>, char > comb;
map < char, set<char> > opp;
map < char,int > count;
vector <int> E;
int c, d, n;

int main() {
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		scanf("%d", &c);
		comb.clear();
		for (int i = 0; i < c; i++) {
			char str[4];
			scanf("%s", str);
			pair <char,char> p = make_pair(str[0], str[1]);
			pair <char,char> q = make_pair(str[1], str[0]);
			comb[p] = comb[q] = str[2];
		}
		scanf("%d", &d);
		opp.clear();
		for (int i = 0; i < d; i++) {
			char str[3];
			scanf("%s", str);
			opp[str[0]].insert(str[1]);
			opp[str[1]].insert(str[0]);
		}
		E.clear();
		count.clear();
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			char ch;
			scanf(" %c", &ch);
			if (E.size() > 0) {
				pair <char,char> p = make_pair(E[E.size()-1], ch);
				if (comb.find(p) != comb.end()) {
					count[E[E.size()-1]]--;
					E.pop_back();
					count[comb[p]]++;
					E.push_back(comb[p]);
					ch = comb[p];
					while (E.size() > 0) {
						pair <char,char> q = make_pair(E[E.size()-1], ch);
						if (comb.find(q) != comb.end()) {
							count[E[E.size()-1]]--;
							E.pop_back();
							count[comb[q]]++;
							E.push_back(comb[q]);
							ch = comb[q];
						} else {
							for (set<char>::iterator j = opp[ch].begin(); j != opp[ch].end(); j++) {
								if (count.count(*j) != 0 && count[*j] > 0) {
									E.clear();
									count.clear();
								}
							}
							break;
						}
					}
				} else {
					count[ch]++;
					E.push_back(ch);
					for (set<char>::iterator j = opp[ch].begin(); j != opp[ch].end(); j++) {
						if (count.count(*j) != 0 && count[*j] > 0) {
							E.clear();
							count.clear();
						}
					}
				}
			} else {
				count[ch]++;
				E.push_back(ch);
			}
		}
		printf("Case #%d: [", test);
		for (int i = 0; i < E.size(); i++) {
			printf("%s%c", (i == 0 ? "" : ", "), E[i]);
		}
		printf("]\n");
	}
	return 0;
}


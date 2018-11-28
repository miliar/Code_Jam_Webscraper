#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
//#include <map>
#include <vector>
#include <set>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = SIMPLE;
bool debug = false;

void init() {
}



set<int> filter(const set<int> &poss, const vector<string> &dict, const set<char> allowed, int dictpos) {
	set<int> ret;
	for(set<int>::const_iterator it = poss.begin(); it != poss.end(); ++it) {
		if(allowed.find(dict[*it][dictpos]) != allowed.end()) {
			ret.insert(*it);
		}
	}
	return ret;
}

int nsol(const vector<string> &dict, const string &word) {
	set<int> poss;
	for(int i = 0; i < (int) dict.size(); ++i) {
		poss.insert(i);
	}

	int dictpos = 0;

	for(string::const_iterator ch = word.begin(); ch != word.end(); ++ch) {
		set<char> allowed;

		if(*ch == '(') {
			++ch;
			while(*ch != ')') {
				assert(ch != word.end());
				allowed.insert(*ch);
				++ch;
			}
		} else {
			allowed.insert(*ch);
		}

		poss = filter(poss, dict, allowed, dictpos++);
	}

	return (int) poss.size();
}

bool solve(int P) {
	int L, D, N;
	if(!scanf("%d%d%d", &L, &D, &N) == 3)
		assert(!"Failed to read LDN");
	char buf[2000];

	vector<string> dict;
	for(int i = 0; i < D; ++i) {
		scanf("%s", buf);
		dict.push_back(buf);
	}

	for(int i = 0; i < N; ++i) {
		if(scanf("%s", buf) != 1)
			assert(!"Failed to read word");

		printf("Case #%d: %d\n", i+1, nsol(dict, buf));
	}
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}

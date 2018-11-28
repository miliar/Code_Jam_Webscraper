#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>

using namespace std;
#define dprintf debug && printf
#define F(x,y) for(typeof((y).begin()) x = (y).begin(); x != (y).end(); ++x) 
#define CHECKREAD(x, ...) if(scanf(__VA_ARGS__) != x) { fprintf(stderr, "Failed to read on %s, %d\n", __FILE__, __LINE__); exit(1); }


const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

bool solve(int P) {
	printf("Case #%d: ", P+1);

	int C, D, N;

	vector<map<char, char>  > transform(256);
	vector<vector<char>  > forbidden(256);

	CHECKREAD(1, "%d", &C);
	for(int i = 0; i < C; ++i) {
		char buf[20];
		CHECKREAD(1, "%5s", buf);
		assert(strlen(buf) == 3);
		transform[buf[0]][buf[1]] = buf[2];
		transform[buf[1]][buf[0]] = buf[2];
	}

	CHECKREAD(1, "%d", &D);
	for(int i = 0; i < D; ++i) {
		char buf[20];
		CHECKREAD(1, "%5s", buf);
		assert(strlen(buf) == 2);
		forbidden[buf[0]].push_back(buf[1]);
		forbidden[buf[1]].push_back(buf[0]);
	}

	CHECKREAD(1, "%d", &N);
	char keys[2000];
	assert(N < 2000);
	CHECKREAD(1, "%1000s", keys);
	assert((int) strlen(keys) == N);

	string magic = "";
	for(char *ch = keys; *ch; ++ch) {
		map<char, char> &tr = transform[*ch];
		if(!magic.empty() && tr.find(*magic.rbegin()) != tr.end()) {
			*magic.rbegin() = tr[*magic.rbegin()];
		} else {
			bool found = false;
			F(it, forbidden[*ch]) {
				if(magic.find(*it) != string::npos) {
					found = true;
					break;
				}
			}
			if(found) 
				magic = "";
			else
				magic.push_back(*ch);
		}
	}

	printf("[");
	F(it, magic) {
		if(it != magic.begin())
			printf(", ");
		printf("%c", *it);
	}
	printf("]\n");

	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}


#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
//#include <vector>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

bool solve(int P) {
	printf("Case #%d: ", P + 1);
	string str;
	cin >> str;
	while(*str.begin() == '0')
		str = str.substr(1);
	if(next_permutation(str.begin(), str.end())) {
		printf("%s\n", str.c_str());
	} else {
		str.push_back('0');
		sort(str.begin(), str.end());
		for(string::iterator it = str.begin(); it != str.end(); ++it) {
			if(*it != '0') {
				swap(*it, *str.begin());
				break;
			}
		}
		printf("%s\n", str.c_str());
	}
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}

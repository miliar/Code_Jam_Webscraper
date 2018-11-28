#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
//#include <string>
//#include <map>
//#include <vector>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

const char *target = "welcome to code jam";

int Nsol[20][5000];

int nsol(int m, int p, const char *str) {
	if(!str[p])
		return 0;

	if(!target[m])
		return 1;

	int &ret = Nsol[m][p];
	if(ret != -1)
		return ret;
	ret = 0;

	if(str[p] == target[m])
		ret += nsol(m+1, p+1, str);
	ret += nsol(m, p+1, str);
	ret %= 10000;
	return ret;
}

bool solve(int P) {
	char buf[2000];
	fgets(buf, sizeof(buf), stdin);
	memset(Nsol, -1, sizeof(Nsol));

	printf("Case #%d: %04d\n", P+1, nsol(0, 0, buf));
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  char buf[2000];
  fgets(buf, sizeof(buf), stdin);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}

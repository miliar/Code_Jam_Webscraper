#include <cassert>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <cstddef>
#include <cctype>
#include <cmath>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <numeric>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <list>
#include <string>
#include <functional>
#include <utility>
using namespace std;
typedef long long llint;
int const A = 26;
int const L = 100;
int mapping[A];
void doit() {
	FILE *in1 = fopen("a_in.txt", "r");
	FILE *in2 = fopen("a_out.txt", "r");
	int c1, c2;
	memset(mapping, -1, sizeof(mapping));
	mapping['z' - 'a'] = 'q' - 'a';
	mapping['q' - 'a'] = 'z' - 'a';
	while ((c1 = fgetc(in1)) != EOF) {
		c2 = fgetc(in2);
		if (!isalpha(c1)) {
			continue;
		}
		c1 -= 'a';
		c2 -= 'a';
		if (mapping[c1] == -1) {
			mapping[c1] = c2;
		} else {
			assert(mapping[c1] == c2);
		}
	}
	fclose(in1);
	fclose(in2);
	copy(mapping, mapping + A, ostream_iterator <int>(cerr, " "));
	cerr << endl;
}
int main() {
	doit();
	int tc;
	scanf("%d", &tc);
	getchar();
	for (int cc = 0; cc < tc; ++cc) {
		char buff[L + 10];
		fgets(buff, L + 5, stdin);
		printf("Case #%d: ", cc + 1);
		for (int i = 0; buff[i]; ++i) {
			if (isalpha(buff[i])) {
				putchar('a' + mapping[buff[i] - 'a']);
			} else {
				putchar(buff[i]);
			}
		}
	}
	return 0;
}

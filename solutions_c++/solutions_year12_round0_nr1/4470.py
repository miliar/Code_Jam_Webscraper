#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> pi;
typedef unsigned long long ull;

#define x first
#define y second
#define mp make_pair



void solution() {
	//char mapping[26] = {0};
	//char a[200] = {0};
	//char b[200] = {0};
	//gets(a);
	//gets(b);
	//int len = strlen(a);
	//for (int i = 0; i < len; ++i) {
	//	if (a[i] != ' ') {
	//		mapping[a[i] - 'a'] = b[i];
	//	}
	//}
	//for (int i = 0; i < 26; ++i) {
	//	printf("%c", mapping[i]);
	//}
	char mapping[] = "yhesocvxduiglbkrztnwjpfmaq";
	char buf[200] = {0};
	gets(buf);
	int len = strlen(buf);
	for (int i = 0; i < len; ++i) {
		if (buf[i] != ' ')
			putchar(mapping[buf[i] - 'a']);
		else
			putchar(' ');
	}
	puts("");
}

int main() {

	//freopen("in.in", "rt", stdin);
	//freopen("out.out", "wt", stdout);

	freopen("A-small.in", "rt", stdin);
	freopen("A-small.out", "wt", stdout);

	//freopen("A-large.in", "rt", stdin);
	//freopen("A-large.out", "wt", stdout);

	//freopen("B-small.in", "rt", stdin);
	//freopen("B-small.out", "wt", stdout);

	//freopen("B-large.in", "rt", stdin);
	//freopen("B-large.out", "wt", stdout);


	//freopen("C-small.in", "rt", stdin);
	//freopen("C-small.out", "wt", stdout);

	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);
	
	int t = 0;
	scanf("%d\n", &t);
	for (int tt = 0; tt < t; tt++) {
		printf("Case #%d: ", tt + 1);
		solution();
	}

	return 0;
}
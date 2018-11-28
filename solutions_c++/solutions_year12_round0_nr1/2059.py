#include <fstream>
#include <cstdio>
#include <cstring>

using namespace std;

ifstream in("a.in");
ofstream out("a.out");

char getLetter(char c) {
	if (c == 'a') return 'y';
	if (c == 'b') return 'h';
	if (c == 'c') return 'e';
	if (c == 'd') return 's';
	if (c == 'e') return 'o';
	if (c == 'f') return 'c';
	if (c == 'g') return 'v';
	if (c == 'h') return 'x';
	if (c == 'i') return 'd';
	if (c == 'j') return 'u';
	if (c == 'k') return 'i';
	if (c == 'l') return 'g';
	if (c == 'm') return 'l';
	if (c == 'n') return 'b';
	if (c == 'o') return 'k';
	if (c == 'p') return 'r';
	if (c == 'q') return 'z';
	if (c == 'r') return 't';
	if (c == 's') return 'n';
	if (c == 't') return 'w';
	if (c == 'u') return 'j';
	if (c == 'v') return 'p';
	if (c == 'w') return 'f';
	if (c == 'x') return 'm';
	if (c == 'y') return 'a';
	if (c == 'z') return 'q';
	return '2';
}

int main() {
	freopen("a.in", "r", stdin);

	int t;
	scanf("%d\n", &t);

	for (int i = 1; i <= t; ++i) {
		char str[200];
		gets(str);
		int len = strlen(str);

		out << "Case #" << i << ": ";

		for (int i = 0; i < len; ++i) {
			if (str[i] != ' ')
				str[i] = getLetter(str[i]);

			out << str[i];
		}

		out << "\n";
	}

	return 0;
}

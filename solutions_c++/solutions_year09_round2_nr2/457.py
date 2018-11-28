#include <stdio.h>
#include <algorithm>
#include <string>
using namespace std;

int main() {
	int T;
	scanf(" %d", &T);
	for (int _42=1; _42 <= T; _42++) {
		char buf[1000];
		scanf(" %s", buf);
		int X;
		sscanf(buf, " %d", &X);
		string s = string(buf);

		printf("Case #%d: ", _42);
		if (next_permutation(s.begin(), s.end())) {
			printf("%s\n", s.c_str());
		}
		else {
			sort(s.begin(), s.end());
			int p=0;
			while (s[p] == '0') p++;
			char ch = s[p];
			s[p] = '\0';
			printf("%c0%s%s\n", ch, s.c_str(), s.c_str()+p+1);
		}
	}

	return 0;
}

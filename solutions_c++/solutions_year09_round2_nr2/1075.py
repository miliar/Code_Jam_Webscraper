#include <stdio.h>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
	int t;
	char line[1000];
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &t);
	for (int t1 = 0; t1<t; t1++) {
		scanf("%s", line);
		string s= line, s2 = line;
		next_permutation(s.begin(), s.end());
		printf("Case #%d: ", t1+1);
		if (s <= s2) {
			if (s[0]!='0') {
				sprintf(line, "%s", s.c_str());
				printf("%c", line[0]);
				printf("0");
				for (int i=1; line[i]; i++)
					printf("%c", line[i]);
				puts("");
			}
			else {
				int t = strlen(line);
				int h=0;
				for (int i=0; i<t; i++)
					if (line[i] < line[h] && line[i] > '0' || line[h]=='0') h=i;
				int y=line[h];
				line[h] = line[0];
				line[0] = y;
				printf("%c", line[0]);
				printf("0");
				for (int i=1; i<t-1; i++)
					for (int j=i+1; j<t; j++)
						if (line[i] > line[j]) {
							int g = line[i];
							line[i] = line[j];
							line[j] = g;
						}
				for (int i=1; line[i]; i++)
					printf("%c", line[i]);
				puts("");
			}
		}
		else
			cout << s << endl;
	}
	return 0;
}


#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int d[500][500];

char w[100] = "welcome to code jam";
char s[501];

void Output() {
	for (int i = 0; i < strlen(w); ++i) {
		for (int j = 0; j < strlen(s); ++j) {
			cout << d[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

void Process() {
	int len = strlen(w);
	int slen = strlen(s);
	if (s[0] == 'w') {
		d[0][0] = 1;
	} else {
		d[0][0] = 0;
	}
	for (int i = 1; i < slen; ++i) {
		d[0][i] = d[0][i-1];
		if (s[i] == 'w') {
			d[0][i]++;
		}
	}
		
	for (int i = 1; i < len; ++i) {
		d[i][i-1] = 0;
		for (int j = i; j < slen; ++j) {
			if (s[j] == w[i]) {
			  d[i][j] = d[i-1][j-1] + d[i][j-1];
			} else {
				d[i][j] = d[i][j-1];
			}
			d[i][j] %= 10000;
		}
	}
	// Output();
	printf("%04d\n", d[len-1][slen-1]);
}

int main() {
	int n;
	char buf[100];
	gets(buf);
	sscanf(buf, "%d", &n);
	for (int i = 0; i < n; ++i) {
		gets(s);
		printf("Case #%d: ", i+1);
		Process();
	}
	return 0;
}

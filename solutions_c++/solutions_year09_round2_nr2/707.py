#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
using namespace std;

int cnt[11];

void go(char *a, char *b) {
	int res = next_permutation(a, a+strlen(a));
	if (res) {
		strcpy(b, a);
		b[strlen(a)] = '\0';
	}
	else {
		for (int i = 0; i < cnt[0]+1; i++) b[i+1] = '0';
		for (int i = 0; i < strlen(a)+1; ) {
			for (int j = 1; j <= 9; j++) {
				if (cnt[j]) {
					cnt[j]--;
					b[i] = j+'0';
					break;
				}
			}
			if (i == 0) i += cnt[0]+2;
			else i++;
		}
		b[strlen(a)+1] = '\0';
	}
}

int main() {
	FILE *fin = fopen("B.txt", "r");
	FILE *fout = fopen("B.out", "w");
	
	int numtests;
	fscanf(fin, "%d\n", &numtests);
	for (int i = 1; i <= numtests; i++) {
		char a[30], b[30];
		fscanf(fin, "%s\n", a);
		memset(cnt, 0, sizeof(cnt));
		for (int j = 0; j < strlen(a); j++) cnt[a[j]-'0']++;
		go(a, b);
		fprintf(fout, "Case #%d: %s\n", i, b);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}



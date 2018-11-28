#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <string>

using namespace std;

#define TRACE(x...) 
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)
#define forr(i, a, b) for(int i=a;i<b;i++)
#define MSET(a, b) memset(a, b, sizeof(a))

const int INF = 0x3f3f3f3f; const int NEGINF = 0xc0c0c0c0;
const double EPS = 1e-10;

int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

char bla[500];

int main() {
	TRACE(setbuf(stdout, NULL));
	int _42=1;
	int T;
	scanf(" %d", &T);
	while (T--) {
		scanf(" %s", bla);
		string s = bla;
		printf("Case #%d: ", _42++);
		if (next_permutation(s.begin(), s.end())) {
			printf("%s\n", s.c_str());
		}
		else {
			sort(s.begin(), s.end());
			int zeros=0;
			for (zeros=0;zeros<s.size();zeros++) {
				if (s[zeros] != '0') break;
			}
			printf("%c", s[zeros]);
			printf("0");
			for (int i=0;i<zeros;i++)
				printf("0");
			for (int i=zeros+1;i<s.size();i++) 
				printf("%c", s[i]);
			}
			printf("\n");
		}
	}
	return 0;
}

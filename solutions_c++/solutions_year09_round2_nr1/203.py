#include <stdio.h>
#include <string.h>
#include <string>
#include <set>
using namespace std;

int i,j,k,n,L,A;
char s[10000], ss[1000];
set<string> v;
double p;
int pos;

void go() {
	while (s[pos] != '(') pos++;
	pos++;
	double w = 0;
	while (s[pos] == ' ' || s[pos] == '\n') pos++;
	w = s[pos]-'0';
	pos++;
	if (s[pos] == '.') { 
		pos++; 
		double d = 1;
		while (s[pos] >= '0' && s[pos] <= '9') {
			d /= 10;
			w += (s[pos] - '0') * d;
			pos++;
		}
	}
	
	p *= w;

	while (s[pos] == ' ' || s[pos] == '\n') pos++;
	if (s[pos] == ')') return;

	i = 0;
	while (s[pos] != ' ' && s[pos] != '\n') {
		ss[i++] = s[pos];
		pos++;
	}
	ss[i] = '\0';
	if (v.find(ss) == v.end()) {
		// preskoc
		i = 0; j = 0;
		do {
			pos++;
			if (s[pos] == '(') { i++; j = 1; }
			if (s[pos] == ')') i--;
		} while (j == 0 || i > 0);
		go();
	} else {
		go();
		// preskoc
		i = 0; j = 0;
		do {
			pos++;
			if (s[pos] == '(') { i++; j = 1; }
			if (s[pos] == ')') i--;
		} while (j == 0 || i > 0);
	}
}

int main() {
	int test, ntest, i, j;
	scanf("%d", &ntest);
	for (test = 1; test <= ntest; test++) {
		printf("Case #%d:\n", test);
		scanf("%d%*c", &L);
		s[0] = '\0';
		for (i = 0; i < L; i++) {
			fgets(s+strlen(s), 10000, stdin);
		}
		scanf("%d%*c", &A);
		for (j = 0; j < A; j++) {
			scanf("%*s%d", &n);
			v.clear();
			for (i = 0; i < n; i++) {
				scanf("%s", ss);
				v.insert(ss);
			}
			p = 1;
			pos = 0;
			go();
			printf("%.10lf\n", p);
		}
	}
	return 0;
}

#include <iostream>
#include <fstream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int now;
double p[2000];
string tab[2000];
int n1[2000], n2[2000];
double nowp;
char have[200][100];

FILE *fin, *fout;

string nextlabel() {
	char c;
	string s = "";
	c = fgetc(fin);
	while (c == ' ' || c == '\n')
		c = fgetc(fin);
	s = c;
	if (c == '(' || c == ')')
		return s;
	while (1) {
		c = fgetc(fin);
		if ('a' <= c && c <= 'z')
			s = s + c;
		else
			break;
	}
	return s;
}

int process() {
	int k = now;
	string s = nextlabel();
	fscanf(fin, "%lf", &nowp);
	p[k] = nowp;

	s = nextlabel();
	if (s == ")")
		return k;
	tab[k] = s;
	now++;
	n1[k] = process();
	now++;
	n2[k] = process();
	
	s = nextlabel();

	return k;
}

int main() {

	fin = fopen("A-large.in", "r");
	fout = fopen("aout.txt", "w");

	int T, L, k, n;
	char cs[20];

	fscanf(fin, "%d", &T);
	for (int t = 1; t <= T; t++) {
		fprintf(fout, "Case #%d:\n", t);
		fscanf(fin, "%d", &L);
		memset(p, 0, sizeof(p));
		memset(tab, 0, sizeof(tab));
		memset(n1, 0, sizeof(n1));
		memset(n2, 0, sizeof(n2));
		now = 0;
		process();
		fscanf(fin, "%d", &n);
		string s;
		for (int i = 0; i < n; i++) {
			fscanf(fin, "%s %d", &cs, &k);
			double ans = 1;
			int now = 0;
			for (int j = 0; j < k; j++) {
				fscanf(fin, "%s", have[j]);
			}
			while (1) {
				ans *= p[now];
				if (n1[now] == 0)
					break;
				bool has = false;
				for (int j = 0; j < k; j++) {
					if (!strcmp(have[j], tab[now].c_str())) {
						has = true;
						break;
					}
				}
				if (has)
					now = n1[now];
				else
					now = n2[now];
			}
			fprintf(fout, "%.12lf\n", ans);
		}
	}

	return 0;
}

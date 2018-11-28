#include <cstdio>
#include <vector>
using namespace std;
const int maxN = 52;
int tab[maxN][maxN];
int tab1[maxN][maxN];
int main() {
	int t; scanf("%d", &t);
	for(int i = 1; i <= t; i++) {
		int n, kk; scanf("%d %d", &n, &kk);
		vector<int> rot[maxN];
		for(int j = 0; j < n; j++)
			for(int k = 0; k < n; k++) tab[j][k] = tab1[j][k] = 0;
		char c; scanf("%c", &c);
		bool a = false, b = false;
		for(int j = n-1; j >= 0; j--) {
			for(int k = 0; k < n; k++) {
				char c; scanf("%c", &c);
				if (c == '.') tab[j][k] = 0;
				if (c == 'R') { tab[j][k] = 1; rot[j].push_back(k); }
				if (c == 'B') { tab[j][k] = -1; rot[j].push_back(k); }
			}
			char c; scanf("%c", &c);
		}
/*		for(int j = n-1; j >= 0; j--) {
			for(int k = 0; k < n; k++){
				if (tab[j][k] == 0) printf(".");
				if (tab[j][k] == 1) printf("R");
				if (tab[j][k] == -1) printf("B"); }
			printf("\n");
		}
		printf("\n\n");
		for(int j = 0; j < n; j++) {
			for(int k = 0; k <  rot[j].size(); k++) {
				printf("%d ", rot[j][k]);
			}
			printf("\n");
		}
*/
		for(int j = 0; j < n; j++) {
			int s = 0;
			for(int k = rot[j].size() - 1; k >= 0; k--) {
				tab1[rot[j].size() - 1-k][j] = tab[j][rot[j][k]];
			}
		}/*
		for(int j = n-1; j >= 0; j--) {
			for(int k = 0; k < n; k++) {
				if (tab1[j][k] == 0) printf(".");
				if (tab1[j][k] == 1) printf("R");
				if (tab1[j][k] == -1) printf("B");}
			printf("\n");
		}*/
		// poziom
		for(int j = 0; j < n; j++) {
			int s = 0;
			for(int k = 0; k < n; k++) {
				if (((s==0) && (tab1[k][j] != 0)) ||(tab1[k][j]*s > 0)) s += tab1[k][j];
				else s = tab1[k][j];
//				printf("%d %d %d %d\n", tab1[k][j], k, j, s);
				if (s == kk) { a = true; /*printf("du[a\n -- %d %d", s, k) ;*/}
				if (s == -kk) { b = true; /*printf("dudu\n");*/}
			}
		}
		//pion
		for(int j = 0; j < n; j++) {
			int s = 0;
			for(int k = 0; k < n; k++) {
				if (((s==0) && (tab1[k][j] != 0)) ||(tab1[j][k]*s > 0)) s += tab1[j][k];
				else s = tab1[j][k];
				if (s == kk) a = true;
				if (s == -kk) b = true;
			}
		}
		for(int j = 0; j < n; j++) {
			int s1 = 0, s2 = j, s = 0; 
			for(int k = j; k < n; k++) {
				if (((s==0) && (tab1[k][j] != 0)) ||(tab1[s1][s2]*s > 0)) s += tab1[s1][s2];
				else s = tab1[s1][s2];
				if (s == kk) a = true;
				if (s == -kk) b = true;
				s1++; s2++;
			}
		}
		for(int j = 1; j < n; j++) {
			int s1 = j, s2 = 0, s = 0; 
			for(int k = j; k < n; k++) {
				if (((s==0) && (tab1[s1][s2] != 0)) ||(tab1[s1][s2]*s > 0)) s += tab1[s1][s2];
				else s = tab1[s1][s2];
				if (s==kk) a = true;
				if (s == -kk) b = true;
				s1++; s2++;
			}
		}

		for(int j = n-1; j >= 0; j--) {
			int s1 = j, s2 = 0,s = 0;
			for(int k = j;k >= 0; k--) {
				if (((s==0) && (tab1[s1][s2] != 0)) || (tab1[s1][s2]*s > 0)) s += tab1[s1][s2];
				else s = tab1[s1][s2];
				if (s == kk) a = true;
				if (s == -kk) b = true;
				s1--; s2++;
			}
		}
		for(int j = 1; j < n; j++) {
			int s1 = n-1, s2 = j, s = 0;
			for(int k = j;k < n; k++) {
				if (((s==0) && (tab1[s1][s2] != 0)) || (tab1[s1][s2]*s > 0)) s += tab1[s1][s2];
				else s = tab1[s1][s2];
				if (s == kk) a = true;
				if (s == -kk) b = true;
//				printf("%d %d %d %d\n", tab1[s1][s2], s1, s2, s);
				if (s == kk) { a = true;/*printf("du[a\n -- %d %d", s, k);*/}
				if (s == -kk) { b = true; /*printf("dudu\n");*/}
				s1--; s2++;
			}
		}
		printf("Case #%d: ", i);
		if (a && b) printf("Both");
		else if (a) printf("Red");
		else if (b) printf("Blue");
		else printf("Neither");
		printf("\n");
	}
}


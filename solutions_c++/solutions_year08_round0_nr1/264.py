#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>

using namespace std;

int n; // liczba testow
int s, q;
string ss[105];
string sq[1050];
int nr[1050];
int tab[105];
int sum;

int wrong(char c) {
	if (c >='A' && c <= 'Z') return 0;
	if (c >='a' && c <= 'z') return 0;
	if (c >='0' && c <= '9') return 0;
	if (c == ' ') return 0;
	return 1;
}

void dalej(void) {
	char *wsk;
	wsk = 0;
	size_t n;
	getline(&wsk, &n, stdin);
}

string wczytaj(void) {
	char *wsk;
	wsk = 0;
	size_t n;
	getline(&wsk, &n, stdin);
	string h = (string) wsk;
	while(wrong(h[h.length()-1])) h.resize(h.length()-1);
	return h;
}

int solve(void) {
	scanf("%d",&s);
	dalej();
	for(int i=0; i<s; i++) ss[i] = wczytaj();
	scanf("%d",&q);
	dalej();
	for(int i=0; i<q; i++) sq[i] = wczytaj();
	if (q<=1) return 0;
	for(int i=0; i<q; i++)
	for(int j=0; j<s; j++)
	{
		if (ss[j] == sq[i]) nr[i]=j;
	}
	int ak=0;
	int ret=0;
	while(ak < q) {
		ret ++;
		for(int i=0; i<s; i++) tab[i] = 0;
		sum = 0;
		while(ak < q && sum < s) {
			if (tab[nr[ak]] == 0) {
				tab[nr[ak]] = 1;
				sum++;
			}
			ak++;
		}
		if (sum == s) ak--;
	}
	return ret-1;
}

int main(void) {
 scanf("%d",&n);
 for(int er=1; er<=n; er++)
 {
  printf("Case #%d: %d\n", er, solve());
 }
 return 0;
}

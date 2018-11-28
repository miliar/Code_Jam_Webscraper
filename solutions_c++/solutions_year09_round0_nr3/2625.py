#include<cstdio>
#include<string>
using namespace std;

string s("welcome to code jam");

int main() {
	int t;
	scanf("%d\n", &t);
	for(int _i = 1; _i <= t; ++_i) {
		string ziom = "";
		char wc;
		while(true) {
			wc = getchar();
			if(wc == '\n' || wc == EOF)
				break;
			ziom += wc;
		}
		int tab[20];
		int tab2[20];
		for(int i = 0; i < 20; ++i) tab[i] = 0;
		int ile = ziom.size();

		tab[0] = 1;
		for(int i = 0; i < ile; ++i) {
			for(int j = 0; j < 20; ++j) tab2[j] = 0;
			for(int j = 0; j < 19; ++j) {
				if(ziom[i] == s[j]) {
					tab2[j+1] += tab[j];
					tab2[j+1] %= 10000;
				}
			}
			for(int j = 0; j < 20; ++j) {
				tab[j] += tab2[j];
				tab[j] %= 10000;
			}
		}
		printf("Case #%d: %04d\n", _i, tab[19]);
	}
	return 0;
}
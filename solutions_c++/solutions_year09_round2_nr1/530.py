#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

#define MAX 100


int main() {
	int n, l, a, i, j, nr, par, k, poz;
	string s, name, aux;
	vector<string> feat;
	char ss[100];
	double currp, p, mult;

	ifstream fin ("A-large.in");
	FILE *fout = fopen("test.out", "wt");
	fin >> n;
	
	for (i = 1; i <= n; i++) {
		fprintf(fout, "Case #%d: \n", i);
		fin >> l;
		s = "";
		for (j = 0; j <= l; j++) {
			fin.getline(ss, 81);
			s += ss;
		}
		fin >> a;
		for (k = 0; k < a; k++) {
			fin >> name >> nr;
			feat.resize(0);
			for (j = 0; j < nr; j++) {
				fin >> aux;
				feat.push_back(aux);
			}
			//compute;
			p = 1;
			poz = 0;
			//asdaasd
			while (1) {
				while (s[poz] == ' ') poz++;
				if (s[poz] == '(') poz++;
				while (s[poz] == ' ') poz++;
				currp = 0; mult = 0;
				while ((s[poz] >= '0' && s[poz] <= '9') || s[poz] == '.') {
					if (s[poz] == '.') mult = .1;
					else {
						if (mult == 0) currp = currp * 10 + (int) (s[poz] - '0');
						else {
							currp = currp + mult * ( (int) (s[poz] - '0') );
							mult *= 0.1;
						}
					}
					poz++;
				}
				p *= currp; //........
				while (s[poz] == ' ') poz++;
				nr = 0;
				while (s[poz+nr] >= 'a' && s[poz+nr] <= 'z') nr++;
				aux = s.substr(poz, nr);
				if (aux == "") break;
				poz += nr;
				for (j = 0; j < feat.size(); j++) 
					if (feat[j] == aux) 
						break;
				while (s[poz] == ' ') poz++;
				if (j == feat.size()) {
					par = 1; poz++;
					while (par != 0) {
						if (s[poz] == '(') par++;
						else if (s[poz] == ')') par--;
						poz++;
					}
				}
			}

//asdadasd
			fprintf(fout, "%.7lf\n", p);;
			}
		}
	fin.close();
	fclose(fout);
	return 0;
}
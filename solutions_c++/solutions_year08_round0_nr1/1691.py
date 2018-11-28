#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
	FILE *fin = fopen("A-large.in", "r");
	int n;
	fscanf(fin, "%d\n", &n);
	FILE *fout = fopen("A-large.out", "w");
	for(int i = 0; i < n; i++) {
		int s;
		fscanf(fin, "%d\n", &s);
		map<string, int> m;
		m.clear();
		for(int j = 0; j < s; j++) {
			char c = getc(fin);
			string p = "";
			while(c != ' ' && (c < 'a' || c > 'z') && (c < 'A' || c > 'Z') && (c < '0' || c > '9'))
				c = getc(fin);
			while(c == ' ' || (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) {
				p += c;
				c = getc(fin);
			}
			//cout << p << ",";
			m[p] = j;
		}
		//cout << endl;
		int q;
		fscanf(fin, "%d", &q);
		int a[1100];
		for(int j = 0; j < q; j++) {
			char c = getc(fin);
			string p = "";
			while(c != ' ' && (c < 'a' || c > 'z') && (c < 'A' || c > 'Z') && (c < '0' || c > '9'))
				c = getc(fin);
			while(c == ' ' || (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')) {
				p += c;
				c = getc(fin);
			}
			//cout << p << ",";
			a[j] = m[p];
		}
		//cout << endl;
		//cout << q << endl;
		//for(int j = 0; j < q; j++)
			//cout << a[j] << ",";
		//cout << endl;
		int k = 0;
		int o[110];
		int b = 0;
		while(k < q) {
			for(int j = 0; j < s; j++)
				o[j] = q;
			for(int j = k; j < q; j++)
				if(o[a[j]] == q)
					o[a[j]] = j;
			int x = 0;
			for(int j = 0; j < s; j++)
				x >?= o[j];
			//cout << x << endl;
			k = x;
			b++;
		}
		if(b == 0)
			b++;
		fprintf(fout, "Case #%d: %d\n", i + 1, b - 1);
	}
	fclose(fin);
	fclose(fout);
	//system("pause");
	return 0;
}

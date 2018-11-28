#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	int l, d, n;
	bool o[5000], oo[5000];
	char * dic[5000];
	fin >> l >> d >> n;
	for (int i = 0; i < d; i++) {
		dic[i] = new char[20];
		fin >> dic[i];
	}
	for (int cases = 1; cases <= n; cases ++) {

		char x;
		bool flag;
		memset(o, 1, sizeof(bool) * d);
		for (int ll = 0; ll < l; ll++) {
			memset(oo, 0, sizeof(bool) * d);
			flag = true;
			fin >> x;
			if (x == '(') {
				fin >> x;
				flag = false;
			}
			do {
				for (int i = 0; i < d; i++)
					if (o[i] && dic[i][ll] == x)
						oo[i] = true;
				if (flag) break;
				else {
					fin >> x;
					if (x == ')') break;
				}
			} while (1);
			for (int i = 0; i < d; i++)
				if (o[i] && oo[i]) o[i] = true;
				else o[i] = false;
		}
		char * temp =  new char [255];
		fin.getline(temp, 255);
		int ans = 0;
		for (int i = 0; i < d; i++)
			if (o[i]) ans ++;
		fout << "Case #" << cases << ": " << ans << endl;
	}
	fout.close();
	return 0;
}
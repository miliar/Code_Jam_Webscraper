#include <iostream>
#include <fstream>

using namespace std;

char * toFind = "welcome to code jam";

int main() {
	ifstream fin("C-large.in");
	ofstream fout("C-large.txt");
	int caseNum;
	char x;
	char * temp = new char[255];
	fin >> caseNum;
	fin.getline(temp, 255);
	int fl = strlen(toFind);
	for (int cases = 1; cases <= caseNum; cases ++) {
	int ans[510][21] = {0}, ansTot = 0;
			int now = 0;
		do{
			fin.get(x);
			if (x == '\n') break;
			if (x == 'w') 
				ans[now][0] = 1;
			for (int l = 1; l < fl; l++) {
				ans[now][l] = 0;
				if (x == toFind[l]) {
					for (int i = 0; i < now; i++) {
						ans[now][l] += ans[i][l - 1];
						if (ans[now][l] > 10000) ans[now][l] -= 10000;
					}
				}
			}
			ansTot += ans[now][fl - 1];
			if (ansTot > 10000) ansTot -= 10000;
			now ++;
		} while (1);

		fout << "Case #" << cases << ": ";
		fout << (ansTot / 1000) % 10 << (ansTot / 100) % 10 << (ansTot / 10) % 10 << ansTot % 10 << endl;
	}
	fout.close();
	return 0;
}


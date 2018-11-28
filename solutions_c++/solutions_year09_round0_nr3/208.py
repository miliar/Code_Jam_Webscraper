#include <iostream>
#include <string>
#include <cstring>
#include <iomanip>

using namespace std;


int N;
char tStr[] = "welcome to code jam";
int ltStr;
int cSet[512][20];
char buf[512];

void go(int caseId) {
	cin.getline(buf, 512);
	int i, j;
	for(i = 0; i < ltStr; i ++) {
		cSet[0][i] = 0;
	}
	if(buf[0] == tStr[0])
		cSet[0][0] = 1;
	for(i = 1; buf[i] != '\0'; i ++) {
		cSet[i][0] = cSet[i - 1][0];
		if(buf[i] == tStr[0]) {
			cSet[i][0] ++;
			cSet[i][0] %= 10000;
		}
		for(j = 1; j < ltStr; j ++) {
			cSet[i][j] = cSet[i - 1][j];
			if(buf[i] == tStr[j]) {
				cSet[i][j] += cSet[i - 1][j - 1];
				cSet[i][j] %= 10000;
			}
		}
	}
	cout << setfill('0');
	cout << "Case #" << caseId << ": " << setw(4) << cSet[i - 1][ltStr - 1] << endl;
}


int main() {
	ltStr = strlen(tStr);
	cin >> N;
	cin.getline(buf,512);
	for(int i = 1; i <= N; i ++) {
		go(i);
	}
	return 0;
}

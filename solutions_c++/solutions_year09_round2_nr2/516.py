#include <iostream>
#include <fstream>

using namespace std;

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("B-large.out");

	int caseNum;
	char * s = new char[255], * ans = new char[255];

	fin >> caseNum;
	for (int cases = 1; cases <= caseNum; cases ++) {
		fin >> s;
		int l = strlen(s);
		int num[10] = {0}, i;

		for (i = 0; i < l; i++) {
			num[int(s[i]) - 48] ++;			
		}

		char maxD = s[l-1], minD;
		bool flag = false;
		for (i = l - 2; i >= 0; i--) {
			if (s[i] > maxD) maxD = s[i];
			else if (s[i] < maxD) {
				flag = true;
				break;
			}
		}
		if (!flag) {
			for (int j = 1; j < 10; j++)
				if (num[j] > 0) {
					ans[0] = char(j + 48);
					num[j] --;
					break;
				}
			num[0] ++;
			int now = 1;
			for (int j = 0; j <= 9; j++) {
				for (int k = 0; k < num[j]; k++)
					ans[now++] = char(j + 48);
			}
			ans[l+1] = '\0';
		} else if (flag) {
			for (int j = i+1; j < l; j++)
				if (s[j] > s[i]) {
					minD = s[j]; break;
				}
			for (int j = i+1; j < l; j++)
				if (s[j] > s[i] && s[j] < minD)
					minD = s[j];
			s[i] = minD;
			for (int j = 0; j <= i; j++)
				num[int(s[j]) - 48] --;
			int now = i+1;
			strcpy(ans, s);
			for (int j = 0; j <= 9; j++) {
				for (int k = 0; k < num[j]; k++)
					ans[now++] = char(j + 48);
			}
			ans[l] = '\0';
		}
		fout << "Case #" << cases << ": " << ans << endl;
	}

	fin.close();
	fout.close();
	return 0;
}
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int flag[200];
	int cnt;
	ifstream fin("a.in");
	ofstream fout("a.out");
	int t;
	fin >> t;
	int i,j;
	long long base;
	string s;
	for (i = 0;i < t;i ++) {
		cnt = 0;
		fin >> s;

		for (j = 0;j < 200;j ++) flag[j] = -1;
		for (j = 0;j < s.length();j ++) {
			if (flag[(int)s[j]] == -1) {
				flag[(int)s[j]] = -2;
				cnt ++;
			}
		}
		base = cnt;
		if (base == 1) {
			base = 2;
		}
		int val;
		long long m = 1, sum = 0;
		for (j = 1;j < s.length();j ++) {
			m *= base;
		}
		for (j = 0;j < s.length();j ++) {
			if (flag[(int)s[j]] == -2) {
				if (j == 0) {
					val = 1;
				}
				flag[(int)s[j]] = val;
				if (val == 1) val--;
				else if (val == 0) val += 2;
				else val++;
			}
			
			//cout << "m = " << m << ", val=" << flag[(int)s[j]] << ", s[j] = " << s[j] << endl;
			sum += flag[(int)s[j]] * m;
			m /= base;
		}
		fout << "Case #" << i + 1 << ": " << sum << endl;
	}
	return 0;
}
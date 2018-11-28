#include <iostream>
#include <fstream>

using namespace std;
ofstream fout ("output.out");
ifstream fin ("input.in");

#define MAX_N	10

int T, cases;
int A, B;
char digit[MAX_N];
int len;

int getIntLen(int num) {
	if (num == 0)
		return 1;
	if (num < 0)
		num = -num;
	int ret = 0;
	while (num != 0) {
		num /= 10;
		ret ++;
	}
	return ret;
}

void work() {
	int mask[MAX_N] = {0,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000};
	int temp[MAX_N];
	int result = 0;
	int num;
	int i, j, k;
	len = getIntLen(B);
	for (i=A; i<B; i++) {
		for (j=1; j<len; j++) {
			num = i/mask[j] + (i%mask[j])*mask[len-j];
			temp[j] = num;
			if (num>i && num<=B) {
				bool flag = true;
				for (k=1; k<j; k++) {
					if (num == temp[k]) {
						flag = false;
						break;
					}
				}
				if (flag) {
					result ++;
				}
			}
		}
	}
	fout << "Case #" << cases << ": " << result << endl;
}

int main() {
	fin >> T;
	for (cases=1; cases<=T; cases++) {
		fin >> A >> B;
		work();
	}
	system("pause");
	return 0;
}

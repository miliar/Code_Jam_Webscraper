#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("b.in");
	ofstream fout("b.out");
	int t,n,i,j,x;
	fin >> t;
	for (i = 0;i < t;i ++) {
		int d1[10],d2[10];
		for (j = 0;j < 10;j ++) {
			d1[j] = 0;
		}
		fin >> n;
		x = n;
		while (x) {
			d1[x % 10] ++;
			x /= 10;
		}
		n ++;
		while (true) {
			x = n;
			for (j = 0;j < 10;j ++) {
				d2[j] = 0;
			}
			while (x) {
				d2[x % 10] ++;
				x /= 10;
			}
			bool flag = true;
			for (j = 1;j < 10;j ++) {
				if (d1[j] != d2[j]) {
					flag = false;
					break;
				}
			}
			if (flag) {
				fout << "Case #" << i + 1 << ": " << n << endl;
				break;
			} else {
				n ++;
			}
		}
	}
	return 0;
}
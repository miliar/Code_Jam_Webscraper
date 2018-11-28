#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int num[100000];
int vals[200];


int main(int argc, char *argv[]) {
	int ncases;
	cin >> ncases;

	for (int c = 1; c <= ncases; c++) {
		int nums;
		int fr;
		cin >> nums >> fr;

		for (int i = 0; i < fr; i++) {
			cin >> vals[i];
		}

		sort(vals, vals+fr);

		int min = 1 << 30;

		do {
			for (int i = 0; i <= nums; i++)
				num[i] = 0;

			int sum = 0;
			for (int i = 0; i < fr; i++) 
			{
				num[vals[i]] = 1;
				int j = vals[i]-1;
				while (j >= 1 && num[j] == 0) {
					j--;
					sum++;
				}
				j = vals[i]+1;
				while (j <= nums && num[j] == 0) {
					j++;
					sum++;
				}
			}
			if (sum < min) {
				min = sum;
			}

		} while (next_permutation(vals, vals+fr));

		cout << "Case #" << c << ": " << min << endl;



	}

	return 0;
}

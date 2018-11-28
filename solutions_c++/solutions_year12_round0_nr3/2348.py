#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int result(int A, int B);
int findDigit(int C);

void main () {
	int T, A, B;
	ifstream fin;
	fin.open("C-large.in");
	fin >> T;
	fin.get();

	ofstream fout;
	fout.open("Output.txt");

    for (int i = 0; i < T; i++) {
		fin >> A >> B;
		fout << "Case #" << i+1 << ": " << result(A, B) << endl;
    }
	
	fin.close();
	fout.close();

}

int result(int A, int B) {
	int y = 0;
	int digit = findDigit(B);
	int temp[7];
	bool repetition = false;
	if (digit == 1)
		return y;
	for (int i = A; i < B+1; i++) {
		int digit_i = findDigit(i);
		temp[0] = i;
		for (int k = 1; k < digit_i; k++) {
			temp[k] = (i%(int)pow(10.,k))*(int)pow(10.,digit_i - k) + i/(int)pow(10.,k);
			for (int j = 0; j < k; j++) {
				if (temp[j] == temp[k])
					repetition = true;
			}
			if ((temp[k] <= B) && (temp[k] >= A) && (repetition == false)) {
				y++;
			}
			repetition = false;
		}
	}
	return y/2;
}

int findDigit(int C) {
	int digit = 0;
	while ((C%(int)pow(10.,digit)) != C) {
		digit++;
	}
	return digit;
}
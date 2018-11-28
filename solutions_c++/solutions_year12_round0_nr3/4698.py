#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int getDigitAtIndex (int number, int index) {
	while (index > 1) {
		index--;
		number /= 10;
	}

	return number % 10;
}

int getNDigits (int number) {
	int n = 0;

	while (number > 0) {
		n++;
		number /= 10;
	}

	return n;
}

int getRecycled (int number, int index){
	int result = number;
	int power = 1;

	for (int i = 1; i < getNDigits(number); i++) {
		power *= 10;
	}

	for (int i = 1; i <= index; i++) {
		result /= 10;
	}

	for (int i = 1; i <= index; i++) {
		result += (power * getDigitAtIndex(number, index - i + 1));
		power /= 10;
	}

	return result;
}

int main () {
	int numberOfLines;
	int m = 11;
	int n = 22;

	ofstream outFile("C-small-attempt1.out");
	ifstream inFile;
	inFile.open("C-small-attempt1.in");
	if (!inFile) {
		cout << "Unable to open input file.";
	} else {
		inFile>>numberOfLines;

		for(int i = numberOfLines; i>0; i--) {
			inFile>>m;
			inFile>>n;

			int counter = 0;
			for (int i = m; i < n ; i++) {
				for (int j = i+1; j <= n; j++) {
					for (int k = 1; k <= getNDigits(n) - 1; k++) {
						int r = getRecycled(j, k);

						if ((i == r) && (j != r)) {
							counter++;
						}
					}
				}
			}

			outFile<<"Case #"<<numberOfLines-i+1<<": "<<counter;
			if (i!=1) 
				outFile<<endl;
		}
	}
	inFile.close();
	outFile.close();

	cin.get();
	return 0;
}
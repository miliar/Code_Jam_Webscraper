#include <fstream>
#include <iostream>

using namespace std;

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int num;
	fin >> num;
	
	for (int i = 1; i <= num; ++i) {
		int a, b;
		fin >> a >> b;
		int s = b, size;
		for (int j = 1; j <= 7; ++j) {
			s /= 10;
			if (s == 0) {
			size = j;
			j = 7;
			}
		}
		int pow = 1;
		for (int j = 1; j < size; ++j){
			pow *= 10;
		}
		s = b -a +1;
		int pairs[s];
		int total = 0, temp;
		for (int j = 0; j < s; ++j)
			pairs[j] = 0;
		for (int j = s; j > 0; --j) {
			temp = j+a - 1;
			for (int k = 1; k < size; ++k) {
				temp = (temp%pow)*10 + temp/pow;
				if (temp > j+a -1 && temp <= b && pairs[j-1] < 1+ pairs[temp-a])
					pairs[j-1] = 1+ pairs[temp-a];
			}
			total += pairs[j-1];
		}
		fout << "Case #" << i << ": " << total << "\n";
	}
	return 0;
}
#include <iostream>
#include <fstream>
#include <algorithm>
//#include <map>
//#include <string>
//#include <cmath>
#include <vector>

using namespace std;

int main(int argc, const char* argv[])  {
    ofstream fout ("gorosort.out");
    ifstream fin ("gorosort.in");

	int trials;
	fin >> trials;
	
	for (int i = 1; i <= trials; i++) {
		int num_numbers;
		fin >> num_numbers;
		
		int wrong_count = 0;
		for (int j = 1; j <= num_numbers; j++) {
			int next_number;
			fin >> next_number;
			if (next_number != j) {
				wrong_count++;
			}
		}
		
		cout << "Case #" << i << ": " << wrong_count << endl;
		fout << "Case #" << i << ": " << wrong_count << endl;
	}

}

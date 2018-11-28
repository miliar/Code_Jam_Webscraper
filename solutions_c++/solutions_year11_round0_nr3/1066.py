#include <iostream>
#include <fstream>
#include <algorithm>
//#include <map>
//#include <string>
//#include <cmath>
#include <vector>

using namespace std;

int trials;
int num_candy;
int min_value_candy;
int value_sum;
int value_nim_sum;

int next_candy_value;

int main(int argc, const char* argv[])  {
    ofstream fout ("candysplitting.out");
    ifstream fin ("candysplitting.in");

	fin >> trials;
	
	for (int i = 1; i <= trials; i++) {
		fin >> num_candy;

		min_value_candy = 1000001; // since max is 10^6
		value_sum = 0;
		value_nim_sum = 0;
				
		for (int j = 1; j <= num_candy; j++) {
			fin >> next_candy_value;
			
			if (next_candy_value < min_value_candy) {
				min_value_candy = next_candy_value;
			}
			
			value_sum = value_sum + next_candy_value;
			value_nim_sum = value_nim_sum ^ next_candy_value;
		}
		
		cout << "Case #" << i << ": ";
		fout << "Case #" << i << ": ";
		if (value_nim_sum == 0) {
			cout << value_sum - min_value_candy;
			fout << value_sum - min_value_candy;
		} else {
			cout << "NO";
			fout << "NO";
		}
		cout << endl;
		fout << endl;
	}

}

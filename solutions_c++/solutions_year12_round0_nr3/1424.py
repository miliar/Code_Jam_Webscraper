#include <iostream>
#include <fstream>
#include <algorithm>
//#include <map>
//#include <string>
#include <cmath>
#include <vector>

using namespace std;

int num_trials, low, high;

vector<int> recycled;

int num_digits(int n) { // assumes n >= 1
	int digits = 1;
	while (n >= 10) {
		n = n / 10;
		digits++;
	}
	return digits;
}

int recycle(int n, int pos, int digits) { // pass digits along because too lazy to calculate
	int factor1 = (int) pow(10,pos);
	int factor2 = (int) pow(10,digits-pos);
	int factor3 = (int) pow(10,digits-1);
	int recycled = n / factor1 + (n % factor1) * factor2;
	if (recycled < factor3) {
		return -1; //leading zero!
	} else {
		return recycled;
	} 
}

int main(int argc, const char* argv[])  {
    ofstream fout ("c.out");
    ifstream fin ("c.in");

	fin >> num_trials;
	
	
	for (int trial = 1; trial <= num_trials; trial++) {
		fin >> low >> high;
		
		int count = 0;
		
		for (int n = low; n <= high; n++) {
			recycled.clear();
			int digits = num_digits(n);
			for (int pos = 1; pos <= digits - 1; pos++) {
				int recycled_num = recycle(n, pos, digits);
				if (recycled_num != -1) {
					bool already_has_it = false;
					for (int i = 0; i < recycled.size(); i++) {
						if (recycled[i] == recycled_num) {
							already_has_it = true;
						}
					}
					if (!already_has_it) {
						recycled.push_back(recycled_num);
					}
				}
			}
			for (int i = 0; i < recycled.size(); i++) {
				if (low <= n && n < recycled[i] && recycled[i] <= high) {
					count++;
				}
			}
			
		}
				 
		fout << "Case #" << trial << ": " << count << endl;
	}
	
}

/* Recycled Numbers */
/*
 Auther: MM BARI
 progrmming language: c++
 email: talashbari@gmail.com
 */


#include <string>
using std::string;

#include <iostream>
using std::cerr;
using std::cout;
using std::endl;

#include <fstream>
using std::ifstream;
using std::ofstream;

#include <math.h>

#include <map>
#include <utility>
using namespace std;

int get_number_of_digit(int number)
{	
	int count_digit = 0;
	while (number != 0) {
		number /= 10;
		++ count_digit;
	}
	return count_digit;
}

int get_new_number(int old_number, int num_of_move)
{
	int new_number = old_number / (int)(pow(10, num_of_move));
	int moving = old_number % (int)(pow(10, num_of_move));
	new_number += (moving * (int)(pow(10, get_number_of_digit(new_number))));
	return new_number;
}

int main()
{
	
	ifstream input_file;
	ofstream output_file; 
	
    input_file.open("input.txt");
    output_file.open("output.txt");
  
	int cases;
	input_file >> cases;
	
	int A;
	int B;
	
	for (size_t i = 1; i <= cases; ++i) {
		input_file >> A;
		input_file >> B;
		
		map<pair<int, int>, int> pairs;
		
		size_t num_of_digit = get_number_of_digit(A);
		
		if (num_of_digit == 1) {
			output_file << "Case #" << i << ": " << 0 << endl;
			continue;
		} 
		
		for (int move = 1; move < num_of_digit; ++move) {
			for (int start = A; start <= B; ++start) {
				
				int m = get_new_number(start, move);
				if (m <= start) {
					continue;
				} else if (m <= B) {
					pairs[make_pair(start, m)] = move;
				}
			}
		}
		output_file << "Case #" << i << ": " << pairs.size() << endl;
	}				
	
    input_file.close();
    output_file.close();
	return 0;
}
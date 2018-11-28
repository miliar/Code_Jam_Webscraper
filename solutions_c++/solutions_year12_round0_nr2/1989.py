/* Dancing with the Googlers */
/*
 Auther: MM BARI
 progrmming language: c++
 email: talashbari@gmail.com
 */


#include <string>
using std::string;

#include <iostream>
using std::cout;
using std::endl;

#include <fstream>
using std::ifstream;
using std::ofstream;

using namespace std;

int main()
{
	
	ifstream input_file;
	ofstream output_file; 
	
    input_file.open("input.txt");
    output_file.open("output.txt");
    
	int total_cases;
	input_file >> total_cases;
	
	int N;
	int S;
	int P;
	int total_score;
	for (size_t i = 1; i <= total_cases; ++i) {
		input_file >> N;
		input_file >> S;
		input_file >> P;
		
		int count = 0;
		for (size_t dancer = 1; dancer <= N; ++dancer) {
			input_file >> total_score;
			
			int avg_score = total_score / 3;
			int remainder = total_score % 3;
			
			if (remainder == 0) { 
				if (avg_score >= P) {
					++count;
				} else if (S > 0 && (avg_score + 1) <= total_score) { 
					if ((avg_score + 1) >= P) {
						++count;
						--S;
					}
				}
			} else if (remainder == 1) { 
				if ((avg_score + 1) >= P) {
					++count;
				} 
			} else { 
				if ((avg_score + 1) >= P) {
					++count;
				} else if (S > 0 && (avg_score + 2) <= total_score) { 
					if ((avg_score + 2) >= P) {
						++count;
						--S;
					}
				}
			}
		}
		output_file << "Case #" << i << ": " << count << endl;
	}
				
	
    input_file.close();
    output_file.close();
	return 0;
}
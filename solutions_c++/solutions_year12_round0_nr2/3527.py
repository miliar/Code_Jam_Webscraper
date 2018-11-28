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



int main()
{
	
	ifstream input_file;
	ofstream output_file; 
	
    input_file.open("input.txt");
    output_file.open("output.txt");
    if(!input_file) {
		cout << "No input file found.\n";
        exit(1);
    }
	
    if (!output_file) {
		cout << "No output file found.\n";
        exit(1);
    }
	
	int cases;
	input_file >> cases;
	
	int num_of_dancers;
	int num_of_surprising_score;
	int best_result;
	int total_score;
	for (size_t i = 1; i <= cases; ++i) {
		input_file >> num_of_dancers;
		input_file >> num_of_surprising_score;
		input_file >> best_result;
		
		int count_top_dancers = 0;
		for (size_t dancer = 1; dancer <= num_of_dancers; ++dancer) {
			input_file >> total_score;
			
			int avg_score = total_score / 3;
			int remainder = total_score % 3;
			
			if (remainder == 0) { 
				if (avg_score >= best_result) { // all same scores, no surprise
					++count_top_dancers;
				} else if (num_of_surprising_score > 0 && (avg_score + 1) <= total_score) { 
					if ((avg_score + 1) >= best_result) { // not same score, with surprise
						++count_top_dancers;
						--num_of_surprising_score;
					}
				}
			} else if (remainder == 1) { 
				if ((avg_score + 1) >= best_result) { // Two scores are average and only one score is 1 point more than average
					++count_top_dancers;}
				//} else if (num_of_surprising_score > 0 && (avg_score + 2) <= total_score) { 
				//	if ((avg_score + 2) >= best_result) { // not same score, with surprise
				//		++count_top_dancers;
				//		--num_of_surprising_score;
				//	}
				//}
			} else { 
				if ((avg_score + 1) >= best_result) { // If remainder is 2 means: one score is average and two scores are 1 point more than average
					++count_top_dancers;
				} else if (num_of_surprising_score > 0 && (avg_score + 2) <= total_score) { 
					if ((avg_score + 2) >= best_result) { // OR Two scores are average and one score is 2 points more than average
						++count_top_dancers;
						--num_of_surprising_score;
					}
				}
			}
		}
		output_file << "Case #" << i << ": " << count_top_dancers << endl;
	}
				
	
    input_file.close();
    output_file.close();
	return 0;
}
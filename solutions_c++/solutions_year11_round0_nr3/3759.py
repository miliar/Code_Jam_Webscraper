#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>


using namespace std;
void Split(vector <int> nums, int TC) 
{
	vector <int>::iterator itr = nums.begin();
	int res = 0;
	int sum = 0;
	bool first = 0;
	int min = 0;

	for (; itr != nums.end(); itr++) {
		res ^= *itr;
		sum += *itr;
		if (!first) {
		    first = 1;
		    min = *itr;
		} else {
		    if (*itr < min) {
		        min = *itr;
		    }
		}
	}
	if (res) {
	   cout << "Case #"<<TC<<": NO"<< endl;
	} else {
	   cout << "Case #"<<TC<<": "<< sum - min << endl;
	}
}

main() 
{
	bool first = 0;
	int N=0, num, line_num=0;
	int total_cases, case_num=1;
	vector <int> numbers;
	string str;

	ifstream rfile("data");
	if (rfile.is_open()) {
	    while (getline(rfile, str)) {

			 line_num++;
			 stringstream ss(str);

		      if (!first) {
		        total_cases = atoi(str.c_str());
			   first = 1;
			 } else if (first && ((line_num % 2) == 0)) {
			   ss >> N;
			 } else if (first && ((line_num % 2) != 0)) {
			   for (int j = 0; j < N; j++) {
				   ss >> num;
				   numbers.push_back(num);
			   }
			   Split(numbers, case_num++);
			   numbers.clear();
			 }
	    }
	    rfile.close();
	}
}

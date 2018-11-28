#include <iostream>
#include <fstream>
#include <stack>
using namespace std;

bool is_oppose(char, char, char* , char* , int);

int main()
{
	ifstream infile("B-large.in");
	ofstream outfile("output.txt");

	int test_cases = 0;
	infile >> test_cases;
	for (int round = 0; round < test_cases; round++) {
		char combine1[100], combine2[100];
		char combine_to[100];
		char oppose1[100], oppose2[100];
		int combine_num;
		int oppose_num;
		char elements[10000];
		int elem;
		infile >> combine_num;
		string s;
		for (int i = 0; i < combine_num; i++) {
			infile >> s;
			combine1[i] = s.at(0);
			combine2[i] = s.at(1);
			combine_to[i] = s.at(2);
		}
		infile >> oppose_num;
		for (int i = 0; i < oppose_num; i++) {
			infile >> s;
			oppose1[i] = s.at(0);
			oppose2[i] = s.at(1);
		}
		infile >> elem >> elements;
		
		char new_list[100];
		int list_size = 0;

		for (int i = 0; i < elem; i++) {
			char c = elements[i];
			if (list_size == 0) {
				new_list[0] = elements[i];
				list_size++;
				continue;
			}
			// check combine
			bool combine_flag = false;
			for (int j = 0; j < combine_num; j++) {
				if ((new_list[list_size-1] == combine1[j] && c == combine2[j])
						|| (new_list[list_size-1] == combine2[j] && c == combine1[j])) {
					new_list[list_size-1] = combine_to[j];
					combine_flag = true;
					break;
				}
			}
			if (combine_flag)
				continue;

			// check oppose
			bool oppose_flag = false;
			for (int j = list_size-1; j >= 0; j--) {
				if (is_oppose(new_list[j], c, oppose1, oppose2, oppose_num)) {
					list_size = 0;
					oppose_flag = true;
					break;
				}
			}
			if (oppose_flag)
				continue;

			// insert
			new_list[list_size++] = c;
		}

		outfile << "Case #" << round+1 << ": [";
		for (int i = 0; i < list_size; i++) {
			outfile << new_list[i];
			if (i != list_size-1)
				outfile << ", ";
		}
		outfile << "]" << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}

bool is_oppose(char c1, char c2, char* array1, char* array2, int num)
{
	for (int i = 0; i < num; i++) {
		if ((c1 == array1[i] && c2 == array2[i]) || (c1 == array2[i] && c2 == array1[i]))
			return true;
	}
	return false;
}

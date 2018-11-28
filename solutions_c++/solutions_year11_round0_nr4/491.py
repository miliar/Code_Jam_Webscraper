#include <iostream>

int main(int argc, char* argv[])
{
	int num_of_cases;
	std::cin >> num_of_cases;
	for (int case_num = 1; case_num <= num_of_cases; ++case_num) {
		int num_of_elements;
		std::cin >> num_of_elements;
		int num_of_missplaced_elements = 0;
		for (int element_num = 1; element_num <= num_of_elements; element_num++) {
			int element;
			std::cin >> element;
			if (element != element_num)
				num_of_missplaced_elements++;
		}
		// don't need to convert to float, since result is always an integer
		std::cout << "Case #" << case_num << ": " << num_of_missplaced_elements << ".000000" << std::endl;
	}
	return 0;
}


#include <iostream>

int main(int argc, char* argv[])
{
	int num_of_cases;
	std::cin >> num_of_cases;
	for (int case_num = 1; case_num <= num_of_cases; ++case_num) {
		int num_of_candies;
		std::cin >> num_of_candies;
		int total_xor_candy_value = 0;
		int total_add_candy_value = 0;
		int minimum_candy_value = 0;
		for (int candy_num = 1; candy_num <= num_of_candies; candy_num++) {
			int candy_value;
			std::cin >> candy_value;
			total_xor_candy_value ^= candy_value;
			total_add_candy_value += candy_value;
			if (candy_num == 1 || minimum_candy_value > candy_value)
				minimum_candy_value = candy_value;
		}
		if (total_xor_candy_value != 0) {
			std::cout << "Case #" << case_num << ": NO" << std::endl;
		}
		else {
			std::cout << "Case #" << case_num << ": " << (total_add_candy_value - minimum_candy_value) << std::endl;
		}
	}
	return 0;
}


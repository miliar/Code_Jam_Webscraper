#include <iostream>

int main(void) {
	int lines;
	std::cin >> lines;

	for(int i = 0; i < lines; i++) {
		int size; std::cin >> size;
		int weird = 0, sum = 0, min = 100000000;

		for(int j = 0; j < size; j++) {
			int elem;
			std::cin >> elem;
			if(elem < min) min = elem;
			sum += elem;
			weird ^= elem;
		}

		if(weird == 0) {
			std::cout << "Case #" << i+1 << ": " << sum - min << std::endl;
		} else {
			std::cout << "Case #" << i+1 << ": NO" << std::endl;
		}
	}


	return 0;
}

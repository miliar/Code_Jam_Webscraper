#include <iostream>

int main() {

	unsigned int T;
	std::cin >> T;
	
	unsigned int i;
	for (i = 0; i < T; i++) {
		unsigned int N;
		std::cin >> N;
		unsigned int S;
		std::cin >> S;
		unsigned int p;
		std::cin >> p;

		unsigned int calculated_S = 0;
		unsigned int greater_than_p = 0;

		for (unsigned int j = 0; j < N; j++) {
			unsigned int data;
			std::cin >> data;

			if (data > 28) {
				greater_than_p++;
			} else if (data < 2) {
				if (p <= data)	greater_than_p++;
			} else {
				switch(data%3) {
					case 0:
						if (
							( (data/3) < p ) 
							&&
							( ( (data/3)+1) >= p)
						) {
							if (calculated_S < S) {
								calculated_S++;
								greater_than_p++;
							}
						} else if ( (data/3) >= p ) {
							greater_than_p++;
						}
						break;
					case 1: 
						if ( ((data/3)+1) >= p ) {
							greater_than_p++;
						}						
						break;
					case 2:
						if (
							( ( (data/3)+1) < p )
							&&
							( ( (data/3)+2) >= p )
						) {
							if (calculated_S < S) {
								calculated_S++;
								greater_than_p++;
							}
						} else if ( ((data/3)+1) >= p ) {
							greater_than_p++;
						}
						break;
				}
			}
		}
		std::cout << "Case #" << (i+1) << ": "<< greater_than_p << std::endl;
	}
}

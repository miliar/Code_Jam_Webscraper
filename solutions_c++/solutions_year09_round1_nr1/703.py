#include <iostream>
#include <string>
#include <sstream>
#include <set>

int is_happy(int num, int base, std::set<int>& s) {
	int sum = 0, digit, n = num;

	while(num > 0) {
		digit = num % base;
		num = num / base;
		sum += digit * digit;
	}
	
	if(sum == 1) {
//		std::cout << n << " es feliz en base " << base << "!!!\n";
		return true;
	} else if(s.count(sum)) {
		return false;
	} else {
		s.insert(sum);
		return is_happy(sum, base, s);
	}
}

int main(int argc, char* argv[]) {
	int T, bases[9];
	std::string line;

	std::cin >> T;

	std::cin.ignore();

	for(int i=0;i<T;i++) {
		int j=0, k=2;
		bool not_found=true;
		std::getline(std::cin, line);
		std::stringstream ss(line);
		while( ss.good()) {
			ss >> bases[j++];
		}
		while(not_found) {
			int b;
			for(b=0; b<j; b++) {
				std::set<int> s;
				if(!is_happy(k, bases[b], s)) {
					k++;
					break;
				}
			}
			if(b==j) {
				not_found=false;
			}
		}
		std::cout << "Case #" << i+1 << ": " << k << "\n";
	}

	return 0;
}


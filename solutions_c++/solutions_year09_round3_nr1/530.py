#include <iostream>
#include <vector>
#include <map>
#include <queue>

using std::string;
using std::vector;
using std::map;
using std::queue;
using std::pair;


unsigned long long minValue(const string& number) {
	
	map<char, int> digits;
	int base = 0;
	for (int i = 0; i < number.length(); i++) {
		if (digits.count(number[i]) == 0) {
			base++;
			digits[number[i]] = 1;
		} else {
			digits[number[i]]++;
		}
	}
//	std::cout << base << " ";
	if (base == 1) {
		base = 2;
	}
	for (int i = '0'; i <= '9'; i++) {
		digits[i] = -1;
	}
	for (int i = 'a'; i <= 'z'; i++) {
		digits[i] = -1;
	}
	unsigned long long currMult = 1;
	for (int i = 1; i < number.length(); i++) {
		currMult *= base;
	}
//	std::cout << currMult << " ";
	int currDigit = 1;
	unsigned long long currValue = 0;
	for (int i = 0; i < number.length(); i++) {
		if (digits[number[i]] == -1) {
			digits[number[i]] = currDigit;
			switch (currDigit) {
				case 1: currDigit = 0; break;
				case 0: currDigit = 2; break;
				default: currDigit++;
			}
		}
		currValue += digits[number[i]] * currMult;
		currMult /= base;
	}
	
	return currValue;
}
	



int main()  {
	
	int t;
	std::cin >> t;
	for (int i = 0; i < t; i++) {
		string number;
		std::cin >> number;
		try {
			std::cout << "Case #" << i+1 << ": " << minValue(number) << std::endl;
		} catch (string& str) {
			std::cout << str << std::endl;
		}
	}			
		
	return 0;
}


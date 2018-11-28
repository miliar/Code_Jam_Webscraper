#include <iostream>
#include <vector>

using std::ostream;
using std::string;
using std::vector;

const string pattern("welcome to code jam");


char charify(int digit);


class Last4 {
	
	public:
		
		Last4(int num);
		
		Last4& operator+=(const Last4 other);
		Last4 operator+(const Last4 other) const;
		
		operator string() const;
		
	private:
		
		int n;
		
};

ostream& operator<<(ostream& os, Last4 last4);


Last4 subseq(string str);


int main()  {
	
	int n;
	std::cin >> n;
	string str;
	std::getline(std::cin, str);
	for (int i = 0; i < n; i++) {
		std::getline(std::cin, str);
		try {
			std::cout << "Case #" << i + 1 << ": " << subseq(str) << std::endl;
		}
		catch (string& str) {
			std::cout << str << std::endl;
		}
	}		
		
	return 0;
}



char charify(int digit) {
	
	if ((digit < 0) || (digit > 9)) {
		throw string("not a digit");
	}
	return ('0' + digit);
}


Last4::Last4(int num) {
	
	n = num % 10000;
}


Last4& Last4::operator+=(const Last4 other) {
	
	n += other.n;
	n %= 10000;
	return *this;
}


Last4 Last4::operator+(const Last4 other) const {
	
	Last4 result(n + other.n);
	return result;
}


Last4::operator string() const {
	
	vector<char> result;
	result.push_back(charify((n % 10000) / 1000));
	result.push_back(charify((n % 1000) / 100));
	result.push_back(charify((n % 100) / 10));
	result.push_back(charify((n % 10)));
	return string(result.begin(), result.end());
}


ostream& operator<<(ostream& os, Last4 last4) {
	
	os << string(last4);
}


Last4 subseq(string str) {
	
	vector<vector<Last4> > count;
	
	for (int i = 0; i < str.length(); i++) {
		vector<Last4> letter;
		for (int j = 0; j < pattern.length(); j++) {
			Last4 letterCount(0);
			if (str.at(i) == pattern.at(j)) {
				if (j == 0) {
					letterCount = 1;
				} else {
					for (int k = 0; k < i; k++) {
						letterCount += count[k][j-1];
					}
				}
			}
// DEBUG:			std::cout << "i=" << i << " j=" << j << " letterCount=" << letterCount << std::endl;
			letter.push_back(letterCount);
		}
		count.push_back(letter);
	}
	Last4 total(0);
	for (int i = 0; i < str.length(); i++) {
		total += count[i][pattern.length()-1];
	}
	
	return total;
}



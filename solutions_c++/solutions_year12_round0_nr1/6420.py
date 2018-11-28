#include <iostream>
#include <string>
#include <algorithm>

int T;
std::string s;
char geez[26] = {
	'y','h','e','s','o',
	'c','v','x','d','u',
	'i','g','l','b','k',
	'r','z','t','n','w',
	'j','p','f','m','a',
	'q'
};

int map(int c) {
	if( c >= 97 && c <= 122 ) return geez[c-97];
	return c;
}

int main() {

	std::cin >> T;
	getline(std::cin,s);

	for(int i = 0; i < T; i++) {
		getline(std::cin, s);
		std::transform(s.begin(), s.end(), s.begin(), map);
		std::cout << "Case #" << i+1 << ": " << s << std::endl;;
	}

	return 0;
}
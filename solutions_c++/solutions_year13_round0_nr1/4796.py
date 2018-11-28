#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

void tictac(unsigned int t, std::string s) {
	std::stringstream ss;
	
	// rows
	ss << s.substr(0, 4) << "|" << s.substr(4, 4) << "|" << s.substr(8, 4) << "|" << s.substr(12, 4) << "|";

	// columns
	for( int c = 0; c < 4; c++ ) {
		ss << s.substr(0+c, 1) << s.substr(4+c, 1) << s.substr(8+c, 1) << s.substr(12+c, 1) << "|";
	}

	// diagonals
	ss << s.substr(0, 1) << s.substr(5, 1) << s.substr(10, 1) << s.substr(15, 1) << "|";
	ss << s.substr(3, 1) << s.substr(6, 1) << s.substr(9, 1) << s.substr(12, 1) << "|";

	std::cout << "Case #" << t << ": ";

	s = ss.str();
	std::replace(s.begin(), s.end(), 'T', 'X');
	if( s.find("XXXX") != std::string::npos ) {
		std::cout << "X won" << std::endl; return;
	}

	s = ss.str();
	std::replace(s.begin(), s.end(), 'T', 'O');
	if( s.find("OOOO") != std::string::npos ) {
		std::cout << "O won" << std::endl; return;
	}
	
	if( s.find(".") == std::string::npos) {
		std::cout << "Draw" << std::endl; return;
	}

	std::cout << "Game has not completed" << std::endl;

} 

int main(int argc, char* argv[]) {

	unsigned int T;
	std::ostringstream ss;
	std::string s;
	
	std::cin >> T;

	for( unsigned int t = 0; t < T; t++ ) {
		ss.str(std::string());
		ss.clear();
		for( unsigned int l = 0; l < 4; l++ ) {
			std::cin >> s;
			ss << s;
		}
		tictac(t+1, ss.str());
	}

	return 0;
}
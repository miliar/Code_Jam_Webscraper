#include <iostream>
#include <string>

//                          "abcdefghijklmnopqrstuvwxyz"
static const char *decode = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
	int T;
	std::cin >> T;
	std::string line;
	std::getline(std::cin, line);
	for (int t = 0; t < T; ++t) {
		std::getline(std::cin, line);
		for (int i = 0; i < line.size(); ++i) {
			char c = line[i];
			if (c >= 'a' && c <= 'z') {
				line[i] = decode[c - 'a'];
			}
		}
		std::cout << "Case #" << (t + 1) << ": " << line << std::endl;
	}
}

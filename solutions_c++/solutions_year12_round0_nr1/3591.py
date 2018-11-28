#include <iostream>
#include <fstream>
#include <algorithm>


char googlize(char a) {
	char normal[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' '};
	char google[] = {'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q', ' '};

	return normal[std::find(google, google + sizeof(google), a) - google];
}

int main(void) {
	int count;
	std::string line;
	std::ofstream fout("tongues.txt");

	std::cin >> count;
	std::getline(std::cin, line);

	for (int i = 0; i < count; ++i) {
		std::getline(std::cin, line);
		std::transform(line.begin(), line.end(), line.begin(), googlize);
		fout << "Case #" << (i + 1) << ": " << line << std::endl;
	}

	return 0;
}

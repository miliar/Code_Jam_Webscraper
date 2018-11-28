#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
	std::map<char, char> mapa;
	std::ifstream mapping("mapping.txt");
	std::string str, str2;
	for (int i = 0; i < 4; i++) {
		std::getline(mapping, str);
		std::getline(mapping, str2);
		std::cout << "'" << str << "'" << std::endl;
		std::cout << "'" << str2 << "'" << std::endl;
		for (int j = 0; j < str.length(); ++j)
			mapa[str[j]] = str2[j];
	}
	mapping.close();
	mapa['z'] = 'q';
	std::vector<char> v;
	for (char c = 'a'; c <= 'z'; ++c) {
		std::cout << c << " -> " << mapa[c] << std::endl;
		v.push_back(mapa[c]);
	}
	std::sort(v.begin(), v.end());
	for (int i = 0; i < v.size(); ++i)
		std::cout << v[i] << " ";
	mapa['z'] = 'q';
	std::ifstream input("input.txt");
	std::ofstream output("output.txt");
	std::getline(input, str);
	int n = atoi(str.c_str());
	std::cout << "\nn=" << n << std::endl;
	for (int i = 0; i < n; ++i) {
		std::getline(input, str);
		str2 = str;
		for (int j = 0; j < str.length(); ++j)
			str2[j] = mapa[str[j]];
		output << "Case #" << i + 1 << ": " << str2 << std::endl;
	}
	output.close();
	input.close();
	return 0;
}
#include <cstdlib>
#include <string>
#include <map>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char*argv[])
{
	std::map<char, char> mapping_tbl;
	mapping_tbl.insert(std::pair<char, char>('a', 'y'));
	mapping_tbl.insert(std::pair<char, char>('b', 'h'));
	mapping_tbl.insert(std::pair<char, char>('c', 'e'));
	mapping_tbl.insert(std::pair<char, char>('d', 's'));
	mapping_tbl.insert(std::pair<char, char>('e', 'o'));
	mapping_tbl.insert(std::pair<char, char>('f', 'c'));
	mapping_tbl.insert(std::pair<char, char>('g', 'v'));
	mapping_tbl.insert(std::pair<char, char>('h', 'x'));
	mapping_tbl.insert(std::pair<char, char>('i', 'd'));
	mapping_tbl.insert(std::pair<char, char>('j', 'u'));
	mapping_tbl.insert(std::pair<char, char>('k', 'i'));
	mapping_tbl.insert(std::pair<char, char>('l', 'g'));
	mapping_tbl.insert(std::pair<char, char>('m', 'l'));
	mapping_tbl.insert(std::pair<char, char>('n', 'b'));
	mapping_tbl.insert(std::pair<char, char>('o', 'k'));
	mapping_tbl.insert(std::pair<char, char>('p', 'r'));
	mapping_tbl.insert(std::pair<char, char>('q', 'z'));
	mapping_tbl.insert(std::pair<char, char>('r', 't'));
	mapping_tbl.insert(std::pair<char, char>('s', 'n'));
	mapping_tbl.insert(std::pair<char, char>('t', 'w'));
	mapping_tbl.insert(std::pair<char, char>('u', 'j'));
	mapping_tbl.insert(std::pair<char, char>('v', 'p'));
	mapping_tbl.insert(std::pair<char, char>('w', 'f'));
	mapping_tbl.insert(std::pair<char, char>('x', 'm'));
	mapping_tbl.insert(std::pair<char, char>('y', 'a'));
	mapping_tbl.insert(std::pair<char, char>('z', 'q'));

	std::ifstream projIn;
	std::string composeInSourse("C:\\Users\\Brook\\Desktop\\A-small-attempt0.in");
	projIn.open (composeInSourse, ifstream::in);

	std::ofstream projOut;
	std::string composeOutSourse("C:\\Users\\Brook\\Desktop\\decode_file.txt");
	projOut.open (composeOutSourse, ofstream::out);

	char number[1024];
	projIn.getline(number, 1024);
	int num = ::atoi(number);

	for(int times = 0 ; times != num ; ++times) {
		char encode[1024];
		projIn.getline(encode, 1024);
		int length = strlen( encode );
		std::cout << "Case #" << times+1 << ": ";
		projOut << "Case #" << times+1 << ": ";
		for(int idx = 0 ; idx != length ; ++idx) {
			if (encode[idx] == ' ') {
				continue;
			}
			encode[idx] = mapping_tbl[encode[idx]];
		}
		projOut << encode << std::endl;
		std::cout << encode << std::endl;
	}

	projIn.close();

	return 0;
}
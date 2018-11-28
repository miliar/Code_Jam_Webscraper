#include <iostream>
#include <fstream>
#include <map>
#include <cstdint>

std::ifstream infile("input.txt");
std::ofstream outfile("output.txt"); 

std::map<char, char> charmap;

int main(int argc, char *argv[]) {
	charmap.insert({'a', 'y'});
	charmap.insert({'b', 'h'}); 
	charmap.insert({'c', 'e'});
	charmap.insert({'d', 's'});
	charmap.insert({'e', 'o'});
	charmap.insert({'f', 'c'});
	charmap.insert({'g', 'v'});
	charmap.insert({'h', 'x'});
	charmap.insert({'i', 'd'});
	charmap.insert({'j', 'u'}); 
	charmap.insert({'k', 'i'});
	charmap.insert({'l', 'g'});
	charmap.insert({'m', 'l'});
	charmap.insert({'n', 'b'});
	charmap.insert({'o', 'k'});
	charmap.insert({'p', 'r'});
	charmap.insert({'q', 'z'});
	charmap.insert({'r', 't'});
	charmap.insert({'s', 'n'});
	charmap.insert({'t', 'w'});
	charmap.insert({'u', 'j'});
	charmap.insert({'v', 'p'});
	charmap.insert({'w', 'f'});
	charmap.insert({'x', 'm'});
	charmap.insert({'y', 'a'});
	charmap.insert({'z', 'q'});
	charmap.insert({' ', ' '});
	
	uint64_t N, iteration;
	infile >> N;
	for(iteration = 0; iteration < N; iteration++) {
		std::string line;
		do { std::getline(infile, line); } while(line == "");
		
		outfile << "Case #" << (iteration + 1) << ": ";
		
		uint64_t index;
		for(index = 0; index < line.length(); index++) {
			outfile << charmap[line[index]];
		}
		
		outfile << std::endl;
	}
	
	infile.close();
	outfile.close();
	return 0;
}
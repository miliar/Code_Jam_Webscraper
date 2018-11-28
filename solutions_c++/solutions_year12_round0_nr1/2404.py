#include <iostream>
#include <fstream>
#include <map>

std::map<char, char> char_map;

void init() {
	char_map['a'] = 'y';
	char_map['b'] = 'h';
	char_map['c'] = 'e';
	char_map['d'] = 's';
	char_map['e'] = 'o';
	char_map['f'] = 'c';
	char_map['g'] = 'v';
	char_map['h'] = 'x';
	char_map['i'] = 'd';
	char_map['j'] = 'u';
	char_map['k'] = 'i';
	char_map['l'] = 'g';
	char_map['m'] = 'l';
	char_map['n'] = 'b';
	char_map['o'] = 'k';
	char_map['p'] = 'r';
	char_map['q'] = 'z';
	char_map['r'] = 't';
	char_map['s'] = 'n';
	char_map['t'] = 'w';
	char_map['u'] = 'j';
	char_map['v'] = 'p';
	char_map['w'] = 'f';
	char_map['x'] = 'm';
	char_map['y'] = 'a';
	char_map['z'] = 'q';
}
void solve(char* p) {
	while(*p != 0) {
		if(char_map.find(*p) != char_map.end()) {
			*p = char_map[*p];
		}
		++p;
	}
}
int main(int argc , char** argv)
{
	init();
	char buf[200];
	std::ifstream in(argv[1]);
	int count;
	in >> count;
	in.getline(buf, sizeof(buf));
	for(int i = 1; i <=count;++i) 
	{
		in.getline(buf, sizeof(buf));
		solve(buf);
		std::cout << "Case #" << i << ": " << buf << std::endl;
	}
	return 0;
}


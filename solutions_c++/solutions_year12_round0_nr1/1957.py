#include <iostream>

int main() {
#if 0
	char cmap[26] = {
		/*a   b    c    d    e    f    g*/
		'y', 'h', 'e', 's', 'o', 'c', 'v', 
		/*h   i    j    k    l    m    n*/
		'x', 'd', 'u', 'i', 'g', 'l', 'b',
		/*o   p    q         r    s    t*/
		'k', 'r', 'q',      't', 'n', 'w', 
		/*u   v    w         x    y    z*/
		'j', 'p', 'f',      'm', 'a', 'z'};
#endif

	char cmap[26] = {
		/*a   b    c    d    e    f    g*/
		'y', 'h', 'e', 's', 'o', 'c', 'v', 
		/*h   i    j    k    l    m    n*/
		'x', 'd', 'u', 'i', 'g', 'l', 'b',
		/*o   p    q         r    s    t*/
		'k', 'r', 'z',      't', 'n', 'w', 
		/*u   v    w         x    y    z*/
		'j', 'p', 'f',      'm', 'a', 'q'};

	int T;
	std::cin >> T;
	char line[256];
	std::cin.getline(line, 256);

	for (int i = 0; i < T; ++i) {
		std::cin.getline(line, 256);
		std::cout << "Case #" << (i + 1) << ": ";
		for (int m = 0; line[m] != '\0'; ++m) {
			if (line[m] == ' ') std::cout << ' ';
			else std::cout << cmap[line[m] - 'a']; 
		} 
		std::cout << std::endl;
	}
	return 0;
}

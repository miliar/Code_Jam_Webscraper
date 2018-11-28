#include <stdexcept>
#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>
char map[256];
char rmap[256];

void add(char c1, char c2, char *map) {
	if (c1==0 || c2==0) throw std::runtime_error("zero");
	unsigned int i1 = (unsigned char)c1;
	if (map[i1]==0) map[i1] = c2;
	else if (map[i1]!=c2)
		throw std::runtime_error("diff subs");
}

void add(const std::string &s1, const std::string &s2) {
	if (s1.size()!=s2.size())
		throw std::runtime_error("length mismatch");
	for (size_t i=0; i<s1.size(); i++) {
		add(s1[i], s2[i], map);
		add(s2[i], s1[i], rmap);
	}
}

void check() {
	char *p_zero = std::find(map+'a', map+'z'+1, 0);
	char *p_rzero = std::find(rmap+'a', rmap+'z'+1, 0);
	if (p_zero!=map+'z'+1) {
		char c2 = p_rzero - rmap;
		*p_zero = c2;
	}
	p_zero = std::find(map+'a', map+'z'+1, 0);
	if (p_zero!=map+'z'+1) throw std::runtime_error("ambiguous");
	if (map[' '] != ' ')
		throw std::runtime_error("space");
}

int main() {
	try {
		std::cin.exceptions(std::ios::failbit|std::ios::badbit);
		std::cout.exceptions(std::ios::failbit|std::ios::badbit);
		add("y qee", "a zoo");
		add("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
		add("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
		add("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
		check();
		std::string line;
		std::getline(std::cin, line);
		std::istringstream f(line);
		f.exceptions(std::ios::failbit|std::ios::badbit);
		unsigned int n;
		f >> n;
		for (unsigned int i=0; i<n; i++) {
			std::getline(std::cin, line);
			for (size_t j=0; j<line.size(); j++) {
				char c = map[(unsigned char)line[j]];
				if (c==0) throw std::runtime_error(std::string("unknown char: ") + c);
				line[j] = c;
			}
			std::cout << "Case #" << (i+1) << ": " << line << std::endl;
		}
	} catch (const std::exception &ex) {
		std::cerr << ex.what() << std::endl;
		return 1;
	}
	return 0;
}


#include <iostream>
#include <fstream>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>

static std::map<char, char> mapping;
static std::map<char, char> reverse;


void assert(bool test)
{
	if (!test) {
		std::cout << "Assertion failed." << std::endl;
		throw std::exception("Assertion failed");
	}
}

void processCase(std::istream& in, std::ostream& out)
{
	std::string str;
	std::getline(in, str);
	for (size_t i=0; i<str.length(); i++) {
		if (str[i] != '\r' && str[i] != '\n') {
			out << mapping[str[i]];
		}
	}
	out << std::endl;
}


void process(std::istream& in, std::ostream& out)
{
	int T;
	in >> T;
	std::string str;
	std::getline(in, str);

	for (int i=0; i<T; i++) {
		out << "Case #" << (i+1) << ": ";
		processCase(in, out);
	}
}


void createMapping(std::string goog, std::string eng)
{
	assert(goog.length() == eng.length());
	for (size_t i=0; i<goog.length(); i++) {
		auto result = mapping.find(goog[i]);
		if (result != mapping.end()) {
			assert(result->second == eng[i]);
		}
		mapping[goog[i]] = eng[i];
		reverse[eng[i]] = goog[i];
	}
}


int main(int argc, char** argv)
{
	createMapping("y qee", "a zoo");
	createMapping("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
	createMapping("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
	createMapping("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
	createMapping("z", "q");
	for (auto i=mapping.begin(); i != mapping.end(); i++) {
		std::cout << i->first << " -> " << i->second << std::endl;
	}
	for (auto i=reverse.begin(); i != reverse.end(); i++) {
		std::cout << i->first << " -> " << i->second << std::endl;
	}

	std::ifstream ifs("A-small-attempt0.in");
	std::ofstream ofs("quali_a_small.txt");
	process(ifs, ofs);
}

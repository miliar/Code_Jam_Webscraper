#include <iostream>
#include <fstream>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>


void assert(bool test)
{
	if (!test) {
		std::cout << "Assertion failed." << std::endl;
		throw std::exception("Assertion failed");
	}
}


int rotate(int n, int digits, int rot)
{
	static int masks[] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000 };
	int mask = masks[rot];
	int compMask = masks[digits-rot];
	return (n % mask)*compMask + (n / mask);
}


void processCase(std::istream& in, std::ostream& out)
{
	int count = 0;

	int A, B;
	in >> A;
	in >> B;
	int rots[10];

	int digits = int(log10((double)A)) + 1;
	for (int n=A; n<=B; n++) {
		for (int i=1; i<digits; i++) {
			int m = rotate(n, digits, i);
			rots[i] = m;
			if (m > n && m <= B) {
				count++;
				for (int j=1; j<i; j++) {
					if (rots[j] == m) {
						count--;
						break;
					}
				}
			}
		}
	}

	out << count;
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
		out << std::endl;
	}
}


int main(int argc, char** argv)
{
	std::ifstream ifs("C-large.in");
	std::ofstream ofs("quali_c_large.txt");
	process(ifs, ofs);
}

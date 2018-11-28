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

int highNonSurprising(int t)
{
	if (t % 3 == 0) return t / 3;
	return (t / 3) + 1;
}

int highSurprising(int t)
{
	/*
	a, a, a-2 =    3a - 2 = t
	a, a-1, a-2 =  3a - 3 = t
	a, a-2, a-2 =  3a - 4 = t
	*/

	if (t < 2 || t > 28) return -1;
	if ((t+2) % 3 == 0) return (t+2) / 3;
	if ((t+3) % 3 == 0) return (t+3) / 3;
	return (t+4) / 3;
}

void processCase(std::istream& in, std::ostream& out)
{
	int count = 0;
	int N;
	int S;
	int p;

	in >> N;
	in >> S;
	in >> p;
	for (int i=0; i<N; i++) {
		int t;
		in >> t;

		if (highNonSurprising(t) >= p) {
			count++;
		} else if (S > 0 && highSurprising(t) >= p) {
			count++;
			S--;
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
	std::ifstream ifs("B-large.in");
	std::ofstream ofs("quali_b_large.txt");
	process(ifs, ofs);
}

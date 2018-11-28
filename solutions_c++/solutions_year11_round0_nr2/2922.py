/*
 * main.cpp
 *
 *  Created on: May 7, 2011
 *      Author: greenvirag
 */

//The first line of the input gives the number of test cases, T. T test cases follow.
//Each test case consists of a single line beginning with a positive integer N,
//representing the number of buttons that need to be pressed.
//This is followed by N terms of the form "Ri Pi" where Ri is a robot color (always 'O' or 'B'),
//and Pi is a button position.



#include <iostream>
#include <cstdio>
#include <map>
#include <set>


enum Robots {BLUE, ORANGE};

int main(int argc, char** argv)
{
	register unsigned char i, j, k, l, m;		// index variables

	std::set< char >	base;
	base.insert('Q'); base.insert('W'); base.insert('E'); base.insert('R');
	base.insert('A'); base.insert('S'); base.insert('D'); base.insert('F');

	unsigned char T; 		// number of test cases
	unsigned char C;		// number of combines
	unsigned char D;		// number of opposites
	unsigned char N; 		// series of elements

	std::map< std::string, char >	crules;
	std::set< std::string >			drules;
	std::map< std::string, char >::iterator	citer;
	std::set< std::string >::iterator		diter;

	FILE* input = fopen("B-large.in", "r");
	if (input == NULL) {
		std::cerr << "Error while opening input file..";
		return -1;
	}

	FILE* output = fopen("B-large.out", "w");
	if (output == NULL) {
		std::cerr << "Error while opening output file..";
		return -1;
	}


	T = 0;
	fread(&k,1,1,input);
	while(k == ' ' || k == '\t' ) {
		fread(&k,1,1,input);
	}
	while('0' <= k && k <= '9' ) {
		T = T*10 + k - '0';
		fread(&k,1,1,input);
	}
	std::cout << "T = " << (unsigned int)T << std::endl;

	for (i = 0; i < T; i++) {
		std::cout << std::endl << (unsigned int)T << "/" << (unsigned int)i << ". test case begins.." << std::endl;

		crules.clear();
		drules.clear();

		C = 0;
		fread(&k,1,1,input);
		while(k == ' ' || k == '\t' ) {
			fread(&k,1,1,input);
		}
		while('0' <= k && k <= '9' ) {
			C = C*10 + k - '0';
			fread(&k,1,1,input);
		}
		std::cout << "C = " << (unsigned int)C << std::endl;

		for (j = 0; j < C; j++) {

			/* Skip empty parts in the line */
			fread(&k,1,1,input);
			while(k == ' ' || k == '\t' ) {
				fread(&k,1,1,input);
			}

			fread(&l,1,1,input);
			fread(&m,1,1,input);
			std::string s = ""; s += k; s += l;
			crules.insert(std::make_pair(s, m));
			s = ""; s += l; s += k;
			crules.insert(std::make_pair(s, m));
		}

		D = 0;
		fread(&k,1,1,input);
		while(k == ' ' || k == '\t' ) {
			fread(&k,1,1,input);
		}
		while('0' <= k && k <= '9' ) {
			D = D*10 + k - '0';
			fread(&k,1,1,input);
		}
		std::cout << "D = " << (unsigned int)D << std::endl;

		for (j = 0; j < D; j++) {

			/* Skip empty parts in the line */
			fread(&k,1,1,input);
			while(k == ' ' || k == '\t' ) {
				fread(&k,1,1,input);
			}

			fread(&l,1,1,input);
			std::string s = ""; s += k; s += l;
			drules.insert(s);
			s = ""; s += l; s += k;
			drules.insert(s);
		}

		/* Make calculations */
		N = 0;
		fread(&k,1,1,input);
		while(k == ' ' || k == '\t' ) {
			fread(&k,1,1,input);
		}
		while('0' <= k && k <= '9' ) {
			N = N*10 + k - '0';
			fread(&k,1,1,input);
		}
		std::cout << "N = " << (unsigned int)N << std::endl;

		/* Skip empty parts in the line */
		while(k == ' ' || k == '\t' ) {
			fread(&k,1,1,input);
		}

		std::string s = "";
		for (j = 0; j < N; j++) {

			s += k;
			std::cout << "S: " << s << std::endl;

			if (s.length() > 1) {

				/* C rules */
				std::string::iterator it = s.end()-2;
				std::string temp = "";
				temp += *it;
				temp += *(it+1);

				citer = crules.find(temp);
				if (citer != crules.end()) {
					std::cout << "Crule: " << temp << std::endl;
					s.erase(s.length()-2,2);
					s += citer->second;
				} else {

					/* D rules */
					for (diter = drules.begin(); diter != drules.end(); diter++) {
						temp = *diter;
						if (temp.at(0) == k) {

							size_t found = s.find(temp.at(1));
							if (found != std::string::npos) {
								std::cout << "Drule: " << temp << std::endl;
								s = "";
								break;
							}
						}
					}
				}
			}

			fread(&k,1,1,input);
			if (feof(input)) {
				break;
			}
		}

		std::string outstr = "[";
		for (unsigned int z = 0; z < s.length(); z++) {
			outstr += s.at(z);
			if (z+1 < s.length()) {
				outstr += ", ";
			}
		}
		outstr += "]";
		fprintf(output, "Case #%u: %s\n", (unsigned int)i + 1, outstr.data());
		std::cout << "Case #" << (unsigned int)i + 1 << ": " << outstr << std::endl;
		std::cout << (unsigned int)T << "/" << (unsigned int)i << ". test case ends.." << std::endl << std::endl;
	}

	fclose(input);
	fclose(output);

	return 0;
}

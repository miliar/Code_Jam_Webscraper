/* 
 * File:   main.cpp
 * Author: maul
 *
 * Created on 2009. szeptember 2., 23:58
 *
 *
 * //alien language
 */

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <set>
#include <map>

/*
 * 
 */
int main(int argc, char** argv)
{

	unsigned int L, D, N;
	std::cin >> L;
	std::cin >> D;
	std::cin >> N;


	typedef std::map<unsigned int, std::set<char> > csvect;


	std::vector<std::string> words(D);

	for (unsigned int i = 0; i < D; i++) {
		std::cin >> words[i];
	}

	for (unsigned int i = 0; i < N; i++) {
		std::string tstr;
		std::cin >> tstr;
		bool par_on = false;
		unsigned int k = 0;
		csvect nvect;
		for (unsigned int j = 0; j < tstr.length(); j++) {
			char c = tstr[j];
			if (c == '(')par_on = true;
			else if (c == ')')
				par_on = false;
			else {
				nvect[k].insert(c);
			}
			if (!par_on) k++;

		}
		std::set<unsigned int> poss;
		for (unsigned int g = 0; g < D; g++) {
			poss.insert(g);
			for (unsigned int j = 0; j < k; j++) {
				if (nvect[j].count(words[g][j]) == 0) poss.erase(g);
			}
		}


		std::cout << "Case #" << i+1 << ": " << poss.size() << "\n";
	}



	return(EXIT_SUCCESS);
}


#include <iostream>
#include <list>
#include <map>
#include <utility>
#include <algorithm>

typedef std::list<char> Elements;
typedef std::map<std::pair<char, char>, char> Combinations;
typedef std::map<char, char> Oppositions;
typedef std::pair<char, char> Pair;

Elements combine(Elements olde, Combinations c, Oppositions o) {
	Elements newe;
	for(Elements::iterator it = olde.begin(); it != olde.end(); ++it) {
		newe.push_back(*it);
		if(newe.size() >= 2) {
			// Combinations
			char last = newe.back(); newe.pop_back();
			char blast = newe.back(); newe.pop_back();
			Combinations::iterator result = c.find(Pair(last, blast));
			if(result != c.end()) {
				newe.push_back(result->second);
			} else {
				newe.push_back(blast);
				newe.push_back(last);
			}

			// Oppositions
			last = newe.back();
			Oppositions::iterator opposed = o.find(last);
			if(opposed != o.end()) {
				Elements::iterator incompatible = find(newe.begin(), newe.end(), opposed->second);
				if(incompatible != newe.end()) {
					newe.clear();
				}
			}
		}
	}

	return newe;
}

void print_list(Elements elements) {
	std::cout << "[";
	for(Elements::iterator it = elements.begin(); it != elements.end(); ++it) {
		// print element
		std::cout << *it;
		
		// print space if needed
		Elements::iterator next = it;
		if(++next != elements.end()) {
			std::cout << ", ";
		}
	}
	std::cout << "]";
}

int main(void) {
	int lines;
	std::cin >> lines;

	for(int cases = 0; cases < lines; ++cases) {
		int combines, opposes, size;

		Combinations combinations;
		std::cin >> combines;
		for(int i = 0; i < combines; ++i) {
			std::string formula;
			std::cin >> formula;
			Pair p1 = Pair(formula.at(0), formula.at(1));
			Pair p2 = Pair(formula.at(1), formula.at(0));
			combinations[p1] = formula.at(2);
			combinations[p2] = formula.at(2);
		}

		std::cin >> opposes;
		Oppositions oppositions;
		for(int i = 0; i < opposes; ++i) {
			std::string formula;
			std::cin >> formula;
			oppositions[formula.at(0)] = formula.at(1);
			oppositions[formula.at(1)] = formula.at(0);
		}

		Elements elements;
		std::cin >> size;
		std::cin.get();
		for(int i = 0; i < size; i++) {
			char c = std::cin.get();
			elements.push_back(c);
		}

		Elements final = combine(elements, combinations, oppositions);
		std::cout << "Case #" << cases+1 << ": ";
		print_list(final);
		std::cout << std::endl;
	}
}

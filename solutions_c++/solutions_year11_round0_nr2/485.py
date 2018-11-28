#include <iostream>
#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <utility>

int main(int argc, char* argv[])
{
	int num_of_cases;
	std::cin >> num_of_cases;
	for (int case_num = 1; case_num <= num_of_cases; ++case_num) {
		std::map<std::pair<char, char>, char> replacements;
		int num_of_replacements;
		std::cin >> num_of_replacements;
		for (int replacement_num = 1; replacement_num <= num_of_replacements; replacement_num++) {
			char src_elem1, src_elem2, result_elem;
			std::cin >> src_elem1 >> src_elem2 >> result_elem;
			if (src_elem1 > src_elem2)
				std::swap(src_elem1, src_elem2);
			replacements[std::make_pair(src_elem1, src_elem2)] = result_elem;
		}
		std::map<char, std::set<char> > oposites;
		int num_of_oposites;
		std::cin >> num_of_oposites;
		for (int oposite_num = 1; oposite_num <= num_of_oposites; oposite_num++) {
			char oposite_elem1, oposite_elem2;
			std::cin >> oposite_elem1 >> oposite_elem2;
			oposites[oposite_elem1].insert(oposite_elem2);
			oposites[oposite_elem2].insert(oposite_elem1);
		}
		std::list<char> elements;
		int num_of_elements;
		std::cin >> num_of_elements;
		for (int elem_num = 1; elem_num <= num_of_elements; elem_num++) {
			char input_elem;
			std::cin >> input_elem;
			if (elements.empty()) {
				elements.push_back(input_elem);
			}
			else {
				char src_elem1 = elements.back();
				char src_elem2 = input_elem;
				if (src_elem1 > src_elem2)
					std::swap(src_elem1, src_elem2);
				std::pair<char, char> replacement_key(src_elem1, src_elem2);
				std::map<std::pair<char, char>, char>::const_iterator replacement_it = replacements.lower_bound(replacement_key);
				if (replacement_it != replacements.end() && replacement_it->first == replacement_key) {
					elements.pop_back();
					elements.push_back(replacement_it->second);
				}
				else {
					std::map<char, std::set<char> >::const_iterator opposite_it = oposites.lower_bound(input_elem);
					if (opposite_it == oposites.end() || opposite_it->first != input_elem) {
						elements.push_back(input_elem);
					}
					else {
						const std::set<char>& opposite_elements = opposite_it->second;
						for (std::set<char>::const_iterator opposite_element_it = opposite_elements.begin(); opposite_element_it != opposite_elements.end(); ++opposite_element_it) {
							if (std::find(elements.begin(), elements.end(), *opposite_element_it) != elements.end()) {
								elements.clear();
								break;
							}
						}
						if (!elements.empty())
							elements.push_back(input_elem);
					}
				}
			}
		}
		std::cout << "Case #" << case_num << ": [";
		for (std::list<char>::const_iterator elem_it = elements.begin(); elem_it != elements.end(); ++elem_it)
		{
			if (elem_it != elements.begin())
				std::cout << ", ";
			std::cout << *elem_it;
		}
		std::cout << "]" << std::endl;
	}
	return 0;
}


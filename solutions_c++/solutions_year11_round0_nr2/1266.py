#include <iostream>
#include <vector>

using namespace std;


struct triplet {
	unsigned char first;
	unsigned char second;
	unsigned char result;
};


unsigned char combine(unsigned char c1, unsigned char c2, vector<triplet> & comb) {
	for (unsigned int i=0 ; i<comb.size() ; ++i) {
		if ( (comb[i].first == c1 && comb[i].second == c2) ||
			(comb[i].first == c2 && comb[i].second == c1) ) {
			return comb[i].result;
		}
	}
	
	return 0;
}

bool check_oppos(vector<unsigned char> elems, unsigned char new_elem, vector<pair<unsigned char, unsigned char> > oppos) {
	for (unsigned int i=0 ; i<oppos.size() ; ++i) {
		if (oppos[i].first == new_elem) {
			for (unsigned int j=0 ; j<elems.size() ; ++j) {
				if (elems[j] == oppos[i].second) {
					return true;
				}
			}
		} else if (oppos[i].second == new_elem) {
			for (unsigned int j=0 ; j<elems.size() ; ++j) {
				if (elems[j] == oppos[i].first) {
					return true;
				}
			}
		}
	}
	return false;
}

int main(void) {
	unsigned int T = 0; // number of test cases
	
	std::cin >> T;
	
	for (unsigned int i=0 ; i<T ; ++i) {
		unsigned int C = 0; // number of combine pairs
		std::cin >> C;
		
		vector<triplet> comb;
		for (unsigned int j=0 ; j<C ; ++j) {
			std::string str;
			std::cin >> str;
			//std::cout << "comb: " << str << "len: " << str.length() << endl;
			triplet comb_elem;
			comb_elem.first = str[0];
			comb_elem.second = str[1];
			comb_elem.result = str[2];
			comb.push_back(comb_elem);
		}

		unsigned int D = 0; // number of opposed pairs
		std::cin >> D;		
		
		vector<pair<unsigned char, unsigned char> > oppos;
		for (unsigned int j=0 ; j<D ; ++j) {
			std::string str;
			std::cin >> str;
			//std::cout << "oppos: " << str << "len: " << str.length() << endl;
			pair<unsigned char, unsigned char> pair_elem (str[0],str[1]);
			oppos.push_back(pair_elem);
		}
		
		unsigned int N = 0; // number of base elements
		std::cin >> N;
		std::vector<unsigned char> result;
		
		for (unsigned int j=0 ; j<N ; ++j) {
			unsigned char elem;
			std::cin >> elem;
			//std::cout << elem << endl;
			
			if (result.size() > 0) {
				unsigned char new_elem = combine(result.back(), elem, comb);
				if (new_elem) {
					result.pop_back();
					result.push_back(new_elem);
					continue;
				}
				
				if (check_oppos(result, elem, oppos)) {
					result.clear();
					continue;
				}
			}
			
			result.push_back(elem);
		}
		
		std::cout << "Case #" << i+1 << ": [";
		if (result.size() == 0) {
			std::cout << "]" << endl;
		} else {
			for (unsigned int j=0 ; j<(result.size()-1) ; ++j) {
				std::cout << result[j] << ", ";
			}
			
			std::cout << result.back() << "]" << endl;
		}
	}
}



#include <iostream>
#include <vector>
#include <map>

using std::map;
using std::string;
using std::vector;


bool isSmall(char c);

map<char, bool> emptyMap();


class Pattern {
	
	public:
		
		Pattern(const string& pattern, int l);
		
		bool isMatch(const string& str);
	
	private:
		
		vector<map<char, bool> > p;

};



int main()  {
	
	int l, d, n;
	std::cin >> l >> d >> n;
	vector<string> dict;
	for (int i = 0; i < d; i++) {
		string word;
		std::cin >> word;
		dict.push_back(word);
	}
	
	for (int i = 0; i < n; i++) {
		string test;
		std::cin >> test;
		try {
			Pattern pattern(test, l);
			int count = 0;
			for (int j = 0; j < d; j++) {
				if (pattern.isMatch(dict[j]))
					count++;
			}
			std::cout << "Case #" << i+1 << ": " << count << std::endl;
		} catch (string& str) {
			std::cout << str << std::endl;
		}

	}			
		
	return 0;
}


bool isSmall(char c) {
	if (c < 'a')
		return false;
	if (c > 'z')
		return false;
	return true;
}


map<char, bool> emptyMap() {
	map<char, bool> m;
	for (char c = 'a'; c <= 'z'; c++)
		m[c] = false;
	return m;
}


Pattern::Pattern(const string& pattern, int l) {
	
	int sets = 0;
	for (int i = 0; i < pattern.length(); i++) {
		map<char, bool> m = emptyMap();
		if (pattern.at(i) != '(') {
			if (!isSmall(pattern.at(i)))
				throw string("baah!");
			m[pattern.at(i)] = true;
		} else {
			while (++i < pattern.length()) {
				if (pattern.at(i) != ')') {
					if (!isSmall(pattern.at(i)))
						throw string("baahhh!");
					m[pattern.at(i)] = true;
				} else {
					break;
				}
			}
		}
		p.push_back(m);
		sets++;
	}
	if (sets != l) {
		throw string("shit!");
	}
}


bool Pattern::isMatch(const string& str) {
	
	for (int i = 0; i < str.length(); i++) {
		if (!p[i][str.at(i)])
			return false;
	}
	return true;
}

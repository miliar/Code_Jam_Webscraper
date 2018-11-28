#include <iostream>
#include <list>
#include <map>
#include <set>

static std::pair<char,char> sort(std::pair<char,char> p) {
	if (p.second<p.first)
		std::swap(p.first, p.second);
	return p;
}

static std::pair<char,char> sortedPair(char a, char b) {
	return sort(std::make_pair(a,b));
}

static std::string runTest() {
	unsigned int N;
	std::map<std::pair<char, char>, char> c;
	std::set<std::pair<char, char> > o;
	std::cin >> N;
	for (unsigned int i=0; i<N; i++) {
		std::string s;
		std::cin >> s;
		c.insert(std::make_pair(sortedPair(s[0],s[1]), s[2]));
	}
	std::cin >> N;
	for (unsigned int i=0; i<N; i++) {
		std::string s;
		std::cin >> s;
		o.insert(sortedPair(s[0],s[1]));
	}
	std::string s;
	std::cin >> N >> s;
	std::string list;
	for (unsigned int i=0; i<s.size(); i++) {
		list += s[i];
		if (list.size()>=2) {
			std::map<std::pair<char,char>, char>::const_iterator it = c.find(sortedPair(list[list.size()-2], list[list.size()-1]));
			if (it!=c.end()) {
				list.resize(list.size()-1);
				list[list.size()-1] = it->second;
			} else {
				for (unsigned int j=0; j<list.size(); j++)
					if (o.find(sortedPair(list[j], s[i]))!=o.end())
						list.clear();
			}
		}
	}
	std::string res = "[";
	for (unsigned int i=0; i<list.size(); i++) {
		if (i!=0)
			res += ", ";
		res += list[i];
	}
	return res + "]";
}

int main() {
	unsigned int T;
	std::cin >> T;
	for (unsigned int i=0; i<T; i++)
		std::cout << "Case #" << (i+1) << ": " << runTest() << std::endl;
}


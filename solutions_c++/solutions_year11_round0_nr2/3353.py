#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <algorithm>
#include <string>
#include <map>
#include <exception>
using namespace std;

struct combination {
	char e;
	char r;
};

int main(int argc, char** argv) {
	try {
		ifstream ifs;
		ifs.exceptions(ifstream::failbit | ifstream::badbit);
		ifs.open(argv[1]);

		size_t T;
		ifs >> T;
		cerr << "T=" << T << endl;

		for (size_t j = 0; j < T; ++j) {

			multimap<char, combination> combinations;
			multimap<char, char> oppositions;

			size_t C;
			ifs >> C;
			for (size_t i = 0; i < C; ++i) {
				char e1, e2, r;
				ifs >> e1 >> e2 >> r;
				combination c1, c2;
				c1.e = e1;
				c1.r = r;
				c2.e = e2;
				c2.r = r;
				combinations.insert(pair<char, combination> (e2, c1));
				combinations.insert(pair<char, combination> (e1, c2));
			}

			size_t D;
			ifs >> D;
			for (size_t i = 0; i < D; ++i) {
				char a, b;
				ifs >> a >> b;
				oppositions.insert(pair<char, char> (a, b));
				oppositions.insert(pair<char, char> (b, a));
			}

			size_t N;
			ifs >> N;
			list<char> elems;
			list<char>::iterator last = elems.end();
			for (size_t i = 0; i < N; ++i) {
				char c;
				ifs >> c;
				bool flag = true;
				if (last != elems.end()) {
					pair<multimap<char, combination>::iterator, multimap<char,
							combination>::iterator> p =
							combinations.equal_range(c);
					for (multimap<char, combination>::iterator it = p.first; it
							!= p.second; ++it) {
						if ((*it).second.e == *last) {
							*last = (*it).second.r;
							flag = false;
							break;
						}
					}
					if (flag) {
						pair<multimap<char, char>::iterator, multimap<char,
								char>::iterator> q = oppositions.equal_range(c);
						for (multimap<char, char>::iterator it = q.first; it
								!= q.second; ++it) {
							for (list<char>::iterator lit = elems.begin(); lit != elems.end(); ++lit) {
								if (*lit == ((*it).second)) {
									elems.clear();
									last = elems.end();
									flag = false;
									break;
								}
							}
							if (!flag) break;
						}
					}
				}
				if (flag)
					last = elems.insert(elems.end(), c);
			}

			cout << "Case #" << j + 1 << ": [";
			list<char>::iterator it = elems.begin();
			if (it != elems.end()) {
				cout << *it;
				++it;
				for (; it != elems.end(); ++it) {
					cout << ", " << *it;
				}
			}
			cout << "]" << endl;
		}

	} catch (exception& ex) {
		cerr << "Exception: " << ex.what() << endl;
	}
}

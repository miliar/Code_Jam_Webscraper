#include <map>
#include <iostream>
#include <fstream>
#include <string>

typedef std::pair<int, int> Key;
typedef std::map<Key, int> Lookup;
Lookup lookup;

int count(const char * s, const char * q, int sl, int ql) 
{
	if (sl == 0) return 0;
	if (ql == 1) {
		int c = 0;
		for (int i = 0; i < sl; i++) if (s[i] == q[0]) c++;
		return c;
	}

	int sum = 0;
	for (int i = 0; i < sl; i++) {
		if (s[i] == q[0]) {
			Key k(sl-i-1, ql-1);
			Lookup::iterator ll = lookup.find(k);
			if (ll == lookup.end()) {
				int tmp = count((s+i+1), (q+1), sl-i-1, ql-1) % 10000;
				lookup.insert(std::make_pair(k, tmp));
				sum = (sum + tmp) % 10000;
			} else {
				sum = (sum + ll->second) % 10000;
			}
		}
	}
	return sum;
}

int main(int argc, char* argv[])
{
	const char * q = "welcome to code jam";
	int ql = strlen(q);

	std::ifstream f(argv[1]);
	int n;
	f >> n;
	std::string line;
	std::getline(f, line);

	for (int i = 0; i < n; i++) {
		std::getline(f, line);

		printf("Case #%d: %4.4d\n", (i+1), count(line.c_str(), q, line.length(), ql));

		lookup.clear();
	}
	return 0;
}


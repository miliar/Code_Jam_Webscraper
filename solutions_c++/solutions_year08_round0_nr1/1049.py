#define  _CRT_SECURE_NO_WARNINGS 1

#include <stdio.h>
#include <stdlib.h>
#include <bitset>
#include <map>
#include <string>
using namespace std;

char buf[4096];
typedef bitset<4096> Occurs;

class SavingUniverse {
	map<string, unsigned> name_to_idx;
	unsigned num_engines;
	unsigned num_queries;
public:
	SavingUniverse() {
		gets(buf);
		sscanf(buf, " %u", &num_engines);
		for(unsigned j = 0; j < num_engines; ++j) {
			gets(buf);
			name_to_idx[buf] = j;
		}
		gets(buf);
		sscanf(buf, " %u", &num_queries);
	}

	unsigned get_min_changes() {
		Occurs o;
		unsigned num_changes = 0;
		unsigned num_set = 0;
		for(unsigned j = 0; j < num_queries; ++j) {
			gets(buf);
			unsigned t = name_to_idx[buf];
			if(!o.test(t)) {
				++num_set;
				o.set(t);
				if(num_set == num_engines) {
					++num_changes;
					o.reset();
					o.set(t); num_set = 1;
				}
			}
		}
		return num_changes;
	}
};

int main(int argc, char* argv[]) {
	unsigned num_tests;
	gets(buf);
	sscanf(buf, " %u", &num_tests);
	for(unsigned j = 0; j < num_tests; ++j) {
		SavingUniverse S;
		printf("Case #%u: %u\n", j + 1, S.get_min_changes());
	}
	return 0;
}


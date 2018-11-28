#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <string>
#include <cstring>

#define DEB(x) std::cerr<<"TaChIdOk: "<<#x<<":("<<x<<")"<<std::endl

using namespace std;

char k1[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi"};
char k2[] = {"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"};
char k3[] = {"de kr kd eoya kw aej tysr re ujdr lkgc jv"};

char w1[] = {"our language is impossible to understand"};
char w2[] = {"there are twenty six factorial possibilities"};
char w3[] = {"so it is okay if you want to just give up"};

int main(int argc, char *argv[]) {

	std::map<char, char> key;

	for (int i = 0; i < 3; i++) {
	int count = 0;
	char c;
	do {

		if (i == 0) {
			c = k1[count];
		}
		else if (i == 1) {
			c = k2[count];
		}
		else {
			c = k3[count];
		}

		if (i == 0) {
			key[c] = w1[count];
		}
		else if (i == 1) {
			key[c] = w2[count];
		}
		else {
			key[c] = w3[count];
		}

		DEB(c);
		DEB(key[c]);

		count++;

	}while(c!=NULL);
	}

	key['q'] = 'z';
	key['z'] = 'q';

	string str, str_out;
	
	int n_examples;

	FILE *output;
	output = fopen("output.txt", "w");

	scanf("%d", &n_examples);
	getline(cin, str);

	DEB(n_examples);

	for (unsigned pp = 0; pp < n_examples; pp++) {

		str.clear();
		str_out.clear();
		getline(cin, str);
		
		unsigned str_size = str.size();
		str_out.resize(str_size);
		for (unsigned i = 0; i < str_size; i++) {

			str_out[i] = key[str[i]];

		}

		DEB(str.c_str());
		DEB(str_out.c_str());

		fprintf(output, "Case #%d: %s\n", pp+1, str_out.c_str());

	}

	fclose(output);

	return 1;

 }


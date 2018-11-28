#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string.h>
#include <climits>
#include <vector>
#include <queue>
#include <stack>
#include <regex.h>
#include <err.h>
#include <sys/types.h>
using namespace std;

static const int DMAX = 5000;

// einfach in regexp umwandeln, also () -> [], und auf alle loslassen 

int
main()
{
	int L, D, N;
	int wordscnt, matches;
	regex_t preg;
	string words[DMAX];
	string tmpstr;

	cin >> L >> D >> N;
	for (wordscnt = 0; wordscnt < D; wordscnt++) {
		cin >> words[wordscnt];
	}
	for (int cas = 1; cas <= N; cas++) {
		cin >> tmpstr;
		for (size_t i = 0; i < tmpstr.size(); i++) {
			if (tmpstr[i] == '(')
				tmpstr[i] = '[';
			else if (tmpstr[i] == ')')
				tmpstr[i] = ']';
		}

		if (regcomp(&preg, tmpstr.c_str(), REG_BASIC | REG_NOSUB) != 0)
			err(1, "regcomp");

		matches = 0;
		for (int i = 0; i < wordscnt; i++) {
			if (regexec(&preg, words[i].c_str(), 0, NULL, 0) == 0)
				matches++;
		}

		printf("Case #%d: %d\n", cas, matches);
	}

	return 0;
}

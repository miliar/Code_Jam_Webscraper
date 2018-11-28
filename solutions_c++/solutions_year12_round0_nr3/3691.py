#include <stdio.h>
#include <stdlib.h>
#include <map>
#include "codejam.h"

class RecycledNo : public CodeJam {
public:
    RecycledNo(FILE *fp) : CodeJam(fp) {
    }
    void solve(void) {
	for (int i = 0; i < cInput.size(); i++) {
	    int A, B;
	    int iCount = 0;

	    // Get A & B
	    sscanf(cInput[i].c_str(), "%d %d", &A, &B);
	    if (A < 10) {
		cOutput.push_back("0");
		continue;
	    }
	    //printf("%d %d\n", A, B);
	    // Go thru n
	    for (int n = A; n <= B; n++) {
		char buf[128];
		snprintf(buf, sizeof(buf), "%d", n);
		string N(buf);
		int len = N.size() - 1;
		map<int, int> cLookup;
		// Find all the possible m
		for (int j = 0; j < len; j++) {
		    string x = N.substr(len);
		    N.erase(len);
		    N = x + N;
		    //printf("s: %s\n", s.c_str());
		    int m = atoi(N.c_str());
		    if (!cLookup[m] && A <= n && n < m && m <= B) {
			iCount++;
			cLookup[m]++;
		    }
		}
	    }
	    char output[256];
	    snprintf(output, sizeof(output), "%d", iCount);
	    cOutput.push_back(output);
	}
    }
};

int main(void) {
    RecycledNo cRecycledNo(stdin);
    cRecycledNo.parseInput();
    cRecycledNo.solve();
    cRecycledNo.dumpOutput();
    return (0);
}

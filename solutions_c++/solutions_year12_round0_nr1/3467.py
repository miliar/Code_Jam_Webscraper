#ifndef CODEJAM_H
#define CODEJAM_H

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <vector>
#include <string>

using namespace std;

class CodeJam {
protected:
    FILE *fp;
    vector<string> cInput, cOutput;

public:
    CodeJam(FILE *fp = stdin) : fp(fp) {
    }
    virtual void parseInput(void) {
	char buf[256];
	int T;
	if (fgets(buf, sizeof(buf), fp) == NULL) {
	    perror("Parse error");
	    exit(-1);
	}
	T = atoi(buf);
	for (int t = 0; t < T; t++) {
	    if (fgets(buf, sizeof(buf), fp) == NULL) {
		perror("Parse error");
		exit(-1);
	    }
	    buf[strlen(buf) - 1] = 0;
	    cInput.push_back(buf);
	}
    }
    void dumpInput(void) {
	for (int i = 0; i < cInput.size(); i++) {
	    printf("[%s]\n", cInput[i].c_str());
	}
    }
    void dumpOutput(void) {
	for (int i = 0; i < cOutput.size(); i++) {
	    printf("Case #%d: %s\n", i + 1, cOutput[i].c_str());
	}
    }
    virtual void solve(void) = 0;
};

#endif // CODEJAM

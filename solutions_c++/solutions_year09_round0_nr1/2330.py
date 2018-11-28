#include <stdio.h>
#include <regex.h>
#include <memory.h>
#include <string>
#include <vector>

using namespace std;

class Regex : public re_pattern_buffer {
private:
    bool bOk;
    string cPattern;

public:
    Regex(const char *pzcPattern) : bOk(true), cPattern(pzcPattern) {
        memset(this, 0, sizeof(re_pattern_buffer));
        // Set the syntax option
        // RE_INTERVALS makes it recognize { } operation
        // RE_NO_BK_BRACES makes it use { and } instead of \{ and \}
        re_set_syntax(RE_INTERVALS | RE_NO_BK_BRACES);
        // Compile the RE
        if (re_compile_pattern(pzcPattern, strlen(pzcPattern), this) != NULL) {
            fprintf(stderr, "Failed to compile RE!\n");
            bOk = false;
        }
    }
    const bool ok(void) const {
        return (bOk);
    }
    const char *pattern(void) const {
	return (cPattern.c_str());
    }
    // Match the provide text against the pattern
    bool match(const char *pzcText) {
	if (re_match(this, pzcText, strlen(pzcText), 0, NULL) >= 0) {
	    return (true);
	} else {
	    return (false);
	}
    }
};

static vector<string> cDict;
static vector<Regex> cTest;

int main(void) {
    int l, d, n;

    // Read the spec
    do {
	// Read 1st line
	if (fscanf(stdin, "%d %d %d", &l, &d, &n) != 3) {
	    fprintf(stderr, "Parse error!\n");
	    break;
	}
	//printf("%d %d %d\n", l, d, n);

	// Read dictionary words
	for (int i = 0; i < d; i++) {
	    char pzcWord[128];
	    if (fscanf(stdin, "%s", pzcWord) != 1) {
		fprintf(stderr, "Parse error!\n");
		break;
	    } else {
		//printf("[%s]\n", pzcWord);
		cDict.push_back(pzcWord);
	    }
	}

	// Read test cases
	for (int i = 0; i < n; i++) {
	    char pzcTest[1024];
	    if (fscanf(stdin, "%s", pzcTest) != 1) {
		fprintf(stderr, "Parse error!\n");
		break;
	    } else {
		// Replace ( and ) with [ and ] respectively
		char *p = pzcTest;
		while (p && *p) {
		    if (*p == '(') {
			*p = '[';
		    } else if (*p == ')') {
			*p = ']';
		    }
		    p++;
		}
		//printf("[%s]\n", pzcTest);
		cTest.push_back(Regex(pzcTest));
		if (!cTest[cTest.size() - 1].ok()) {
		    fprintf(stderr, "Regex error!\n");
		    break;
		}
	    }
	}

    } while (0);

    // Compare the result
    vector<int> cResult;
    for (int i = 0; i < cTest.size(); i++) {
	int iMatch = 0;
	for (int j = 0; j < cDict.size(); j++) {
	    if (cTest[i].match(cDict[j].c_str())) {
		iMatch++;
	    }
	}
	cResult.push_back(iMatch);
    }

    // Output the result
    for (int i = 0; i < cResult.size(); i++) {
	printf("Case #%d: %d\n", i + 1, cResult[i]);
    }

    return (0);
}

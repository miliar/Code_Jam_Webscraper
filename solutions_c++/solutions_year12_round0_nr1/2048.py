#include <cstdio>
#include <iostream>

#include <string>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <bitset>

#include <algorithm>

#define INPUT_INT(inp) scanf("%d", &(inp));
#define INPUT_LNG(inp) scanf("%ld", &(inp));
#define INPUT_DBL(inp) scanf("%f", &(inp));
#define INPUT_STR(inp) scanf("%s", inp);

#define OUTPUT_INT(i, val) printf("Case #%d: %d\n", (i), (val));
#define OUTPUT_LNG(i, val) printf("Case #%d: %ld\n",(i), (val));
#define OUTPUT_LNGLNG(i, val) printf("Case #%d: %lld\n",(i), (val));
#define OUTPUT_DBL(i, val) printf("Case #%d: %f\n", (i), (val));
#define OUTPUT_STR(i, str) printf("Case #%d: %s\n", (i), (str));

#define FOR(i, start, end) for(i = start; i < end; i++)
#define ROF(i, end, start) for(i = end - 1; i >= start; i--)

using namespace std;

// Declare globals here
static void solve(int);
static void learn_to_translate();
bool learnt = false;

map<char, char> mapping;

void learn_to_translate(const char* foreign, const char* english)
{
    int i = 0;
    while (foreign[i] != '\0') {

	if (foreign[i] == ' ') {
	    // skip spaces
	    i++;
	    continue;
	}

	if (mapping.find(foreign[i]) == mapping.end()) {
	    // Add to mapping
	    pair<char, char> pr(foreign[i], english[i]);
	    mapping.insert(pr);
	}
	i++;
    }
    
}
void solve(int testcase)
{
    // Declarations
    int x = 0;
    string G;

    if (!learnt) {
     
       // First do learning
	mapping['z'] = 'q';

        // Here's the missing piece
	mapping['q'] = 'z';

        learn_to_translate("ejp mysljylc kd kxveddknmc re jsicpdrysi",
		           "our language is impossible to understand");

        learn_to_translate("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
	   	           "there are twenty six factorial possibilities");

	learn_to_translate("de kr kd eoya kw aej tysr re ujdr lkgc jv",
		           "so it is okay if you want to just give up");

	learnt = true;
    }

    // Then do solving
    getline (cin, G);
    //printf("\nG = %s", G.c_str());
    
    int i = 0;
    while (G[i] != '\0') {

	if (G[i] == ' ') {
	    i++;
	    continue;
	}

	G[i] = mapping[G[i]];
	i++;
    }   

    // Output
    OUTPUT_STR(testcase, G.c_str());
    G.clear();

}

int main()
{
    // Declarations
    int N = 0, testcase = 1;

    // Get number of cases
    INPUT_INT(N);

    string G;
    getline(cin, G);

    while (N--) {
	solve(testcase++);
    }

    return 0;
}


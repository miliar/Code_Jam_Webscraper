#include <cstdio>

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

void solve(int testcase)
{
    // Declarations
    int N, S, p, i, temp;
    vector<int> t;
    
    int best_googlers = 0;
    int average;    

    // Scan Input
    INPUT_INT(N);
    INPUT_INT(S);
    INPUT_INT(p);

    t.reserve(N);
    FOR(i, 0, N) {
	INPUT_INT(temp);
	t.push_back(temp);
    }
   
    // sorting may not be required 
    sort(t.begin(), t.end());
    reverse(t.begin(), t.end());

    // Calculations
    FOR(i, 0, N) {
	
	average = (int) (t[i] / 3);
	if (t[i] % 3 == 0) {
	   
	    if (average >= p) {
		// best_googler without surprise
		best_googlers++;

	    } else if (average + 1 <= t[i] &&
		       average + 1 >= p &&
		       S > 0) {
		// best_googler with surprise
		S--;
		best_googlers++;
	    }

	} else if (t[i] % 3 == 1) {
	    
	    // No surprises possible
	    if (average + 1 >= p) {
		best_googlers++;
	    }

	} else if (t[i] % 3 == 2) {

	    if (average + 1 >= p) {
		// best_googler without surprise
		best_googlers++;
	    } else if (average + 2 >= p &&
		       S > 0) {
		// best_googler with surprise
		S--;
		best_googlers++;
	    }
	}
    }

    // Output
    OUTPUT_INT(testcase, best_googlers);
}

int main()
{
    // Declarations
    int N = 0, testcase = 1;

    // Get number of cases
    INPUT_INT(N);

    while (N--) {
	solve(testcase++);
    }

    return 0;
}


#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <complex>
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
#include <cctype>
#include <climits>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int, int> PII;
//typedef long long LL;
typedef complex<double> tComp;

int count(string path, set<string> &paths) {
    if (path.empty()) {
        return 0;
    }
    if (paths.find(path) != paths.end()) {
        return 0;
    }

    int t = 1 + count(path.substr(0, path.find_last_of("/")), paths);
    paths.insert(path);
    return t;

}

int main(int argc, char **argv) {
//      freopen("A.in","r",stdin);

//       freopen("A-small-attempt0.in","r",stdin);
//       freopen("A-small-attempt0.out","w",stdout);

//      freopen("A-small-attempt1.in","r",stdin);
//      freopen("A-small-attempt1.out","w",stdout);

//     freopen("A-small-attempt2.in","r",stdin);
//     freopen("A-small-attempt2.out","w",stdout);

      freopen("A-large.in","r",stdin);
      freopen("A-large.out","w",stdout);

    int ntestcases = 0;
    scanf("%d\n", &ntestcases);

    int testcase = 0;
    while (testcase < ntestcases) {

        int N = 0;
        int M = 0;
        scanf("%d %d\n", &N, &M);

        set<string> paths;
        for (int i = 0; i < N; ++i) {
            string line;
            getline(cin, line);
            paths.insert(line);
        }

        int sum = 0;
        for (int i = 0; i < M; ++i) {
            string line;
            getline(cin, line);
//             cout << "set" << endl;
//             copy(paths.begin(), paths.end(),
//                  ostream_iterator<string>(cout, "\n"));
            sum += count(line, paths);
        }

        printf("Case #%d: %d", testcase + 1, sum);

        printf("\n");

        ++testcase;
    }

    return 0;
}

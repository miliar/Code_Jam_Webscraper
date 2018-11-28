#include <cstdio>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
using namespace std;

//by Skyly

typedef long long int64;
typedef vector<int> vint;

#define SIZE(X) ((int)((X).size())) 
#define ALL(X) (X).begin(), (X).end()
#define FOR(IT, X) for (__typeof((X).begin()) IT = (X).begin(); IT != (X).end(); ++IT)

template<typename T> string toStr(const T &x) { ostringstream os; os << x; return os.str(); }
template<typename T> void toMin(T &x, const T &y) { x = min(x, y); }
template<typename T> void toMax(T &x, const T &y) { x = max(x, y); }

int main() {
    int t, casN = 0;
    const char *trans = "yhesocvxduiglbkrztnwjpfmaq";
    char buf[105];

    fgets(buf, 105, stdin);
    sscanf(buf, "%d", &t);
    while (t-- > 0) {
        fgets(buf, 105, stdin);
        printf("Case #%d: ", ++casN);
        for (int i = 0; ('a' <= buf[i] && buf[i] <= 'z') || buf[i] == ' '; i++) {
            if (buf[i] == ' ') putchar(' ');
            else putchar(trans[buf[i] - 'a']);
        }
        putchar('\n');
    }

    return 0;
}


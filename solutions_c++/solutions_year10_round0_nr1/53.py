#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <cstdio>
#include <cmath>
#include <queue>
#include <sstream>
#include <map>
#include <set>
#include <stack>
using namespace std;

typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<char> VC;
typedef vector<VI> VVI;
typedef vector<VC> VVC;
typedef vector<bool> VVB;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000000;

int main() {
    int casos;
    cin >> casos;
    for (int z = 1; z <= casos; ++z) {
        cout << "Case #" << z << ": ";
        long long n, k;
        cin >> n >> k;
        long long periodo = 1 <<n;
        k = k%periodo;
        if (k== periodo - 1) cout << "ON" << endl;
        else cout << "OFF" << endl;
    }
}

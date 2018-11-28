#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <stack>
using namespace std;

#define x first
#define y second

typedef long long ll;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<ll> VL;
typedef vector<VL> VVL;
typedef vector<char> VC;
typedef vector<VC> VVC;
typedef vector<string> VS;
typedef vector<VS> VVS;
typedef pair<int, int> PII;
const int INF = 1000000000;
 
int main() {
    int k, caso = 1;
    cin >> k;
    while (k--) {
        string s;
        cin >> s;
        if (not next_permutation(s.begin(), s.end())) {
            sort(s.begin(), s.end());
            int i;
            for (i = 0; i < s.size() and s[i] == '0'; ++i);
            swap(s[i], s[0]);
            s.insert(1,1, '0');
        }
        cout << "Case #" << caso++ << ": " << s << endl;
    }
}

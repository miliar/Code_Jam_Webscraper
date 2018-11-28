#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std;

const int MAXN = 1005;

int cc;

string a;

char t[27] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
    scanf("%d\n", &cc);
    for (int cas = 1; cas <= cc; cas++) {
        cout << "Case #" << cas << ": ";
        getline(cin, a);
        for (int i = 0; i < a.size(); i++) {
            if (a[i] == ' ') cout << ' ';
            else printf("%c", t[a[i] - 'a']);
        }
        cout << endl;
    }
	return 0;
}
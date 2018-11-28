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

#define MAXN 1005

int cc;
int n, k;
bool res;

vector <int> nei[MAXN];

bool v[MAXN];

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
    scanf("%d", &cc);
    for (int cas = 1; cas <= cc; cas++) {
        res = false;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &k);
            nei[i].clear();
            for (int j = 0, a; j < k; j++) {
                scanf("%d", &a);
                nei[i].push_back(a - 1);
            }
        }
        for (int i = 0; i < n && res == false; i++) {
            memset(v, 0, sizeof(v));
            queue <int> Q;
            Q.push(i);
            while (!Q.empty() && res == false) {
                int node = Q.front();
                Q.pop();
                if (v[node] == true) res = true;
                v[node] = true;
                for (int j = 0; j < nei[node].size(); j++) Q.push(nei[node][j]);
            }
        }
        cout << "Case #" << cas << ": ";
        if (res == true) cout << "Yes" << endl;
        else cout << "No" << endl;
    }
	return 0;
}
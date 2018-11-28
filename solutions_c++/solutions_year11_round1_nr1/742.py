#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int process() {
    long long n,pd,pg;
    cin >>n>>pd>>pg;
    if ((pg == 100) && (pd < 100)) return 0;
    if ((pg == 0) && (pd > 0)) return 0;
    
    if ((pd != 0) && (pd * n/100 < 1)) return 0;
    int i;
    for (i = 1; (i <= n) && (i <= 100); i++) if (pd * i % 100 == 0)return 1;
    return 0;
}

int main() {
    freopen("A-large.in","rt",stdin);
    freopen("A.out","wt",stdout);
    int T,i;
    cin >> T;
    for (i = 1; i <= T;i ++) {
        cout <<"Case #"<<i;
        if (process() == 1) cout << ": Possible\n"; 
        else cout <<": Broken \n";
    }
}

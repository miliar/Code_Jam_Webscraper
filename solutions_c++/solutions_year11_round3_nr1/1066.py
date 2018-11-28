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

int main() {
    int T;
    int R,C;

    cin >> T;
    for(int tc=1;tc<=T;tc++) {
        cin >> R >> C;

        vector<string> m(R);
        for(int i=0;i<R;i++) cin >> m[i];

        for(int i=0;i<R-1;i++) {
            for(int j=0;j<C-1;j++) {
                if(m[i][j]=='#' && m[i][j+1]=='#' &&
                    m[i+1][j]=='#' && m[i+1][j+1]=='#') {
                    m[i][j]='/'; m[i][j+1]='\\';
                    m[i+1][j]='\\'; m[i+1][j+1]='/';
                }
            }
        }

        bool f = true;
        for(int i=0;i<R;i++)
            for(int j=0;j<C;j++)
                if(m[i][j]=='#') { f=false; goto end; }

end:
        printf("Case #%d:\n", tc);
        if(f) {
            for(int i=0;i<R;i++) cout << m[i] << endl;
        } else {
            puts("Impossible");
        }
    }

    return 0;
}

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
 
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) (a).begin(),a.end()
#define SORT(a) sort(ALL(a))
#define SZ(a) ((int) a.size())
#define pb push_back
char str[50005];
int len;
int k;
vector<int> per;
int main() {
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D-small-attempt1.out", "w", stdout);
    int T, cnt = 0;
    scanf("%d", &T);
    while (T--) {
           scanf("%d", &k);
           getchar();
           gets(str);
           per.clear();
           for (int i = 0; i < k; i++) {
                per.push_back(i+1);
           }
           len = strlen(str);
           int res = (1<<25);
           do {
               char ch = str[per[0]-1];
               int tmp = 1;
               for (int i = 1; i < len; i++) {
                    //printf("%d %d %d\n", i, ((i)/k)*k, ((i)/k)*k+per[i%k]-1);
                    if (ch == str[((i)/k)*k+per[i%k]-1]) {
                        continue;
                    }
                    else {
                        ch = str[((i)/k)*k+per[i%k]-1];
                        tmp++;
                    }
               }
               if (res > tmp)
                   res = tmp;
           }while (next_permutation(per.begin(), per.end()));
           printf("Case #%d: %d\n", ++cnt, res);
    }
}

#include <cmath>
#include <ctime>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;

#define debug(args...) fprintf(stderr,args);

typedef long long lint;
typedef pair<int,int> pii;

const int INF = 0x3f3f3f3f;

int tt,n,s,p;

int main() {
    scanf("%d",&tt);
    for(int t=1;t<=tt;++t) {
        printf("Case #%d: ",t);
        scanf("%d%d%d",&n,&s,&p);
        int ret=0,tot;        
        for(int a=0;a<n;++a) {
            scanf("%d",&tot);
            int best = (tot+2)/3;
            if(best >= p) ++ret;
            else if(s && best==p-1 && tot%3!=1 && tot>1) {
                --s;
                ++ret;
            }
        }
        printf("%d\n",ret);
    }
    return 0;
}

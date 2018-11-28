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

int from,to;

int stoi(char *s,int len) {
    int ret=0;
    for(int a=0;a<len;++a) ret = 10*ret+s[a]-'0';
    return ret;
}

int mp[2100000];
char s[10];

int find(int n) {
    int len = sprintf(s,"%d",n);
    int ret=0;
    for(int a=1;a<len;++a) {
        rotate(s,s+1,s+len);
        if(s[0]=='0') continue;
        int cyc = stoi(s,len);
        if(n<cyc && cyc<=to && mp[cyc] != n) {
            ++ret;
            mp[cyc] = n;
        }
    }
    return ret;
}

int main() {
    int tt;
    scanf("%d",&tt);
    for(int t=1;t<=tt;++t) {
        memset(mp,0,sizeof(mp));
        printf("Case #%d: ",t);
        int ret=0;
        scanf("%d%d",&from,&to);
        for(int a=from;a<=to;++a) {
            ret += find(a);
        }
        printf("%d\n",ret);
    }
    return 0;
}

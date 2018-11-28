#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <sstream>
#include <queue>
using namespace std;
#define out(x) (cout<<#x<<": "<<x<<endl)
const int maxint=0x7FFFFFFF;
typedef long long lint;
template<class T>void show(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void show(T a, int r, int l){for(int i=0; i<r; ++i)show(a[i],l);cout<<endl;}

char mp[64];


char in[500] = 
"ejp mysljylc kd kxveddknmc re jsicpdrysi"
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
"de kr kd eoya kw aej tysr re ujdr lkgc jv";

char ans[500] =
"our language is impossible to understand"
"there are twenty six factorial possibilities"
"so it is okay if you want to just give up";


void init() {
    memset(mp, 0, sizeof(mp));
    for (char c = 'a'; c <= 'z'; ++c) {
        mp[c - 'a'] = c;
    }
    mp['z' - 'a'] = 'q';
    mp['q' - 'a'] = 'z';
    int len = strlen(in);
    for (int i=0; i<len; ++i) {
        if(in[i] == ' ') continue;
        mp[in[i] - 'a'] = ans[i];
    }
}
char tmp[500];
int main()
{
    init();
    int ca;
    scanf("%d\n", &ca);
    for (int z=1; z<=ca; ++z) {
        gets(tmp);
        int len = strlen(tmp);
        for (int i=0; i<len; ++i) {
            if (tmp[i] == ' ') continue;
            tmp[i] = mp[tmp[i] - 'a'];
        }
        printf("Case #%d: %s\n", z, tmp);
    }
    return 0;
}


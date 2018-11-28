#include <cstdio>
#include <cstring>
#include <algorithm>

#define REP(i,n) for(int i=1;i<=n;++i)
using namespace std;

int main()
{
    int T;
    char number[63];
    int map[256];
    int base;
    int num[]={-1,1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47};
    long long out;
    scanf("%d",&T);
    REP(n,T) {
        scanf("%s",number);
        base = 0;
        memset(map, -1, sizeof(map));
        for(int i=0;number[i]!=0;++i) {
            if (map[number[i]]==-1) {
                map[number[i]]=num[++base];
            }
        }
        out=1LL;
        if (base==1) base=2;
        for(int i=1;number[i]!=0;++i) {
            out = out*base + map[number[i]];
        }
        printf("Case #%d: %lld\n",n,out);
    }
    return 0;
}

using namespace std;
#include <iostream>
#include <cstdio>
#include <cstring>
#include <numeric>
#include <utility>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <cassert>

#define out(x) (cout<<#x<<": "<<x<<endl)

template<class T>
inline int lth(const T &x) {return static_cast<int>(x.size()); }

const char *pn = "welcome to code jam";
const int N = 19;
int dp[100];
const int Mod = 10000;

char buf[1000];
inline void ox(int x) {
    if(x<10) {
        printf("000%d\n",x);
    }else if(x<100) {
        printf("00%d\n",x);
    }else if(x<1000) {
        printf("0%d\n",x);
    }else {
        printf("%d\n",x);
    }
}
int main(int argc,char **argv) {
    freopen(argv[1],"r",stdin);
    freopen(argv[2],"w",stdout);

    int Kse;
    scanf("%d",&Kse);
    getchar();
    for(int k=1;k<=Kse;++k) {
        gets(buf+1);
        memset(dp,0,sizeof(dp));
        dp[0]=1;

        for(char *p=buf+1;*p;++p) {
            for(int i=N;i>=1;--i) {
                if(dp[i-1] && pn[i-1]==*p) {
                    dp[i] += dp[i-1];
                    dp[i] %= Mod;
                }
            }
        }
        printf("Case #%d: ",k); 
        ox(dp[N]);
    }
    return 0;
}




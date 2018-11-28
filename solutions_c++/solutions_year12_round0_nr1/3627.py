#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

#define PB push_back
#define MP make_pair
#define INF 1000000000
#define PI 4.0*atan(1.0)

#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

char arrs[30]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
char ch[110];
int ttt;

int main(){
    //freopen("A-small-attempt2 (1).in", "r", stdin);
    //freopen("A-small-attempt0.out", "w", stdout);

    while ( EOF != scanf("%d", &ttt) ){
        getchar();
        int t = 1;
       while(t <= ttt){
            gets(ch);
            int len = strlen(ch);
            printf("Case #%d: ", t);
            for ( int i = 0 ; i < len ; i++ )
                if (' '==ch[i])
                    printf(" ");
                else printf("%c", arrs[ch[i]-'a']);
            printf("\n");
            t++;
        }
    }
    return 0;
}


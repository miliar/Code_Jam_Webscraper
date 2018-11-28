#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

#define FORALL(a,b) for(typeof((b).begin()) a = (b).begin(); a != (b).end(); ++a)
#define FOR(i,a,b) for(int i = a; i < (int)(b); ++i)

typedef long long LL;

const double EPS = 1e-6;
const int INF = 1<<29;

char in[3][60]={"ejp mysljylc kd kxveddknmc re jsicpdrysi",
              "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
              "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
char out[3][60]={"our language is impossible to understand",
                 "there are twenty six factorial possibilities",
                 "so it is okay if you want to just give up"};
char to[300]={};

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    for (int i = 0; i < 3; ++i)
        for (int j = 0; in[i][j]; ++j){
            to[in[i][j]+0] = out[i][j];
        }
    to['z'+0] = 'q';
    to['q'+0] = 'z';
//    for (int i = 'a'; i <= 'z'; ++i) printf("%c %c\n", i, to[i]);
    int t, cas = 0;
    char str[150];
    scanf("%d", &t);
    gets(str);
    while (t--){
        gets(str);
        printf("Case #%d: ", ++cas);
        for (int i = 0; str[i]; ++i) str[i] = to[str[i]+0];
        puts(str);
    }
    return 0;
}


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>

#include <vector>
#include <list>
#include <map>
#include <queue>
#include <algorithm>
#include <cmath>
#include <set>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef vector<int>::iterator VII;
typedef set<int>::iterator SII;
#define FOR(i,n) for(int i = 0; i<(n); i++)
#define FORD(i,n) for(int i=(n)-1; i>=0; i--)
#define FOR1(i,n) for(int i=1; i<=(n); i++)
#define FOR1D(i,n) for(int i=(n); i>=1; i--)
#define NL printf("\n")

//sort(t.begin(),t.end(),greater<int>()); // malejaco
//sort(t.begin(),t.end(),less<int>()); // rosnaco
//char buf[500]; gets(buf); stringstream ss(buf); int x; while(ss > x) {}


int main() {

    char buf[1024];
    int tests;

    gets(buf);

    tests = atoi(buf);

    FOR(t,tests) {
        gets(buf);
        int dl = strlen(buf);
//        printf("dl = %d\n",dl);
        if (next_permutation(buf,buf+dl)) {
        printf("Case #%d: %s\n",t+1,buf);
        }
        else {
            buf[dl] = '0';
            dl++;
            buf[dl] = 0;
            sort(buf,buf + dl , less<char>());
            if (buf[0] == '0') {
                for (int i = 1; i < dl; ++i)
                    if (buf[i] != '0') {
                        swap(buf[i],buf[0]);
                        break;
                    }
                printf("Case #%d: %s\n",t+1,buf);
                
            } else {
                printf("Case #%d: %s\n",t+1,buf);
            }
 //           printf("Case #%d: %c",t+1,buf[0]);
 //           printf("0");
 //           for (int i = 1; i < dl; ++i)
 //               printf("%c",buf[i]);
 //           NL;
        }
//        printf("Case #%d: %s\n",t+1,buf);
    }

    return 0;

}


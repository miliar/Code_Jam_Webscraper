#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctype.h>
#include <vector>
#include <iostream>

using namespace std;

#define FOREACH( i, C ) for( __typeof(C.begin())i = C.begin(); i != C.end(); ++i )
#define CLEAR( V )      memset( V, 0, sizeof(V) )
#define LEN 19

const char* tmp = "welcome to code jam";
int map[257];
char txt[501];
int len;
int N;

vector<int> V[LEN+1];

long long S = 0;

long long count(char c, int onpos, int frompos) {
    long long ss = 0, s =0;

    FOREACH(it, V[map[c]]) {
        if (*it >= frompos) {
            ss++;

            if ( onpos < LEN - 1) {

                long long mmm = count(tmp[onpos+1], onpos+1, *it);
                if ( mmm > 0 ) {
                    s = (s + mmm) % 10000;
                }
                else break;
            }
            else {
                s = (ss);
            }
        }
    }


    return s % 10000;
}

int main()
{    
    memset(map, 257, sizeof(map));
    for (int i = 0; i < LEN; ++i) {
        map[tmp[i]] = i;
    }


    scanf("%d\n", &N);

    char c;
    for (int no = 1; no <= N; ++no) {
        len = 0;
        CLEAR(txt);
        for (int i = 0; i <= LEN; ++i) V[i].clear();

        while( (c = getchar()) != '\n') {

            if ( (islower(c) || c==' ')&& (map[c] <= LEN) ) {
                txt[len] = c;

                V[map[c]].push_back(len);
                len++;
            }
        }


        S = count(tmp[0], 0, 0);

        printf("Case #%d: ", no);
        cout.width(4);
        cout.fill('0');

        cout << S << endl;

    }
    return 0;
}

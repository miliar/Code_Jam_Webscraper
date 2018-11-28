#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

#define MAX_LEN     (17)
int R, C;

set<string> visited;

const char NA = 'a' - 1;
#define encode(buf,x,y,p1x,p1y,p2x,p2y) {\
    buf[0] = NA + x;\
    buf[1] = NA + y;\
    buf[2] = NA + p1x;\
    buf[3] = NA + p1y;\
    buf[4] = NA + p2x;\
    buf[5] = NA + p2y;\
}

inline void decode(const string& s, int&x, int&y, int&p1x, int&p1y, int&p2x, int&p2y) {
    x = s[0] - NA;
    y = s[1] - NA;
    p1x = s[2] - NA;
    p1y = s[3] - NA;
    p2x = s[4] - NA;
    p2y = s[5] - NA;
}

vector<string> queue;
vector<string> nextqueue;
bool wall[MAX_LEN][MAX_LEN];
                        //printf("added to queue (%d %d) (%d %d) (%d %d) %s\n", cx, cy, p1x, p1y, p2x, p2y, buf);\

#define process(buf,cx,cy,p1x,p1y,p2x,p2y,queue) {\
                    encode(buf, cx, cy, p1x, p1y, p2x, p2y);\
                    if (visited.find(buf) == visited.end()) {\
                        visited.insert(buf);\
                        queue.push_back(buf);\
                    }\
}

int portalShootD[MAX_LEN][MAX_LEN][4];
int TR, TC;
int main() {
    int NTc;
    scanf("%d", &NTc);
    int i, j, k;
    char buf[1024];
    for (int tc = 0; tc < NTc; tc++) {
        printf("Case #%d: ", tc+1);
        
        scanf("%d %d", &R, &C);
        memset(wall, 1, sizeof(wall));

        int sR, sC, cR, cC;
        
        for (i = 1; i <= R; i++) {
            scanf("%s", buf);
            for (j = 1; j <= C; j++) {
                wall[i][j] = false;
                switch(buf[j-1]) {
                case 'O': sR = i, sC = j; break;
                case 'X': cR = i, cC = j; break;
                case '#': wall[i][j] = true; 
                }
            }
        }
        queue.clear();
        visited.clear();
        
        if (sR == cR && sC == cC) {
            printf("0\n");
            continue;
        }

        for (i = 1; i <= R; i++) {
            for (j = 1; j <= C; j++) {
                if (wall[i][j]) continue;
                
                k = i;
                while (!wall[k-1][j]) k--;
                portalShootD[i][j][0] = k;

                k = i;
                while (!wall[k+1][j]) k++;
                portalShootD[i][j][1] = k;

                k = j;
                while (!wall[i][k-1]) k--;
                portalShootD[i][j][2] = k;

                k = j;
                while (!wall[i][k+1]) k++;
                portalShootD[i][j][3] = k;
            }
        }        
        memset(buf, 0, sizeof(buf));
        encode(buf, sR, sC, 0, 0, 0, 0);
        queue.push_back(buf);
        int currR, currC, p1r, p1c, p2r, p2c;
        int res = 0;
        
        bool found = false;
        while (true) {
            nextqueue.clear();
            for (i = 0; i < queue.size(); i++) {
                string& s = queue[i];
                string next;
                decode(s.c_str(), currR, currC, p1r, p1c, p2r, p2c);
                //printf("queue[%d] = (%d %d) (%d %d) (%d %d)\n", i, currR, currC, p1r, p1c, p2r, p2c);
                if (currR == cR && currC == cC) {
                    found = true;
                    goto finished;
                }
                if (!wall[currR-1][currC]) process(buf, currR-1, currC, p1r, p1c, p2r, p2c, nextqueue);
                if (!wall[currR+1][currC]) process(buf, currR+1, currC, p1r, p1c, p2r, p2c, nextqueue);
                if (!wall[currR][currC-1]) process(buf, currR, currC-1, p1r, p1c, p2r, p2c, nextqueue);
                if (!wall[currR][currC+1]) process(buf, currR, currC+1, p1r, p1c, p2r, p2c, nextqueue);
                if (p2r && p2c && currR == p1r && currC == p1c) process(buf, p2r, p2c, p1r, p1c, p2r, p2c, nextqueue);
                if (p1r && p1c && currR == p2r && currC == p2c) process(buf, p1r, p1c, p1r, p1c, p2r, p2c, nextqueue);
                process(buf, currR, currC, portalShootD[currR][currC][0], currC, p2r, p2c, queue);
                process(buf, currR, currC, portalShootD[currR][currC][1], currC, p2r, p2c, queue);
                process(buf, currR, currC, currR, portalShootD[currR][currC][2], p2r, p2c, queue);
                process(buf, currR, currC, currR, portalShootD[currR][currC][3], p2r, p2c, queue);
                process(buf, currR, currC, p1r, p1c, portalShootD[currR][currC][0], currC, queue);
                process(buf, currR, currC, p1r, p1c, portalShootD[currR][currC][1], currC, queue);
                process(buf, currR, currC, p1r, p1c, currR, portalShootD[currR][currC][2], queue);
                process(buf, currR, currC, p1r, p1c, currR, portalShootD[currR][currC][3], queue);
            }
            if (nextqueue.size() == 0) break;
            queue = nextqueue;
            res++;
        }                
        finished:
        if (found) printf("%d\n", res);
        else printf("THE CAKE IS A LIE\n");
    }
    return 0;
}

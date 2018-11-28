#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int fromHex(char ch) {
    if('0' <= ch && ch <= '9')return ch-'0';
    if('A' <= ch && ch <= 'F')return ch-'A'+10;
    while(true){printf("!!!!\n");fflush(stdout);}
    return -1;
}

int main(int argc, char **argv) {
    int tc; scanf("%d\n", &tc);
    for(int tci = 0; tci < tc; tci++) {
        int m,n; scanf("%d%d\n", &m, &n);
        static int tbl[512][512];
        for(int y = 0; y < m; y++) {
            static char line[512];
            scanf("%s\n", line);
            for(int xx = 0; xx*4 < n; xx++) {
                int val = fromHex(line[xx]);
                val ^= 5;
                if(y&1)val ^= 15;
                for(int i = 0; i < 4; i++) {
                    tbl[y][xx*4+i]=(val>>(3-i))&1;
                }
            }
            //for(int x = 0; x < n; x++) {
            //    printf("%d,",tbl[y][x]);
            //}printf("\n");
        }
        static int ctbl0[512][512];
        static int ctbl1[512][512];
        vector<pair<int,int> > v;
        for(int s = min(n,m); s >= 1; s--) {
            int scnt = 0;
            for(int y = 0; y < m; y++) {
                int cnts[3];
                cnts[0]=cnts[1]=cnts[2]=0;
                for(int x = 0; x <= n; x++) {
                    if(x>=s) {
                        ctbl0[y][x-s] = 
                            cnts[2] ? 2 :
                            cnts[1] ? (cnts[0] ? 2 : 1) : 0
                            ;
                        cnts[tbl[y][x-s]]--;
                    }
                    if(x<n)cnts[tbl[y][x]]++;
                }
            }
            for(int x = 0; x+s <= n; x++) {
                int cnts[3];
                cnts[0]=cnts[1]=cnts[2]=0;
                for(int y = 0; y <= m; y++) {
                    if(y>=s) {
                        ctbl1[y-s][x] = 
                            cnts[2] ? 2 :
                            cnts[1] ? (cnts[0] ? 2 : 1) : 0
                            ;
                        cnts[ctbl0[y-s][x]]--;
                    }
                    if(y<m)cnts[ctbl0[y][x]]++;
                }
            }
            //printf("s=%d:\n",s);
            //for(int y = 0; y+s <= m; y++) {
            //    for(int x = 0; x+s <= n; x++) {
            //        printf("%d,",ctbl1[y][x]);
            //    }printf("\n");
            //}
            for(int y = 0; y+s <= m; y++) {
                for(int x = 0; x+s <= n; x++) {
                    if(ctbl1[y][x]!=2) {
                        scnt++;
                        //printf("scnt++ at %d,%d\n",y,x);
                        for(int yy = y; yy < y+s; yy++) {
                            for(int xx = x; xx < x+s; xx++) {
                                tbl[yy][xx]=2;
                            }
                        }
                        for(int yy = max(y-s+1,0);
                                yy < min(y+s,m); yy++) {
                            for(int xx = max(x-s+1,0);
                                    xx < min(x+s,n); xx++) {
                                ctbl1[yy][xx]=2;
                            }
                        }
                    }
                }
            }
            if(scnt)v.push_back(make_pair(s,scnt));
        }
        printf("Case #%d: %d\n",tci+1, v.size());
        for(int i = 0; i < (int)v.size(); i++) {
            printf("%d %d\n",v[i].first,v[i].second);
        }
    }
    return 0;
}


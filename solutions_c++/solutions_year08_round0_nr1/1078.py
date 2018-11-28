#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
using namespace std;

#define INF             10000

int main() {
        int T, N,M;
        int i,j,k,tt;
        string engine[100], query[1000];
        int ret,m;

        cin >> T;
        for(tt=1;T--;tt++) {
                cin >> N; while(getc(stdin)!='\n');
                for(i=0;i<N;i++) getline(cin, engine[i]);
                cin >> M; while(getc(stdin)!='\n');
                for(i=0;i<M;i++) getline(cin, query[i]);
                if(M==0) { printf("Case #%d: 0\n", tt); continue; }

                int table[1000][100]={{0,},};

                for(i=0;i<N;i++) if(query[0]==engine[i]) { table[0][i]=INF; break; }
                for(i=1;i<M;i++) {
                        for(j=0;j<N;j++) {
                                if(query[i]==engine[j]) table[i][j]=INF;
                                else {
                                        m=INF;
                                        for(k=0;k<N;k++) {
                                                if(j==k) m=min(m, table[i-1][k]);
                                                else m=min(m,table[i-1][k]+1);
                                        }
                                        table[i][j]=m;
                                }
                        }
                }
/*
for(i=0;i<M;i++) {
        for(j=0;j<N;j++) {
                printf("%d ", table[i][j]);
        }
        puts("");
}
*/
                ret=INF;
                for(i=0;i<N;i++) ret=min(ret, table[M-1][i]);
                printf("Case #%d: %d\n", tt, ret);
        }

        return 0;
}

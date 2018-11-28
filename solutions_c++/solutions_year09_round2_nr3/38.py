// Author: Adam Polak
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <cmath>
#include <ctime>
#include <cstdlib>
using namespace std;
const int NIL = (-1);

#define REP(i,n) for(int i=0;i<(n);i++)
#define SIZE(c) ((int)((c).size()))

#define mp make_pair
#define st first
#define nd second
#define pb push_back

const int N = 21;
const int D = 3000;


int dx[]={-1,0,1,0};
int dy[]={0,-1,0,1};

int n;
char t[N][N];
bool id[N][N];
map<int,string> dp[N][N];

typedef pair<int,int> PI;
typedef pair<PI,int> PII;

queue<PII> Q;

bool cmp(const string &a, const string &b) {
    return a.length()<b.length()||(a.length()==b.length()&&a<b);
}

int ask[1000]; set<int> as;

void scase(int case_num) {
    
    while(!Q.empty()) Q.pop();
    printf("Case #%d:\n",case_num);
    int q;
    scanf("%d%d",&n,&q);
    REP(i,n) scanf("%s",t[i]);
    REP(i,q) scanf("%d",&ask[i]);
    as.clear(); REP(i,q) as.insert(ask[i]);
    REP(x,n) REP(y,n) dp[x][y].clear();
    REP(x,n) REP(y,n) id[x][y] = (t[x][y]!='-'&&t[x][y]!='+');
    REP(x,n) REP(y,n) if (id[x][y]) t[x][y]-='0';
    
    REP(x,n) REP(y,n) if(id[x][y]) {
        dp[x][y][t[x][y]]=string(1,char(t[x][y]+'0'));
        Q.push(PII(PI(x,y),t[x][y]));
    }
    while(!as.empty()) {
   //     if (Q.empty()) {printf("Q.empty to fast\n");}
        int x = Q.front().st.st;
        int y = Q.front().st.nd;
        int d = Q.front().nd;
        if (as.find(d)!=as.end()) as.erase(as.find(d));

   //     printf("%d %d %d %s\n",x,y,d,dp[x][y][d].c_str());
        Q.pop();
        REP(i,4) {
            int sx = x+dx[i]; int sy = y+dy[i];
            REP (j,4) {
                int nx = sx+dx[j];
                int ny = sy+dy[j];
                if (nx<0||ny<0||nx>=n||ny>=n) continue;
                if (sx<0||sy<0||sx>=n||sy>=n) continue;
           
                char sig = t[sx][sy];
                int nd;
                if (sig=='+') 
                    nd = d+t[nx][ny];
                else 
                    nd = d-t[nx][ny];
                string tmp = string(dp[x][y][d]).append(string(1,char(sig))).append(string(1,char(t[nx][ny]+'0')));
                if (dp[nx][ny].count(nd)==0) {
                    dp[nx][ny][nd]=tmp;
                    Q.push(PII(PI(nx,ny),nd));
                } else if (cmp(tmp,dp[nx][ny][nd])) dp[nx][ny][nd]=tmp;
            }
        }
    }
    REP(i,q) {
        string tmp="";
        REP(x,n)REP(y,n) if(dp[x][y].count(ask[i])) tmp=dp[x][y][ask[i]];
        REP(x,n)REP(y,n) if(dp[x][y].count(ask[i])) if(cmp(dp[x][y][ask[i]],tmp)) tmp=dp[x][y][ask[i]];
        printf("%s\n",tmp.c_str());
    }

}

int main() {
    int cases; 
    scanf("%d",&cases);
    //cin >> cases;
    REP(case_num,cases) scase(case_num+1);
    return 0;
}

    

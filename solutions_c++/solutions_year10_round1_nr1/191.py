#include <string>
#include <vector>
#include <list>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <iostream>
#include <sstream>
#include <numeric>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;

#define CLR(x) memset((x),0,sizeof(x))
#define SET(x,y) memset((x),(y),sizeof(x))
#define REP(i,x) for(int i=0;i<(x);i++)
#define FOR(i,x,y) for(int i=(x);i<(y);i++)
#define VI vector<int> 
#define PB(i,x) (i).push_back(x)
#define MP(x,y) make_pair((x),(y))


int T, K, N;
char B[51][51];
const int dr[]={0,-1,-1,-1}, dc[]={-1,0,-1,1};
int S[51][51][4][2];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d", &T);
    REP(cas,T){
        scanf("%d %d", &N, &K);
        REP(i,N){
            scanf("%s", B[i]);
            REP(j,N) if(B[i][j]!='.') B[i][j]=(B[i][j]=='R')?'0':'1';
        }

        REP(i,N){
            int p=N-1, q=N-1;
            while(q>=0){
                while(q>=0 && B[i][q]=='.') q--;
                if(q<0)break;
                B[i][p--]=B[i][q--];
            }
            while(p>=0) B[i][p--]='.';
        } 

        bool yes[2]={false,false};
        CLR(S);
        REP(i,N) REP(j,N) REP(q,2) REP(k,4){
            S[i][j][k][q]=(B[i][j]==q+'0');
            int nr=i+dr[k], nc=j+dc[k];
            if(S[i][j][k][q]>0 && nr>=0 && nr<N && nc>=0 && nc<N)
                S[i][j][k][q] += S[nr][nc][k][q];
            if(S[i][j][k][q]>=K) yes[q]=true;
        }
        printf("Case #%d: ",cas+1);
        if(yes[0]&&yes[1])puts("Both");
        else if(yes[0] && !yes[1])puts("Red");
        else if(!yes[0] && yes[1])puts("Blue");
        else puts("Neither");
    }
    return 0;
}

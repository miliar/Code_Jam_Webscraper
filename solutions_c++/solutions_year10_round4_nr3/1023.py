#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <iostream>
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

int C, R;
int xx[5000][5000];

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("c-small-0.out","w",stdout);
    scanf("%d", &C);
    FOR(cas,1,C+1){
        CLR(xx);
        scanf("%d", &R);
        int x1,y1,x2,y2;
        REP(i,R){
            scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
            FOR(r,x1,x2+1) FOR(c,y1,y2+1) xx[r][c]=1;
        }
        int u=0,d=100,l=0,r=100;
        int ans=0;
        bool ok=true;
        while(ok){
            ans++;
            ok=false;
            int tu=1111, td=-1, tl=1111, tr=-1;
            for(int i=d+1; i>=u; i--)
                for(int j=r+1; j>=l; j--){
                    if(xx[i][j]==1 &&(xx[i-1][j] || xx[i][j-1])
                        || xx[i][j]==0 && xx[i-1][j] && xx[i][j-1]){
                        xx[i][j]=1;
                        //printf("%d,%d,%d\n", ans,i,j);
                        ok=true;
                        tu=min(tu,i);
                        tl=min(tl,j);
                        tr=max(tr,j);
                        td=max(td,i);
                    } else{
                        xx[i][j]=0;
                    }
                }
            u=tu; d=td; l=tl; r=tr;
        }
        printf("Case #%d: %d\n", cas,ans);
    }
    return 0;
}


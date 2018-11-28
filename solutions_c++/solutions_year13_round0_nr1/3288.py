#include <set>
#include <map>
#include <cmath>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define lx(x) (x<<1)
#define rx(x) (x<<1|1)
#define debug puts("here")
#define rep(i,n) for(int i=0;i<n;i++)
#define rep1(i,n) for(int i=1;i<=n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define foreach(i,vec) for(unsigned i=0;i<vec.size();i++)
#define pb push_back
#define RD(n) scanf("%d",&n)
#define RD2(x,y) scanf("%d%d",&x,&y)
#define RD3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define RD4(x,y,z,w) scanf("%d%d%d%d",&x,&y,&z,&w)

/******** program ********************/

char s[5][5];

int ok(char op){
    rep(i,4){
        int ans = 0;
        rep(j,4)
            if(s[i][j]==op||s[i][j]=='T')
                ans ++;
        if(ans==4)
            return true;
    }
    rep(j,4){
        int ans = 0;
        rep(i,4)
            if(s[i][j]==op||s[i][j]=='T')
                ans ++;
        if(ans==4)
            return true;
    }

    bool ok = true;
    rep(i,4)if(!(s[i][i]=='T'||s[i][i]==op))
        ok = false;
    if(ok)
        return true;
    rep(i,4)if(!(s[i][3-i]=='T'||s[i][3-i]==op))
        return false;
    return true;
}

bool em(){
    rep(i,4)
        rep(j,4)
            if(s[i][j]=='.')
                return false;
    return true;
}

int main(){

	freopen("A-large.in","r",stdin);
	freopen("sum.out","w",stdout);

    int ncase = 0;
    RD(ncase);
    rep1(Ncase,ncase){
        rep(i,4)
            scanf("%s",s[i]);
        printf("Case #%d: ",Ncase);
        if(ok('X'))
            puts("X won");
        else if(ok('O'))
            puts("O won");
        else if(!em())
            puts("Game has not completed");
        else
            puts("Draw");
    }

	return 0;
}

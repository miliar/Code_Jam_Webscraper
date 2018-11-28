#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <utility>
#include <cstdlib>
#include <cassert>

#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define EPS 1e-9

using namespace std;

typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii;
typedef long long ll;

bool win(char ch, const vector<string> &brd)
{
    rep(i,4)
    {
        bool f=true;
        rep(j,4)
            if(brd[i][j]!=ch)f=false;
        if(f)return true;
    }
    rep(i,4)
    {
        bool f=true;
        rep(j,4)
            if(brd[j][i]!=ch)f=false;
        if(f)return true;
    }
    bool f=true;
    rep(i,4)
        if(brd[i][i]!=ch)f=false;
    if(f)return true;
    f=true;
    rep(i,4)
        if(brd[i][3-i]!=ch)f=false;
    if(f)return true;
    return false;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A_output.txt","w",stdout);
    int T;
    cin>>T;
    rep(TI,T)
    {
        vector<string> brd(4);
        rep(i,4)cin>>brd[i];
        int x,y;
        bool existT=false;
        rep(i,4)rep(j,4)if(brd[i][j]=='T')x=i,y=j,existT=true;
        if(existT)brd[x][y]='X';
        if(win('X',brd))
            printf("Case #%d: %c won\n",TI+1,'X');
        else {
            if(existT)brd[x][y]='O';
            if(win('O',brd))
                printf("Case #%d: %c won\n",TI+1,'O');
            else
            {
                bool f=false;
                rep(i,4)
                    rep(j,4)
                        if(brd[i][j]=='.')f=true;
                if(f)printf("Case #%d: Game has not completed\n",TI+1);
                else printf("Case #%d: Draw\n",TI+1);
            }
        } 
    }
    return 0;
}

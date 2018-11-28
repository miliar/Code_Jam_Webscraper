/*
  ------------------------- Hachiikung ---------------------------------
  ---------------------- Worrachate Bosri ------------------------------
  ------ Faculty of Computer Engineering Chulalongkorn University ------
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<string>
#include<utility>
using namespace std;
#define REP(i,FN) for(int i=0;i<FN;i++)
#define FOR(i,ST,FN) for(int i=ST;i<=FN;i++)
#define FORD(i,FN,ST) for(int i=FN;i>=ST;i--)
#define FORX(i,c) for(typeof(c.begin())i=c.begin();i!=c.end();i++)
#define pause system("pause")
#define S scanf
#define P printf
#define X first
#define Y second
#define pb push_back
#define PII pair<int,int>
#define sz size()

const int MOD(1000000007);
const int INF((1<<30)-1);
const int MAXN();

int solve(){

    string a[4];
    REP(i,4)
     cin >> a[i];

    bool dot=0;

    REP(i,4)
     REP(j,4)
      if(a[i][j]=='.')
       dot=1;

    REP(i,4)
    {
        int numX=0,numO=0;
        REP(j,4)
        {
            if(a[i][j]=='X') numX++;
            else if(a[i][j]=='O') numO++;
            else if(a[i][j]=='T') numX++,numO++;
        }
        if(numX==4) return 1;
        else if(numO==4) return 2;
    }

    REP(j,4)
    {
        int numX=0,numO=0;
        REP(i,4)
        {
            if(a[i][j]=='X') numX++;
            else if(a[i][j]=='O') numO++;
            else if(a[i][j]=='T') numX++,numO++;
        }
        if(numX==4) return 1;
        else if(numO==4) return 2;
    }

    int numX=0,numO=0;

    REP(i,4)
    {
        if(a[i][i]=='X') numX++;
        else if(a[i][i]=='O') numO++;
        else if(a[i][i]=='T') numX++,numO++;
    }

    if(numX==4) return 1;
    if(numO==4) return 2;

    numX=0,numO=0;

    REP(i,4)
    {
        if(a[i][3-i]=='X') numX++;
        else if(a[i][3-i]=='O') numO++;
        else if(a[i][3-i]=='T') numX++,numO++;
    }

    if(numX==4) return 1;
    if(numO==4) return 2;

    if(!dot) return 3;
    return 4;

}

int main(){

    freopen("1input.txt","r",stdin);
    freopen("1output.txt","w",stdout);

    int t;
    S("%d",&t);
    FOR(i,1,t)
    {
        int x=solve();
        P("Case #%d: ",i);
        if(x==1) P("X won\n");
        else if(x==2) P("O won\n");
        else if(x==3) P("Draw\n");
        else P("Game has not completed\n");
    }

}











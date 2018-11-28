#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <cstdio>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <cassert>
#include <sstream>

using namespace std;

typedef unsigned long long ULL;
typedef long long LL;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef stringstream SS;

#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define ABS(a) MAX(a,-(a))

#define SS(a) scanf("%d",&a)
#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define MOD 1000000007
#define INF (1<<31)

string str[4];

int score(char mine,char inp){
    if (inp == 'T') return 1;
    if (inp == mine) return 1;
    return 0;
}

bool check(char ch){
    REP(i,4){
        int cnt = 0;
        REP(j,4){
            cnt += score(ch, str[i][j]);
        }
        if (cnt==4) return 1;
    }

    REP(i,4){
        int cnt = 0;
        REP(j,4){
            cnt += score(ch, str[j][i]);
        }
        if (cnt==4) return 1;
    }
    int cnt = 0;
    REP(i,4){
        cnt += score(ch, str[i][i]);
    }
    if (cnt==4) return 1;

    cnt = 0;
    REP(i,4){
        cnt += score(ch, str[i][3-i]);
    }
    if (cnt==4) return 1;
    return 0;
}

bool checkdraw(){
    REP(i,4) REP(j,4) if (str[i][j]=='.') return 0;
    return 1;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int t;
    cin>>t;
    FOR(tt,1,t){
        REP(i,4){
            cin>>str[i];
        }
        printf("Case #%d: ",tt);
        if (check('X'))
          printf("X won\n");
        else if (check('O'))
          printf("O won\n");
        else if (checkdraw())
          printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}

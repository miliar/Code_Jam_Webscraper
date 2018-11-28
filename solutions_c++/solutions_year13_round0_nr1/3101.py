/*
 *Author:       Zhaofa Fang
 *Created time: 2013-04-13-10.50
 *Language:     C++
 */
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <string>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

typedef long long ll;
#define DEBUG(x) cout<< #x << ':' << x << endl
#define FOR(i,s,t) for(int i = (s);i <= (t);i++)
#define FORD(i,s,t) for(int i = (s);i >= (t);i--)
#define REP(i,n) FOR(i,0,n-1)
#define REPD(i,n) FORD(i,n-1,0)
#define PII pair<int,int>
#define PB push_back
#define MP make_pair
#define ft first
#define sd second
#define lowbit(x) (x&(-x))
#define INF (1<<30)


char str[6][6];

bool check(char ch){
    bool flag;
    REP(i,4){
        flag = 1;
        REP(j,4)if(!(str[i][j]=='T'||str[i][j]==ch)){
            flag = 0;
            break;
        }
        if(flag)return true;
    }
    REP(j,4){
        flag = 1;
        REP(i,4)if(!(str[i][j]=='T'||str[i][j]==ch)){
            flag = 0;
            break;
        }
        if(flag)return true;
    }

    int x=0,y=0;
    while(x<4){
        if(!(str[x][y]=='T'||str[x][y]==ch))break;
        x++;y++;
    }
    if(x>=4)return true;
    x=3,y=0;
    while(x>=0){
        if(!(str[x][y]=='T'||str[x][y]==ch))break;
        x--;y++;
    }
    if(x<0)return true;
    return false;
}
int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T;
	cin>>T;
	FOR(cas,1,T){
        bool hasEmpty = 0;
        REP(i,4){
            scanf("%s",str[i]);
            REP(j,4)if(str[i][j]=='.')hasEmpty = 1;
        }
        printf("Case #%d: ",cas);
        if(check('X'))puts("X won");
        else if(check('O'))puts("O won");
        else if(hasEmpty)puts("Game has not completed");
        else puts("Draw");
	}
	return 0;
}

#include <iostream>
#include <cstdio>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
#include <queue>
#include <deque>
#include <bitset>
#include <cmath>
#include <stack>
#include <algorithm>
#include <cctype>
#include <fstream>
#include <cassert>
#include <iomanip>
using namespace std;
#define pb push_back
#define FOR(i,ini,fin) for(int i=(int)ini;i<(int)fin;i++)
#define FOR_INC(i,ini,fin,inc) for(int i=(int)ini;i<(int)fin;i+=inc)
#define FOR_IT(iter,C) for(typeof(C.begin()) iter = C.begin();iter!=C.end();iter++)
#define all(A) A.begin(), A.end()
#define mem(x,val) memset(x,val,sizeof(x))
#define EPS 1e-7
#define MAY 100100
#define INF 100000000
#define MOD 1000000007
#define PI 3.141592654
typedef long long LL;
typedef double D;
#define G(x) (D)(x)
#define F(x) (LL)(x)

vector<string>s;
int win(char c){
    FOR(i,0,4){int xx=0;FOR(j,0,4)if(s[i][j]==c||s[i][j]=='T')xx++;if(xx==4)return 1;}
    FOR(i,0,4){int xx=0;FOR(j,0,4)if(s[j][i]==c||s[j][i]=='T')xx++;if(xx==4)return 1;}
    if((s[0][0]==c||s[0][0]=='T')&&(s[1][1]==c||s[1][1]=='T')&&(s[2][2]==c||s[2][2]=='T')&&(s[3][3]==c||s[3][3]=='T'))return 1;
    if((s[0][3]==c||s[0][3]=='T')&&(s[1][2]==c||s[1][2]=='T')&&(s[2][1]==c||s[2][1]=='T')&&(s[3][0]==c||s[3][0]=='T'))return 1;
    return 0;
}
int main(){
    int T;
    cin>>T;
    string ss;
    FOR(t,1,T+1){
        s.clear();
        FOR(i,0,4)cin>>ss, s.pb(ss);
        int x=0,o=0,dot=0;
        FOR(i,0,4)FOR(j,0,4)if(s[i][j]=='.')dot++;
        if(win('X'))printf("Case #%d: X won\n",t);
        else if(win('O'))printf("Case #%d: O won\n",t);
        else if(dot==0)printf("Case #%d: Draw\n",t);
        else printf("Case #%d: Game has not completed\n",t);

    }
    return 0;
}


#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<queue>
#include<map>
#include<vector>
#include<set>
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORr(i,a,b) for(int i=a;i>=b;i--)
#define tr(it,M) for(it=M.begin();it!=M.end();it++)
#define F first
#define S second
#define lim 250005
#define infi 10000
#define MOD 5000000
using namespace std;
typedef long long LL;
char game[4][4];
int sym[3]; // 0 for X, 1 for O and 2 for T
int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int test,t=0;scanf("%d",&test);
    while(test--){
        t++;
        FOR(i,0,4) cin>>game[i];
        bool fp=0;
        // Row Match
        FOR(i,0,4){
            memset(sym,0,sizeof(sym));
            FOR(j,0,4){
                if(game[i][j]=='X')sym[0]++;
                else if(game[i][j]=='O')sym[1]++;
                else if(game[i][j]=='T')sym[2]++;
            }
            if(sym[0]==4 || (sym[0]==3 && sym[2]==1)) { printf("Case #%d: X won\n",t); fp=1; break;}  // X won
            else if(sym[1]==4 || (sym[1]==3 && sym[2]==1)) { printf("Case #%d: O won\n",t); fp=1; break;}  // O won
        }
        if(fp)continue;
        // Column Match
        FOR(i,0,4){
            memset(sym,0,sizeof(sym));
            FOR(j,0,4){
                if(game[j][i]=='X')sym[0]++;
                else if(game[j][i]=='O')sym[1]++;
                else if(game[j][i]=='T')sym[2]++;
            }
            if(sym[0]==4 || (sym[0]==3 && sym[2]==1)) { printf("Case #%d: X won\n",t); fp=1; break;}  // X won
            else if(sym[1]==4 || (sym[1]==3 && sym[2]==1)) { printf("Case #%d: O won\n",t); fp=1; break;}  // O won
        }

        if(fp)continue;
        // Left Diagonal match
        memset(sym,0,sizeof(sym));
        FOR(i,0,4){
            if(game[i][i]=='X')sym[0]++;
            else if(game[i][i]=='O')sym[1]++;
            else if(game[i][i]=='T')sym[2]++;
        }
        if(sym[0]==4 || (sym[0]==3 && sym[2]==1)) { printf("Case #%d: X won\n",t); fp=1;}  // X won
        else if(sym[1]==4 || (sym[1]==3 && sym[2]==1)) { printf("Case #%d: O won\n",t); fp=1;}  // O won

        if(fp)continue;
        // Right Diagonal Match
        memset(sym,0,sizeof(sym));
        int k=0;
        FORr(i,3,0){
            if(game[k][i]=='X')sym[0]++;
            else if(game[k][i]=='O')sym[1]++;
            else if(game[k][i]=='T')sym[2]++;
            k++;
        }
        if(sym[0]==4 || (sym[0]==3 && sym[2]==1)) { printf("Case #%d: X won\n",t); fp=1;}  // X won
        else if(sym[1]==4 || (sym[1]==3 && sym[2]==1)) { printf("Case #%d: O won\n",t); fp=1;}  // O won

        if(fp)continue;

        int dots=0;
        FOR(i,0,4){
            FOR(j,0,4){
                if(game[i][j]=='.')dots++;
            }
        }

        if(dots>0) { printf("Case #%d: Game has not completed\n",t);}
        else {printf("Case #%d: Draw\n",t);}
    }
    return 0;
}

#include<stdio.h>
#include<map>
#include<queue>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back

char s[10][10];

int main(){
    int ca; scanf("%d",&ca);
    FOE(tt,1,ca){
        FOR(i,0,4) scanf("%s",s[i]);

        bool full=true;
        FOR(i,0,4){
            FOR(j,0,4){
                if (s[i][j]=='.') full=false;
            }
        }

        bool xw=false, ow=false;
        FOR(i,0,4){
            bool xx=true, oo=true;
            FOR(j,0,4){
                if (s[i][j]!='X' && s[i][j]!='T') xx=false;
                if (s[i][j]!='O' && s[i][j]!='T') oo=false;
            }
            if (xx) xw=true;
            if (oo) ow=true;
        }
        FOR(j,0,4){
            bool xx=true, oo=true;
            FOR(i,0,4){
                if (s[i][j]!='X' && s[i][j]!='T') xx=false;
                if (s[i][j]!='O' && s[i][j]!='T') oo=false;
            }
            if (xx) xw=true;
            if (oo) ow=true;
        }

        {
            bool xx=true, oo=true;
            FOR(i,0,4){
                if (s[i][i]!='X' && s[i][i]!='T') xx=false;
                if (s[i][i]!='O' && s[i][i]!='T') oo=false;
            }
            if (xx) xw=true;
            if (oo) ow=true;
        }

        {
            bool xx=true, oo=true;
            FOR(i,0,4){
                if (s[i][3-i]!='X' && s[i][3-i]!='T') xx=false;
                if (s[i][3-i]!='O' && s[i][3-i]!='T') oo=false;
            }
            if (xx) xw=true;
            if (oo) ow=true;
        }

        printf("Case #%d: ", tt);
        if (xw) printf("X won\n");
        else if (ow) printf("O won\n");
        else if (full) printf("Draw\n");
        else printf("Game has not completed\n");
    }
    return 0;
}

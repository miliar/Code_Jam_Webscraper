#include <iostream>
#include <cstring>
#include <cstdio>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;
string g[5];
int check()
{
    bool isfull=true;
    for (int i=0;i<4;i++) {
        bool isx1=true, iso1=true;
        bool isx2=true, iso2=true;
        for(int j=0;j<4;j++) {
            if (g[i][j]=='.') isfull=false;
            if (g[i][j]!='X' && g[i][j]!='T')
                isx1 = false;
            if (g[i][j]!='O' && g[i][j]!='T')
                iso1 = false;
            if (g[j][i]!='X' && g[j][i]!='T')
                isx2 = false;
            if (g[j][i]!='O' && g[j][i]!='T')
                iso2 = false;
        }
        if (isx1 || isx2) return 1;
        if (iso1 || iso2) return 2;
    }
    bool isx=true, iso=true;
    for(int i=0;i<4;i++) {
        if (g[i][i]!='X' && g[i][i]!='T')
            isx = false;
        if (g[i][i]!='O' && g[i][i]!='T')
            iso = false;
    }
    if (isx) return 1;
    if (iso) return 2;
    isx=true;
    iso=true;
    for(int i=0;i<4;i++) {
        if (g[i][3-i]!='X' && g[i][3-i]!='T')
            isx = false;
        if (g[i][3-i]!='O' && g[i][3-i]!='T')
            iso = false;
    }
    if (isx) return 1;
    if (iso) return 2;
    return isfull?3:4;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int Case;
    cin >> Case;
    for(int ca=1;ca<=Case;ca++) {
        printf("Case #%d: ", ca);
        for(int i=0;i<4;i++)
            cin>>g[i];
        int ret = check();
        if (ret==1) printf("X won\n");
        if (ret==2) printf("O won\n");
        if (ret==3) printf("Draw\n");
        if (ret==4) printf("Game has not completed\n");
    }
    return 0;
}

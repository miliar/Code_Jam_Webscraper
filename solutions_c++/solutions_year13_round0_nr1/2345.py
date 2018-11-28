#include <cstdio>
#include <cstdlib>
#include <cstring>
int t; char g[10][10];
int main()
{
    freopen("in1","r",stdin);
    freopen("out1","w",stdout);
    scanf("%d",&t);
    for(int I=1;I<=t;++I)
    {
        bool flag=0;
        for(int i=0;i<4;++i) scanf("%s",g[i]);
        for(int i=0;i<4;++i)
        {
            bool f=1;
            for(int j=0;j<4;++j) if(g[i][j]!='X'&&g[i][j]!='T') f=0;
            if(f) {flag=1; printf("Case #%d: X won\n",I); break;}
        }
        for(int i=0;i<4&&!flag;++i)
        {
            bool f=1;
            for(int j=0;j<4;++j) if(g[j][i]!='X'&&g[j][i]!='T') f=0;
            if(f) {flag=1; printf("Case #%d: X won\n",I); break;}
        }
        for(int i=0;i<4&&!flag;++i)
        {
            bool f=1;
            for(int j=0;j<4;++j) if(g[i][j]!='O'&&g[i][j]!='T') f=0;
            if(f) {flag=1; printf("Case #%d: O won\n",I); break;}
        }
        for(int i=0;i<4&&!flag;++i)
        {
            bool f=1;
            for(int j=0;j<4;++j) if(g[j][i]!='O'&&g[j][i]!='T') f=0;
            if(f) {flag=1; printf("Case #%d: O won\n",I); break;}
        }
        bool f=1;
        for(int i=0;i<4&&!flag;++i) if(g[i][i]!='X'&&g[i][i]!='T') f=0;
        if(f&&!flag) {flag=1; printf("Case #%d: X won\n",I);}
        f=1;
        for(int i=0;i<4&&!flag;++i) if(g[i][i]!='O'&&g[i][i]!='T') f=0;
        if(f&&!flag) {flag=1; printf("Case #%d: O won\n",I);}
        f=1;
        for(int i=0;i<4&&!flag;++i) if(g[i][3-i]!='X'&&g[i][3-i]!='T') f=0;
        if(f&&!flag) {flag=1; printf("Case #%d: X won\n",I);}
        f=1;
        for(int i=0;i<4&&!flag;++i) if(g[i][3-i]!='O'&&g[i][3-i]!='T') f=0;
        if(f&&!flag) {flag=1; printf("Case #%d: O won\n",I);}
        f=1;
        for(int i=0;i<4&&!flag;++i)
            for(int j=0;j<4&&!flag;++j) if(g[i][j]=='.') {f=0; break;}
        if(f&&!flag) printf("Case #%d: Draw\n",I);
        else if(!flag) printf("Case #%d: Game has not completed\n",I);
    }
    return 0;
}

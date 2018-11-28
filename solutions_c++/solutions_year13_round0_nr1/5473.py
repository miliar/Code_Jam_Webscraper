#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
long long t;
char c[5][5];
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%lld",&t);
    for(int o=1; o<=t; o++)
    {
        int f=0,l=0;
        for(int i=1; i<=4; i++)
        {
            scanf("\n");
            for(int j=1; j<=4; j++)
            {
                scanf("%c",&c[i][j]);
                //cout<<c[i][j];
                if(c[i][j]=='.') l=1;
            }
        }
        //system("pause");
        printf("Case #%d: ",o);
        for(int i=1; i<=4; i++)
        {
            int e=0;
            char p=c[i][1];
            if(p=='T') p=c[i][2];
            if(p=='.') continue;
            for(int j=2; j<=4; j++)
            {
                if(c[i][j]!=p&&c[i][j]!='T') {e=1; break;}
            }
            if(e==0&&p=='X') {printf("X won\n"); f=1; break;}
            else if(e==0&&p=='O') {printf("O won\n"); f=1; break;}
        }
        if(f==1) continue;
        for(int i=1; i<=4; i++)
        {
            int e=0;
            char p=c[1][i];
            if(p=='T') p=c[2][i];
            if(p=='.') continue;
            for(int j=2; j<=4; j++)
            {
                if(c[j][i]!=p&&c[i][j]!='T') {e=1; break;}
            }
            if(e==0&&p=='X') {printf("X won\n"); f=1; break;}
            if(e==0&&p=='O') {printf("O won\n"); f=1; break;}
        }
        if(f==1) continue;
        int e=0;
        char p=c[1][1];
        if(p=='T') p=c[2][2];
        if(p!='.') {
        for(int i=1; i<=4; i++)
        {
            if(c[i][i]!=p&&c[i][i]!='T') {e=1; break;}
        }
        if(e==0&&p=='X') {printf("X won\n"); continue;}
        else if(e==0&&p=='O') {printf("O won\n"); continue;}}
        e=0;
        p=c[1][4];
        if(p=='T') p=c[2][3];
        if(p!='.') {
        for(int i=1; i<=4; i++)
        {
            if(c[i][5-i]!=p&&c[i][5-i]!='T') {e=1; break;}
        }
        if(e==0&&p=='X') {printf("X won\n"); continue;}
        else if(e==0&&p=='O') {printf("O won\n"); continue;}}
        //cout<<f<<" "<<l<<endl;
        if(f==0&&l==1) printf("Game has not completed\n");
        else if(f==0&&l==0) printf("Draw\n");
        scanf("\n");
    }
    return 0;
}

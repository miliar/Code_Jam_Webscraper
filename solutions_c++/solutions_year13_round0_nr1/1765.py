#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
#define ss(n) scanf("%d",&n)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define REP(i,n) FOR(i,0,n-1)
int X_hor, O_hor, X_ver, O_ver;
char ar[10][10], k[10];
void check(int x, int y)
{
    FOR(i,1,4) {
        if(ar[x][i] == 'X') X_hor++;
        else if(ar[x][i] == 'O') O_hor++;
        else if(ar[x][i] == 'T') {X_hor++, O_hor++;}
    }
    FOR(i,1,4) {
        if(ar[i][y] == 'X') X_ver++;
        else if(ar[i][y] == 'O') O_ver++;
        else if(ar[i][y] == 'T') {X_ver++; O_ver++;}
    }
}
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int tc, not_draw, x_d1, o_d1, x_d2, o_d2, cnt = 0;
    ss(tc);
    cin.ignore(1);
    while(tc--)
    {   ++cnt;
        not_draw = 0;
        if(cnt != 1) gets(k);
        FOR(i,1,4)
        {
            gets(&ar[i][1]);
            FOR(j,1,4) {if(ar[i][j] == '.') not_draw = 1;}
        }
        //*****************************************************************8give gets
        //cout<<"printing input : \n\n";
        //FOR(i,1,4) {FOR(j,1,4) {printf("%c",ar[i][j]);} printf("\n");}
        //checking 1st diagonal
        x_d1 = 0, o_d1 = 0;
        FOR(i,1,4)
        {
            if(ar[i][i] == 'X') x_d1++;
            if(ar[i][i] == 'O') o_d1++;
            if(ar[i][i] == 'T') {x_d1++; o_d1++;}
        }
        if(x_d1 == 4) {printf("Case #%d: X won\n",cnt); continue;}
        if(o_d1 == 4) {printf("Case #%d: O won\n",cnt); continue;}
        //checking 2nd diagonal
        x_d2 = 0, o_d2 = 0;
        FOR(i,1,4)
        {
            if(ar[i][5-i] == 'X') x_d2++;
            if(ar[i][5-i] == 'O') o_d2++;
            if(ar[i][5-i] == 'T') {x_d2++; o_d2++;}
        }
        if(x_d2 == 4) {printf("Case #%d: X won\n",cnt); continue;}
        if(o_d2 == 4) {printf("Case #%d: O won\n",cnt); continue;}
        int found = 0;
        FOR(i,1,4)
        {
            FOR(j,1,4)
            {   X_hor=0, O_hor=0, X_ver=0, O_ver=0;
                check(i,j);
                if(X_hor==4 || X_ver==4) {printf("Case #%d: X won\n",cnt); found = 1; break;}
                if(O_hor==4 || O_ver==4) {printf("Case #%d: O won\n",cnt); found = 1; break;}
            }
            if(found == 1) break;
        }
        if(found==0 && not_draw==1) printf("Case #%d: Game has not completed\n",cnt) ;
        else if(found==0 && not_draw==0) printf("Case #%d: Draw\n",cnt);
    }
return 0;
}


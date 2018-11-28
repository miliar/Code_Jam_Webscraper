/*
TASK: Tic-Tac-Toe-Tomek
LANG: C++
*/
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
using namespace std;
#define X first
#define Y second
#define EPS 1e-9
#define ALL(x) (x).begin(),(x).end()
typedef pair<int,int> PII;
typedef long long LL;

int N,M,T;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int ii=0;
    char tb[10][10];
    while(T--)
    {
        for(i=0;i<4;i++)
            scanf("%s",tb[i]);
        vector<int> o_row(6),o_col(6);
        vector<int> x_row(6),x_col(6);
        bool con=false;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                if(tb[i][j]=='.')
                    con=true;
                if(tb[i][j]=='O' || tb[i][j]=='T')
                    o_row[i]++,o_col[j]++;
                if(tb[i][j]=='X' || tb[i][j]=='T')
                    x_row[i]++,x_col[j]++;
                if(i==j)
                {
                    if(tb[i][j]=='O' || tb[i][j]=='T')
                        o_col[5]++;
                    if(tb[i][j]=='X' || tb[i][j]=='T')
                        x_col[5]++;
                }
                if(i+j==3)
                {
                    if(tb[i][j]=='O' || tb[i][j]=='T')
                        o_col[4]++;
                    if(tb[i][j]=='X' || tb[i][j]=='T')
                        x_col[4]++;
                }
            }
        int num=0;
        for(i=0;i<6;i++)
        {
            if(o_col[i]==4) num=1;
            if(x_col[i]==4) num=2;
            if(o_row[i]==4) num=1;
            if(x_row[i]==4) num=2;
        }
        printf("Case #%d: ",++ii);
        if(num==1)      printf("O won\n");
        else if(num==2) printf("X won\n");
        else if(con)
            printf("Game has not completed\n");
        else
            printf("Draw\n");
    }
}

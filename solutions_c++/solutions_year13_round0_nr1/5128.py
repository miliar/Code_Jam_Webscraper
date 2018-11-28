//HighFlow
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <fstream>
#include <string.h>
#include <math.h>
#include <algorithm>
#define fcat(c) while (c!='\n') fscanf(f,"%c",&c)
#define cat(c) while (c!='\n') scanf("%c",&c)
#define For(i,st,dr,k) for (int i=(st);i<=(dr);i+=(k))
#define ll (long long)
#define kfl(i,j) (a[(i)][(j)].c-a[(i)][(j)].f)
using namespace std;
FILE *f,*g;
char a[6][6];
char ax[10];
int i,j,q,t,cn;

inline int kk(char c)
{
    if (c=='T') return 0;
    if (c=='X') return 1;
    if (c=='O') return -1;
}

void afis(int x)
{
    if (x>=3) fprintf(g,"Case #%d: X won\n",q);
    else
        fprintf(g,"Case #%d: O won\n",q);

}


void solve()
{
    int i,j;

    for (i=1,cn=0;i<=4;i++)
     if (a[i][i]=='.')
        {
           cn=0;
           break;
        }
        else
        cn=cn+kk(a[i][i]);

    if (cn>=3 || cn<=-3)
        {
            afis(cn);
            return;
        }

    for (i=1,cn=0;i<=4;i++)
        if (a[i][4-i+1]=='.')
        {
           cn=0;
           break;
        }
        else
        cn=cn+kk(a[i][4-i+1]);

    if (cn>=3 || cn<=-3)
        {
            afis(cn);
            return;
        }

    for (i=1;i<=4;i++)
    {
        for (j=1,cn=0;j<=4;j++)
             if (a[i][j]=='.')
            {
                cn=0;
                break;
            }
            else
                cn=cn+kk(a[i][j]);
        if (cn>=3 || cn<=-3)
        {
            afis(cn);
            return;
        }
    }
    for (j=1;j<=4;j++)
    {
        for (i=1,cn=0;i<=4;i++)
             if (a[i][j]=='.')
            {
                cn=0;
                break;
            }
            else
                cn=cn+kk(a[i][j]);
            if (cn>=3 || cn<=-3)
            {
                afis(cn);
                return;
            }
    }

    bool ok=true;
    for (i=1;i<=4;i++)
        for (j=1;j<=4;j++)
            if (a[i][j]=='.') ok=false;

    if (ok==true)
        fprintf(g,"Case #%d: Draw\n",q);
    else
        fprintf(g,"Case #%d: Game has not completed\n",q);

}

int main()
{
    f=fopen("test.in","r");
    g=fopen("tic-tac.out","w");
    fscanf(f,"%d",&t);

    for (q=1;q<=t;q++)
    {
        for (i=1;i<=4;i++)
            fscanf(f,"%s",a[i]+1);
        solve();
    }

	return 0;
}

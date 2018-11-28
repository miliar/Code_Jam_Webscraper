#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
char cmap[100][100];
int r,c;
bool change(int i,int j)
{
    if(i+1<r && j+1<c)
    {
        if(cmap[i][j]=='#' && cmap[i+1][j]=='#' && cmap[i][j+1]=='#' && cmap[i+1][j+1]=='#')
        {
            cmap[i][j]='/';
            cmap[i][j+1]='\\';
            cmap[i+1][j]='\\';
            cmap[i+1][j+1]='/';
            return true;
        }
    }
    return false;
}
bool judge()
{
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            if(cmap[i][j]=='#')
            {
                if(!change(i,j))
                    return false;
            }
        }
    }
    return true;
}
int main()
{
    FILE *in=fopen("A-large.in","r");
    FILE *out=fopen("A-large.out","w");

    int t;
    int cntt=0;
    fscanf(in,"%d",&t);
    bool flag;
    while(t--)
    {
        cntt++;
        fprintf(out,"Case #%d:\n",cntt);
        fscanf(in,"%d%d",&r,&c);
        for(int i=0;i<r;i++)
        {
            fscanf(in,"%s",cmap[i]);
        }
        flag=judge();
        if(flag)
        {
            for(int i=0;i<r;i++)
                fprintf(out,"%s\n",cmap[i]);
        }
        else
        {
            fprintf(out,"Impossible\n");
        }
    }
    return 0;
}


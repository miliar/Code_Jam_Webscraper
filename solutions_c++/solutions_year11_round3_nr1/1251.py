#include<iostream>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<string>
#include<vector>
#include<sstream>
#include<cstdio>
#include<map>
using namespace std;
char mat[200][200];
int r,c;
int valid(int itemx,int itemy)
{
    if(itemx>=r || itemy>=c) return 0;
    if(itemx<0 || itemy<0) return 0;
    return 1;

}
int main()
{   freopen("A.txt","r",stdin);
    freopen("A1.txt","w",stdout);

    int i,j,m,n,kase,k;
    scanf("%d",&kase);
    k=1;
    while(kase--)
    {
        scanf("%d%d",&r,&c);

        for(i=0;i<r;i++)
            for(j=0;j<c;j++)
                scanf(" %c",&mat[i][j]);

        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(valid(i,j))
                {
                        if(mat[i][j]=='#' && mat[i+1][j]=='#' && mat[i+1][j+1]=='#' && mat[i][j+1]=='#')
                        {
                            mat[i][j]='/';
                            mat[i+1][j]='\\';
                            mat[i+1][j+1]='/';
                            mat[i][j+1]='\\';
                        }
                }
            }

        }


        int cq1=1;

        for(i=0;i<r;i++)
            for(j=0;j<c;j++)
            {
                if(mat[i][j]=='#'){cq1=0;goto out;}
            }
        out:;
        printf("Case #%d:\n",k++);


        if(cq1==0){printf("Impossible\n");}
        else
        {
            for(i=0;i<r;i++)
            {
                for(j=0;j<c;j++)
                {
                    printf("%c",mat[i][j]);
                }
                printf("\n");
            }
        }
        memset(mat,0,sizeof(mat));
    }
    return 0;
}

#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<cstdio>
#include<cctype>
#include<cstdlib>
#include<cmath>

using namespace std;

int level, mb[103][103], h, w;

int minim(int mat[103][103], int i, int j)
{
    if(mb[i][j]!=0) return mb[i][j];
    if(mat[i][j]<=mat[i-1][j] && mat[i][j]<=mat[i+1][j] && mat[i][j]<=mat[i][j-1] && mat[i][j]<=mat[i][j+1])
        return mb[i][j]=++level;
    if(mat[i+1][j]<mat[i-1][j] && mat[i+1][j]<mat[i][j-1] && mat[i+1][j]<mat[i][j+1] && mat[i+1][j]<mat[i][j])
        return mb[i][j]=minim(mat, i+1, j);
    if(mat[i][j+1]<mat[i-1][j] && mat[i][j+1]<mat[i][j-1] && mat[i][j+1]<=mat[i+1][j] && mat[i][j+1]<mat[i][j])
        return mb[i][j]=minim(mat, i, j+1);
    if(mat[i][j-1]<mat[i-1][j] && mat[i][j-1]<=mat[i][j+1] && mat[i][j-1]<=mat[i+1][j] && mat[i][j-1]<mat[i][j])
        return mb[i][j]=minim(mat, i, j-1);
    if(mat[i-1][j]<=mat[i][j-1] && mat[i-1][j]<=mat[i][j+1] && mat[i-1][j]<=mat[i+1][j] && mat[i-1][j]<mat[i][j])
        return mb[i][j]=minim(mat, i-1, j);
}

int main(void)
{
    int t, mat[103][103], almax=10002, i, j, k, cont=0;
    scanf("%d", &t);
    while(cont<t)
    {
        level=0;
        scanf("%d%d", &h, &w);
        for(i=0; i<h; i++)
            for(j=0; j<w; j++)
            {
                scanf("%d", &mat[i+1][j+1]);
                mb[i+1][j+1]=0;
            }
        for(i=0; i<=h+1; i++)
            mat[i][0]=mat[i][w+1]=almax;
        for(i=0; i<=w+1; i++)
            mat[0][i]=mat[h+1][i]=almax;
        for(i=1; i<=h; i++)
            for(j=1; j<=w; j++)
            {
                if(mb[i][j]==0)
                    mb[i][j]= minim(mat, i, j);
            }
        printf("Case #%d:\n", cont+1);
        for(i=1; i<=h; i++)
        {
            for(j=1; j<w; j++)
                printf("%c ", mb[i][j]+'a'-1);
            printf("%c\n", mb[i][w]+'a'-1);
        }
        cont++;
    }
    return 0;
}

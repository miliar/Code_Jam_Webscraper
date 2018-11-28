#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<cstdlib>
#include<cmath>
#include<stack>
#include<string>
#include<cstdio>
using namespace std;
char mat[100][100],ch;

int dig(int n,int k,int r,int c)
{
    int i,j;
    if(mat[r][c]=='.')
        return 0;
    if(mat[r][c]=='R')
    {
        int cnt=0;
        for(i=r,j=c;i<n && j<n;i++,j++)
        {
            if(mat[i][j]=='R')
                cnt++;
            else
                break;
        }
        if(cnt==k)
            return 'R';
        cnt=0;
        for(i=r,j=c;i <n && j>=0;i++,j--)
        {
            if(mat[i][j]=='R')
                cnt++;
            else
                break;
        }
        if(cnt==k)
            return 'R';
    }
    else if(mat[r][c]=='B')
    {
        int cnt=0;
        for(i=r,j=c;i<n && j<n;i++,j++)
        {
            if(mat[i][j]=='B')
                cnt++;
            else
                break;
        }
        if(cnt==k)
            return 'B';
        cnt=0;
        for(i=r,j=c;i<n && j>=0;i++,j--)
        {
            if(mat[i][j]=='B')
                cnt++;
            else
                break;
        }
        if(cnt==k)
            return 'B';
    }
    return 0;
}
int row(int n,int k,int r,int c)
{
    int i,j;
    if(mat[r][c]=='.')
        return 0;
    if(mat[r][c]=='R')
    {
        int cnt=0;
        for(i=r;i<n;i++)
            if(mat[i][c]=='R')
                cnt++;
            else
                break;
        if(cnt==k)
            return 'R';
    }
    else if(mat[r][c]=='B')
    {
        int cnt=0;
        for(i=r;i<n;i++)
            if(mat[i][c]=='B')
                cnt++;
            else
                break;
        if(cnt==k)
            return 'B';
    }
    return 0;
}
int col(int n,int k,int r,int c)
{
    int i,j;
    if(mat[r][c]=='.')
        return 0;
    if(mat[r][c]=='R')
    {
        int cnt=0;
        for(i=c;i<n;i++)
            if(mat[r][i]=='R')
                cnt++;
            else
                break;
        if(cnt==k)
            return 'R';
    }
    else if(mat[r][c]=='B')
    {
        int cnt=0;
        for(i=c;i<n;i++)
            if(mat[r][i]=='B')
                cnt++;
            else
                break;
        if(cnt==k)
            return 'B';
    }
    return 0;
}
int main()
{
    int test,i,j,n,k,kase=0;

    freopen("A.in","r",stdin);
    freopen("Aout.txt","w",stdout);

    scanf("%d",&test);
    while(test--)
    {
        scanf("%d %d%c",&n,&k,&ch);
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                scanf("%c",&ch);
                mat[j][n-1-i]=ch;
            }
            scanf("%c",&ch);
        }
        int sp=1;
        while(sp)
        {
            sp=0;
            for(i=n-1;i>0;i--)
            {
                for(j=n-1;j>=0;j--)
                {
                    if(mat[i][j]=='.' && mat[i-1][j]!='.')
                    {
                        swap(mat[i][j],mat[i-1][j]);
                        sp++;
                    }
                }
            }
        }
 /*       for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                printf("%c",mat[i][j]);
            }
            printf("\n");
        }
*/
        int blk=0,red=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(dig(n,k,i,j)=='R')
                    red++;
                if(row(n,k,i,j)=='R')
                    red++;
                if(col(n,k,i,j)=='R')
                    red++;
                if(dig(n,k,i,j)=='B')
                    blk++;
                if(row(n,k,i,j)=='B')
                    blk++;
                if(col(n,k,i,j)=='B')
                    blk++;
            }
        }
        if(blk>0 && red >0)
            printf("Case #%d: Both\n",++kase);
        else if(blk>0 && red == 0)
            printf("Case #%d: Blue\n",++kase);
        else if(blk == 0 && red > 0)
            printf("Case #%d: Red\n",++kase);
        else
            printf("Case #%d: Neither\n",++kase);
    }
    return 0;
}

/*
 * File:   newcodejam.cc
 * Author: tanaeem
 *
 * Created on August 9, 2008, 10:05 PM
 */

#include <stdio.h>
#include <stdlib.h>
#include<string.h>
#define MOD 10007
int h, r;;
bool ill[110][110];
int cache[110][110];
void init()
{
    for (int i = 0; i < 105; i++)
    {
        for (int j = 0; j < 105; j++)
        {
            cache[i][j]=-1;
            ill[i][j]=false;
        }
        
    }
    
}
int cnt(int r, int h)
{
    if(r==1 && h==1)
        return 1;
    if(r<1 || h<1)
        return 0;
    if(ill[r][h])
        return 0;
    if(cache[r][h]!=-1)
        return cache[r][h];
    cache[r][h]=cnt(r-2, h-1);
    cache[r][h]+=cnt(r-1, h-2);
    cache[r][h]%=MOD;
    return cache[r][h];
}
int main()
{
      freopen ("D.in","r",stdin);
      freopen ("small.op","w",stdout);
    
    //  freopen ("C2.in","r",stdin);
    //  freopen ("large.op","w",stdout);
    int t, c = 0;
    scanf("%d", &t);
    while (t--)
    {
        int R;
        init();
        scanf("%d%d%d", &h, &r, &R);
        for (int i = 0; i < R; i++)
        {
            int a, b;
            scanf("%d%d", &a, &b);
            ill[a][b]=true;
        }
        
        int ans=cnt(h, r);
        
        printf("Case #%d: %d\n", ++c, ans);
    }
    return 0;
}


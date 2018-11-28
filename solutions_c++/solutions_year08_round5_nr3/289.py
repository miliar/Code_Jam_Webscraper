/*
 * File:   newcodejam.cc
 * Author: tanaeem
 *
 * Created on August 9, 2008, 10:45 PM
 */

#include <stdio.h>
#include <stdlib.h>
#include<string.h>
char grid[20][20];
int m, n;
int cache[11][1050];
int gr[20];
int cnt[1030];
void init()
{
    for (int i = 0; i < 11; i++)
    {
        gr[i]=0;
        for (int j = 0; j < 1030; j++)
        {
            cache[i][j]=-1;
        }
        
        
    }
    
    
}
bool isvalid(int r, int pr, int cur)
{
    int v=cur & (cur>>1);
    if(v!=0)
        return false;
    v=cur & ((cur<<1)&((1<<n)-1));
    if(v!=0)
        return false;
    v=cur & ((pr>>1));
    if(v!=0)
        return false;
    
    v=cur & ((pr<<1)&((1<<n)-1));
    if(v!=0)
        return false;
    v=cur&gr[r];
    if(v!=cur)
        return false;
    return true;
    
}

int maxim(int r, int pr)
{
    if(r==m)
        return 0;
    if(cache[r][pr]!=-1)
        return cache[r][pr];
    cache[r][pr]=0;
    for (int i = 0; i < 1<<n; i++)
    {
        if(isvalid(r, pr, i))
            if(cache[r][pr]<(maxim(r+1, i)+cnt[i]))
                cache[r][pr]=maxim(r+1, i)+cnt[i];
    }
    return cache[r][pr];
}

int main()
{
      freopen ("C.in","r",stdin);
      freopen ("small.op","w",stdout);
    
    //  freopen ("C2.in","r",stdin);
    //  freopen ("large.op","w",stdout);
    int t, c = 0;
    scanf("%d", &t);
    for (int i = 0; i < 1025; i++)
    {
        cnt[i]=cnt[i/2]+(i%2);        
    }

    while (t--)
    {
        scanf("%d%d", &m, &n);
        init();
        for (int i = 0; i < m; i++)
        {
            scanf("%s", grid[i]);
            for (int j = 0; j < n; j++)
            {
                gr[i]<<=1;
                gr[i]|=(grid[i][j]=='.');
            }
            
        }
        
        int op=maxim(0,0);
        printf("Case #%d: %d\n", ++c, op);
    }
    return 0;
}


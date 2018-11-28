#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;
char s[53][53],ch[53][53];
int dx[8]={-1,-1,0,1,1,1,0,-1},dy[8]={0,1,1,1,0,-1,-1,-1};
int n,k;
bool limit(int x,int y,int k)
{
     if (x+dx[k]>=0&&x+dx[k]<n&&y+dy[k]>=0&&y+dy[k]<n)
     return true;
     return false;
}
int main()
{
    int i,j,t,q,cas,tcas=0;
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&cas);
    while (cas--)
    {scanf("%d%d",&n,&k);for (i=0;i<n;i++)
    scanf("%s",s[i]);
    memcpy(ch,s,sizeof(s));
    for (i=0;i<n;i++)
    for (j=0;j<n;j++)
    ch[j][n-i-1]=s[i][j];
    for (i=n-2;i>=0;i--)
    for (j=0;j<n;j++)
    if (ch[i][j]!='.'&&ch[i+1][j]=='.')
    {
        t=i;
        while (ch[t][j]!='.'&&ch[t+1][j]=='.'&&t<n-1)
        {swap(ch[t][j],ch[t+1][j]);t++;}
    }
    bool flag1=false;
    bool flag2=false;
    for (i=0;i<n;i++)
    for (j=0;j<n;j++)
    { if (flag1) break;
        if (ch[i][j]=='R'){ 
        for (q=0;q<4;q++)
        //if (!limit(i,j,4+q)||ch[i+dx[4+q]][j+dy[4+q]]!='R')
        {
           
            int x=i;int y=j;
            for (t=1;t<k&&limit(x,y,q);t++)
            {
                x+=dx[q];y+=dy[q];
                if (ch[x][y]!='R')
                break;
            }
            if (t==k)
            flag1=true;
     }   }
}
    for (i=0;i<n;i++)
    for (j=0;j<n;j++)
    { if (flag2) break;
        if (ch[i][j]=='B')
       for (q=0;q<4;q++)
      // if (!limit(i,j,4+q)||ch[i+dx[4+q]][j+dy[4+q]]!='B')
        { 
            int x=i;int y=j;
            for (t=1;t<k&&limit(x,y,q);t++)
            {
                x+=dx[q];y+=dy[q];
                if (ch[x][y]!='B')
                break;
            }
            if (t==k)
            flag2=true;
        }
    }
    if (flag1&&flag2)
    printf("Case #%d: Both\n",++tcas);
    else if (flag1)
    printf("Case #%d: Red\n",++tcas);
    else if (flag2)
    printf("Case #%d: Blue\n",++tcas);
    else
    printf("Case #%d: Neither\n",++tcas);
}
}

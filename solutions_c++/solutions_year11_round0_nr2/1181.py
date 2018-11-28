#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int c,d,n;
int t[513];
void init()
{
    for(int i='A';i<='Z';i++)
    t[i]=i-'A';
    scanf("%d",&c);
    char s[4];
    int pro[30][30];
    memset(pro,-1,sizeof(pro));
    for(int i=0;i<c;i++)
    {
        scanf("%s",s);
        pro[t[s[0]]][t[s[1]]]=t[s[2]];
        pro[t[s[1]]][t[s[0]]]=t[s[2]];
    }
    scanf("%d",&d);
    int turn[30][30];
    memset(turn,-1,sizeof(turn));
    for(int i=0;i<d;i++)
    {
        scanf("%s",s);
        turn[t[s[0]]][t[s[1]]]=1;
        turn[t[s[1]]][t[s[0]]]=1;
    }
    char che[109],ch;
    scanf("%d",&n);
    scanf("%s",che);
    int ans[102];
    int vis[30];
    int top=-1;
    memset(vis,-1,sizeof(vis));
    for(int i=0;i<n;i++)
    {
        ch=che[i];
       // cout<<ch<<" tt"<<endl;
        if(top==-1){ans[++top]=t[ch];continue;}
        if(pro[ans[top]][t[ch]]!=-1)
        ans[top]=pro[ans[top]][t[ch]];
        else
        {
            for(int i=0;i<=top;i++)
            if(turn[ans[i]][t[ch]]==1)
            top=-1;
            if(top!=-1)ans[++top]=t[ch];
        }
    }
    printf("[");
    for(int i=0;i<top;i++)
    {
        printf("%c, ",char(ans[i]+'A'));
    }
    if(top>-1)
    printf("%c",char(ans[top]+'A'));
    printf("]\n");
}
int main()
{
    int Case;
   // freopen("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\A-small.in","r",stdin);
    freopen("E:\\c.out", "w", stdout);
    scanf("%d",&Case);
    for(int i=1;i<=Case;i++)
    {
        printf("Case #%d: ",i);
        init();
    }
return 0;
}

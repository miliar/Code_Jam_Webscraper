#include <iostream>

using namespace std;

int nt;
int h,w;
int tab[128][128];
int ch[16384];
int let[32];
int pt[16384];

int dfs(int x,int y)
{
    if(ch[(x-1)*w+y]!=0) return ch[(x-1)*w+y];
    int min=10001;
    if(x>1) if(tab[x-1][y]<min) min=tab[x-1][y];
    if(y>1) if(tab[x][y-1]<min) min=tab[x][y-1];
    if(y<w) if(tab[x][y+1]<min) min=tab[x][y+1];
    if(x<h) if(tab[x+1][y]<min) min=tab[x+1][y];
    if(min>=tab[x][y]) {ch[(x-1)*w+y]=(x-1)*w+y; return ch[(x-1)*w+y];}
    if(min==10001) {ch[(x-1)*w+y]=(x-1)*w+y; return ch[(x-1)*w+y];}
    if(x>1&&tab[x-1][y]==min)
    {
       ch[(x-1)*w+y]=dfs(x-1,y);
       return ch[(x-1)*w+y];
    }
    if(y>1&&tab[x][y-1]==min)
    {
        ch[(x-1)*w+y]=dfs(x,y-1);
        return ch[(x-1)*w+y];
    }
    if(y<w&&tab[x][y+1]==min)
    {
       ch[(x-1)*w+y]=dfs(x,y+1);
       return ch[(x-1)*w+y];
    }
    if(x<h&&tab[x+1][y]==min)
    {
       ch[(x-1)*w+y]=dfs(x+1,y);
       return ch[(x-1)*w+y];
    }
    return 0;
}

void solve()
{
    for(int i=1;i<=h;i++)
        for(int j=1;j<=w;j++)
            if(ch[(i-1)*w+j]==0) dfs(i,j);

    int l=1;
    for(int i=1;i<=h;i++)
    {
        for(int j=1;j<=w;j++)
        {
            if(pt[ch[(i-1)*w+j]]==0)
            {
                let[l]=ch[(i-1)*w+j];
                pt[ch[(i-1)*w+j]]=l;
                l++;
            }
        }
    }
}

void read()
{
    scanf("%d",&nt);
    for(int i=1;i<=nt;i++)
    {
        memset(ch,0,sizeof(ch));
        memset(tab,0,sizeof(tab));
        memset(let,0,sizeof(let));
        memset(pt,0,sizeof(pt));
        scanf("%d %d",&h,&w);
        for(int j=1;j<=h;j++)
        {
            for(int k=1;k<=w;k++) scanf("%d",&tab[j][k]);
        }
        solve();
        printf("Case #%d:\n",i);
        for(int j=1;j<=h;j++)
        {
            printf("%c", pt[ch[(j-1)*w+1]]+'a'-1);
            for(int k=2;k<=w;k++)
            {
                printf(" %c", pt[ch[(j-1)*w+k]]+'a'-1);
            }
            printf("\n");
        }
    }
}

int main()
{
    read();
    return 0;
}

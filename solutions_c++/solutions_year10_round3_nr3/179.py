#include<stdio.h>
#include<iostream>
#include<queue>
#include<map>
#include<vector>
#include<string>
#include<sstream>
#include<math.h>
#include<algorithm>
#define _clr(x) memset(x,-1,sizeof(x))
#define clr(x) memset(x,0,sizeof(x))
#define pb push_back
#define M 1001
#define ll long long
using namespace std;
int g[1010][1010];
int v[1010][1010];
int d[4][2]={0,1,0,-1,1,0,-1,0};
int ft[1010];
int check(int a,int b,int l)
{
    for(int i=0;i<l;i++)
    {
        for(int j=0;j<l;j++)
        {
            if(v[i][j])return 0;
            int x=a+i,y=b+j;
            for(int k=0;k<4;k++)
            {
                int rx=x+d[k][0],ry=y+d[k][1];
                if(rx<a+l&&rx>=a&&ry<b+l&&ry>=b)
                {
                    if(g[rx][ry]==g[x][y])return 0;
                }
            }
        }
    }
    return 1;
}
void mark(int a,int b,int l)
{
    for(int i=0;i<l;i++)
    {
        for(int j=0;j<l;j++)
        {
            v[i+a][j+b]=1;
        }
    }
}
int check(char ch)
{
    if(ch>='A'&&ch<='Z')return ch-'A'+10;
    else return ch-'0';
}
int main()
{
    freopen("in.txt","r",stdin);
    //freopen("in.in","r",stdin);
    //freopen("in.out","w",stdout);
    int T;
    scanf("%d",&T);
    int ca=0;
    while(T--)
    {
        clr(v);
        clr(ft);
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
        {
            int pos=-1;
            for(int j=0;j<m;j++)
            {
                char ch;
                cin>>ch;
                int k=check(ch);
                pos+=4;
                while(k)
                {
                    g[i][pos]=k&1;
                    k>>=1;
                    pos--;
                }
                pos+=4;
            }
        }
        m*=4;
        int ans=0,nn=0;
        while(1)
        {
            int maxlen=0;
            int a,b;
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<m;j++)
                {
                    int len=0;
                    for(int k=2;k<min(n,m);k++)
                    {
                        if(!check(i,j,k))
                        {
                            len=k-1;
                            break;
                        }
                    }
                    if(maxlen<len)
                    {
                        maxlen=len;
                        a=i;b=j;
                    }
                }
            }
            if(maxlen<2)break;
            mark(a,b,maxlen);
            ft[maxlen]++;
            if(ft[maxlen]==1)ans++;
            nn=max(nn,maxlen);
        }
        printf("%d\n",ans);
        for(int i=nn;i>1;i--)
        {
            if(ft[i])
            {
                printf("%d %d\n",i,ft[i]);
            }
        }
    }
}

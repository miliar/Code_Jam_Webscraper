#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;

const int N=30;
int a[N][N];
bool op[N][N];
int v[N];
int n,c,d;
char s[200];
int b[200];

void init()
{
    memset(a,-1,sizeof(a));
    memset(op,false,sizeof(op));
    memset(v,0,sizeof(v));
}

void read()
{
    int i,x,y,z;
        scanf("%d",&c);
        for(i=0;i<c;i++)
        {
            scanf("%s",s);
            x=s[0]-'A';
            y=s[1]-'A';
            z=s[2]-'A';
            a[x][y]=a[y][x]=z;
        }
        scanf("%d",&d);
        for(i=0;i<d;i++)
        {
            scanf("%s",s);
            x=s[0]-'A';
            y=s[1]-'A';
            op[x][y]=op[y][x]=true;
        }
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t,i,j;
    int x,y,z;
    int cs=0;
    scanf("%d",&t);
    while(t--)
    {
        init();
        read();
        scanf("%d",&n);
        scanf("%s",s);
        int len=0;
        b[len++]=s[0]-'A';
        v[b[0]]=1;
        for(i=1;i<n;i++)
        {
            x=s[i]-'A';
            if(len==0)
            {
                b[len++]=x;
                v[x]++;
                continue;
            }
            y=a[x][b[len-1]];
            if(y!=-1)
            {
                v[b[len-1]]--;
                b[len-1]=y;
                v[y]++;
            }
            else
            {
                for(j=0;j<26;j++) if(v[j]&&op[x][j]) break;
                if(j<26)
                {
                    memset(v,0,sizeof(v));
                    len=0;
                }
                else
                {
                    v[x]++;
                    b[len++]=x;
                }
            }
        }
        printf("Case #%d: [",++cs);
        for(i=0;i<len;i++)
        {
            printf("%c",b[i]+'A');
            if(i!=len-1) printf(", ");
        }
        printf("]\n");
    }
    return 0;
}









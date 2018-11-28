#include <cstdio>
#include <iostream>
#define MAXN 50
using namespace std;

const int dx[4]={0,1,1,1};
const int dy[4]={1,0,-1,1};
char a[MAXN+1][MAXN+1],b[MAXN+1][MAXN+1];
int n,k;

void rotate(int x,int y)
{
    int i;
    for(i=x-1;i>=0;i--)
    {
        b[i+1][y]=b[i][y];
    }
    b[0][y]='.';
}

int check(int x,int y,char ch)
{
    int i,j,d,cnt;
    for(d=0;d<4;d++)
    {
        cnt=0;
        i=x;
        j=y;
        while((i>=0)&&(i<n)&&(j>=0)&&(j<n)&&(b[i][j]==ch))
        {
            i=i+dx[d];
            j=j+dy[d];
            cnt++;
        }
        if(cnt>=k)
        {
            return 1;
        }
    }
    return 0;
}

int kpiece(char ch)
{
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {
            if((b[i][j]==ch)&&(check(i,j,ch)==1))
            {
                return 1;
            }
        }
    }
    return 0;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int c,i,j,p,t,fr,fb;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        scanf("%d %d",&n,&k);
        for(i=0;i<n;i++)
        {
            scanf("%s",a[i]);
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                b[j][n-1-i]=a[i][j];
            }
        }
        for(j=0;j<n;j++)
        {
            for(p=0;p<n;p++)
            {
                for(i=n-1;i>=0;i--)
                {
                    if(b[i][j]=='.')
                    {
                        rotate(i,j);
                        break;
                    }
                }
            }
        }
        fr=kpiece('R');
        fb=kpiece('B');
        printf("Case #%d: ",c+1);
        if((fr==1)&&(fb==1))
        {
            printf("Both\n");
        }
        else if(fr==1)
        {
            printf("Red\n");
        }
        else if(fb==1)
        {
            printf("Blue\n");
        }
        else
        {
            printf("Neither\n");
        }
    }
    return 0;
}

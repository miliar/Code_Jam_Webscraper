#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;

int c,r;
char map[55][55];
int cut[55];
int sum;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    int h=1;
    scanf("%d",&t);
    while(t--)
    {
        int flag=0;
        memset(cut,0,sizeof(cut));
        sum=0;
        scanf("%d%d",&r,&c);
        int i,j;
        for(i=0;i<r;i++)
        {
            scanf("%s",map[i]);
            for(j=0;j<c;j++)
            {
                if(map[i][j]=='#')
                {
                    sum++;
                    cut[i]++;

                }


            }if((cut[i]%2)!=0)
                {
                    flag=1;
                }
        }
        printf("Case #%d:\n",h++);
        if(flag||sum%4)
        {
            printf("Impossible\n");
            continue;
        }
        for(i=0;i<r;i++)
        {
            for(j=0;j<c;j++)
            {
                if(map[i][j]=='#')
                {
                    map[i][j]='/';
                    map[i][j+1]='\\';
                    map[i+1][j]='\\';
                    map[i+1][j+1]='/';
                }
            }
        }
        for(i=0;i<r;i++)
        {
            printf("%s\n",map[i]);
        }
    }
    return 0;
}

#include <iostream>

using namespace std;
char inp[100][100], inpt[100][100];
int k, n, i, j;
int chk()
{
    //printf("in function\n");
    int p, q, cnt;
    if(inp[i][j]=='R')
    {
        cnt=0;
        for(p=j;p<n;p++)
        {
            if(inp[i][p]=='R')
                cnt++;
            else break;
        }
        for(p=j-1;p>=0;p--)
        {
            if(inp[i][p]=='R')
                cnt++;
            else break;
        }
        if(cnt>=k)return 1;
        cnt = 0;
        for(p=i;p<n;p++)
        {
            if(inp[p][j]=='R')
                cnt++;
            else break;
        }
        for(p=i-1;p>=0;p--)
        {
            if(inp[p][j]=='R')
                cnt++;
            else break;
        }
        if(cnt>=k)return 1;
        cnt = 0;
        for(p=i,q=j;p<n && q<n;p++,q++)
        {
            if(inp[p][q]=='R')
                cnt++;
            else break;
        }
        for(p=i-1,q=j-1;p>=0 && q>=0;p--,q--)
        {
            if(inp[p][q]=='R')
                cnt++;
            else break;
        }
        if(cnt>=k)return 1;
        cnt = 0;
        for(p=i,q=j;p<n && q>=0;p++,q--)
        {
            if(inp[p][q]=='R')
                cnt++;
            else break;
        }
        for(p=i-1,q=j+1; p>=0 && q<n; p--,q++)
        {
            if(inp[p][q]=='R')
                cnt++;
            else break;
        }
        if(cnt>=k)return 1;
    }
    else
    {
        cnt=0;
        for(p=j;p<n;p++)
        {
            if(inp[i][p]=='B')
                cnt++;
            else break;
        }
        for(p=j-1;p>=0;p--)
        {
            if(inp[i][p]=='B')
                cnt++;
            else break;
        }
        if(cnt>=k)return 2;
        cnt = 0;
        for(p=i;p<n;p++)
        {
            if(inp[p][j]=='B')
                cnt++;
            else break;
        }
        for(p=i-1;p>=0;p--)
        {
            if(inp[p][j]=='B')
                cnt++;
            else break;
        }
        if(cnt>=k)return 2;
        cnt = 0;
        for(p=i,q=j;p<n && q<n;p++,q++)
        {
            if(inp[p][q]=='B')
                cnt++;
            else break;
        }
        for(p=i-1,q=j-1;p>=0 && q>=0;p--,q--)
        {
            if(inp[p][q]=='B')
                cnt++;
            else break;
        }
        if(cnt>=k)return 2;
        cnt = 0;
        for(p=i,q=j;p<n && q>=0;p++,q--)
        {
            if(inp[p][q]=='B')
                cnt++;
            else break;
        }
        for(p=i-1,q=j+1; p>=0 && q<n; p--,q++)
        {
            if(inp[p][q]=='B')
                cnt++;
            else break;
        }
        if(cnt>=k)return 2;
    }
    return 0;
}
int main()
{
    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    int test, c, dt[100], r, f1, f2, f, m, cs=1;

    scanf("%d", &test);
    while(test--)
    {
        scanf("%d %d ", &n, &k);
        //memset(dt, 0, sizeof(dt));
        for(i=0;i<n;i++)
        {
            gets(inpt[i]);
            c=0;
            f=0;
            for(j=n-1;j>=0;j--)
            {
                if(inpt[i][j]!='.')
                {
                   c++;
                }
            }
            dt[i]=c;
        }

        for(i=0;i<n;i++)
        {
            for(j=0;j<(n-dt[i]);j++)
            {
                inp[i][j]='.';
            }
            for(m=0;m<n;m++)
            {
                if(inpt[i][m]!='.')
                {
                    inp[i][j]=inpt[i][m];
                    j++;
                }
            }
        }

        /*for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                printf("%c", inp[i][j]);
            }
            printf("\n");
        }*/
        r=0;
        f1=f2=0;
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                //printf("now %c\n", inp[i][j]);
                if(inp[i][j]!='.')
                {
                    //if(i>0 && inp[i][j]==inp[i-1][j])continue;
                    //if(j>0 && inp[i][j]==inp[i][j-1])continue;
                    //if(i>0 && j>0)
                    //{
                    //    if(inp[i][j]==inp[i-1][j-1])continue;
                    //    if(inp[i][j]==inp[i-1][j+1])continue;
                    //}
                    r = chk();
                    //printf("now r %d\n", r);
                    if(r==1)
                    f1=1;
                    if(r==2)
                    f2=1;
                }
                //if(r) break;
                //printf("running\n");
            }
            //if(r)break;
        }
        if(f1==1 && f2==1)
        printf("Case #%d: Both\n", cs++);
        else if(f1 == 1)
        printf("Case #%d: Red\n", cs++);
        else if(f2==1)
        printf("Case #%d: Blue\n", cs++);
        else printf("Case #%d: Neither\n", cs++);
    }
    return 0;
}

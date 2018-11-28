#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int q[10001];
bool p[10001];
int idx;
int abs(int a)
{
    if(a>=0) return a;
    else return -a;
}
main()
{
    freopen("xxx.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int t;
    int pp;
    int n;
    char ch[2];
    int num;
    int ans=0;
    int o=1,b=1;
    scanf("%d",&t);
    int i,j,c;
    for(pp=0;pp<t;pp++)
    {
        ans=0;
        idx=0;
        o=1;
        b=1;
        scanf("%d",&n);
        for(j=0;j<n;j++)
        {
            scanf("%1s %d",ch,&num);
            q[idx]=num;
            if(ch[0]=='O') p[idx]=0;
            else if(ch[0]=='B') p[idx]=1;
            idx++;
        }   
        p[idx]=2;
        for(i=0;i<idx;i++)
        {
            if(p[i]==0)//O
            {
                ans+=(abs(q[i]-o)+1);
                for(c=0;i+c<idx;c++) if(p[i+c]==1) break;
                if(p[i+c]==1)
                {
                    if(abs(q[i+c]-b)<=(abs(q[i]-o)+1))
                    {
                        b=q[i+c];
                    }
                    else
                    {
                        if(q[i+c]>b)
                        {
                            b+=(abs(q[i]-o)+1);
                        }
                        else
                        {
                            b-=(abs(q[i]-o)+1);
                        }
                    }
                }
                o=q[i];
            }
            else if(p[i]==1)//B
            {
                ans+=(abs(q[i]-b)+1);
                for(c=0;i+c<idx;c++) if(p[i+c]==0) break;
                if(p[i+c]==0)
                {
                    if(abs(q[i+c]-o)<=(abs(q[i]-b)+1))
                    {
                        o=q[i+c];
                    }
                    else
                    {
                        if(q[i+c]>o)
                        {
                            o+=(abs(q[i]-b)+1);
                        }
                        else
                        {
                            o-=(abs(q[i]-b)+1);
                        }
                    }
                }
                b=q[i];
            }
        }
        printf("Case #%d: %d\n",pp+1,ans);
    }
    scanf(" ");
}

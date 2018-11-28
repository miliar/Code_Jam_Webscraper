#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <string.h>
#define lim 55
using namespace std;

int i,j,k,n,test,y,x,t,kase;
int sum[lim][lim],sm[lim][lim],ssum[lim][lim],ssm[lim][lim];
char str[lim][lim],st[lim][lim],strin[lim],ch,chh;
bool B,R;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>test;
    while(test--)
    {
        cin>>n>>k;
        for(i=0;i<n;i++)
            scanf("%s",st[i]);


        for(i=n-1,t=0;i>=0;i--,t++)
        {
            for(j=0;j<n;j++)
                sum[i][j]=sm[i][j]=ssum[i][j]=ssm[i][j]=0;
            sscanf(st[i],"%s",strin);

            for(y=n-1,x=n-1;y>=0;y--)
                if(strin[y]!='.')
                    str[x--][t]=strin[y];
            for(;x>=0;x--)str[x][t]='.';

        }

        B = R = 0;

        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
            {
                ch = str[i][j];
                if(ch!='.')
                    if(sum[i][j]>=k-1)
                    {
                        if(ch=='R')R = 1;
                        else B = 1;
                    }

                if(j!=n-1)
                {
                    ch = str[i][j];
                    chh = str[i][j+1];
                    if(ch!='.' && ch==chh)
                    {
                        if(sum[i][j]+1>=k-1)
                        {
                            if(ch=='R')R = 1;
                            else B = 1;
                        }
                        sum[i][j+1]=sum[i][j]+1;
                    }
                }
                if(i!=n-1)
                {
                    ch = str[i][j];
                    chh = str[i+1][j];
                    if(ch!='.' && ch==chh)
                    {
                        if(sm[i][j]+1>=k-1)
                        {
                            if(ch=='R')R = 1;
                            else B = 1;
                        }
                        sm[i+1][j]=sm[i][j]+1;
                    }
                }
                if(i!=n-1 && j!=0)
                {
                    ch = str[i][j];
                    chh = str[i+1][j-1];
                    if(ch!='.' && ch==chh)
                    {
                        if(ssum[i][j]+1>=k-1)
                        {
                            if(ch=='R')R = 1;
                            else B = 1;
                        }
                        ssum[i+1][j-1]=ssum[i][j]+1;
                    }
                }
                if(i!=n-1 && j!=n-1)
                {
                    ch = str[i][j];
                    chh = str[i+1][j+1];
                    if(ch!='.' && ch==chh)
                    {
                        if(ssm[i][j]+1>=k-1)
                        {
                            if(ch=='R')R = 1;
                            else B = 1;
                        }
                        ssm[i+1][j+1]=ssm[i][j]+1;
                    }
                }

            }
            printf("Case #%d: ",++kase);
            if(R&&B)printf("Both\n");
            else if(R)printf("Red\n");
            else if(B)printf("Blue\n");
            else printf("Neither\n");
            /*for(i=0;i<n;i++,cout<<endl)
                for(j=0;j<n;j++)printf("%d ",sum[i][j]);
            cout<<endl;
            for(i=0;i<n;i++,cout<<endl)
                for(j=0;j<n;j++)printf("%d ",ssum[i][j]);
            cout<<endl;
            cout<<endl;
            for(i=0;i<n;i++,cout<<endl)
                for(j=0;j<n;j++)printf("%d ",sm[i][j]);
            cout<<endl;
            for(i=0;i<n;i++,cout<<endl)
                for(j=0;j<n;j++)printf("%d ",ssm[i][j]);*/
    }
    return 0;
}


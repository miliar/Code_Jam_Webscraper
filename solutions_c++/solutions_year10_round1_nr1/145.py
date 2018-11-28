#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <set>
#include <algorithm>
#include <vector>

using namespace std;

int t,iii;
int n,k,i,j,l;
int tmp1,tmp2,xxx;
char in[105][105],in2[105][105];
int r,b;
int chk1,chk2;

bool is(int tmpx,int tmpy)
{
    if(tmpx>=0&&tmpx<n&&tmpy>=0&&tmpy<n)
    return 1;
    else
    return 0;
}

int main()
{
    scanf("%d",&t);
    for(iii=0;iii<t;iii++)
    {
        r=0;
        b=0;
        scanf("%d %d",&n,&k);
        for(i=0;i<n;i++)
        {
            scanf("%s",in[i]);
        }
        for(xxx=1;xxx<=n;xxx++)
        {
            for(j=n-2;j>=0;j--)
            {
                for(i=0;i<n;i++)
                {
                    if(in[i][j+1]=='.')
                    {
                        in[i][j+1]=in[i][j];
                        in[i][j]='.';
                    }
                }
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                for(tmp1=-1;tmp1<=1;tmp1++)
                {
                    for(tmp2=-1;tmp2<=1;tmp2++)
                    {
                        if(tmp1!=0||tmp2!=0)
                        {
                            chk1=1;
                            chk2=1;
                            for(l=0;l<k;l++)
                            {
                                if(!is(i+tmp1*l,j+tmp2*l)||in[i+tmp1*l][j+tmp2*l]!='R')
                                chk1=0;
                                if(!is(i+tmp1*l,j+tmp2*l)||in[i+tmp1*l][j+tmp2*l]!='B')
                                chk2=0;
                            }
                            if(chk1==1)
                            r=1;
                            if(chk2==1)
                            b=1;
                        }
                    }
                }
            }
        }
        printf("Case #%d: ",iii+1);
        if(r==0&&b==0)
        printf("Neither\n");
        else if(r==1&&b==0)
        printf("Red\n");
        else if(r==0&&b==1)
        printf("Blue\n");
        else
        printf("Both\n");
    }
    return 0;
}

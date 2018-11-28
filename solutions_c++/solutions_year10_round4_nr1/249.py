#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstring>

using namespace std;

int t,iii;
int n,val[205][205],i,j,m;
int valtmp[205][205];
int tmp[205][205];
int k,l;
int chk;
int answer;

void ans()
{
    for(k=0;k<=55;k++)
    {
        if((k+n)*(k+n)-n*n>=answer)
        break;
        for(l=0;l<=55;l++)
        {
            if((k+n+l)*(k+n+l)-n*n>=answer)
            break;
            chk=1;
            for(i=1;i<=155;i++)
            {
                for(j=1;j<=155;j++)
                {
                    tmp[i][j]=-1;
                }
            }
            for(i=1;i<=n;i++)
            {
                for(j=1;j<=i;j++)
                {
                    tmp[i+k][j]=val[i][j];
                }
            }
            m=n+k+l;
            for(i=n+1;i<=2*n;i++)
            {
                for(j=1;j<=2*n-i;j++)
                {
                    if(i+k<=m)
                    {
                        tmp[i+k][j+i-n]=val[i][j];
                    }
                    else
                    {
                        tmp[i+k][j+l]=val[i][j];
                    }
                }
            }
            for(i=1;i<=m;i++)
            {
                for(j=1;j<=i;j++)
                {
                    if(tmp[i][j]!=tmp[i][i+1-j]&&tmp[i][j]!=-1&&tmp[i][i+1-j]!=-1)
                    {
                        chk=0;
                    }
                    if(tmp[i][j]!=tmp[2*m-i][j]&&tmp[i][j]!=-1&&tmp[2*m-i][j]!=-1)
                    {
                        chk=0;
                    }
                }
            }
            for(i=m+1;i<=2*m;i++)
            {
                for(j=1;j<=2*m-i;j++)
                {
                    if(tmp[i][j]!=tmp[i][2*m-i+1-j]&&tmp[i][j]!=-1&&tmp[i][2*m-i+1-j]!=-1)
                    {
                        chk=0;
                    }
                }
            }
            if(chk==1)
            {
                if((k+n+l)*(k+n+l)-n*n<answer)
                {
                    answer=(k+n+l)*(k+n+l)-n*n;
                }
            }
        }
    }
    return ;
}

int main()
{
    scanf("%d",&t);
    for(iii=1;iii<=t;iii++)
    {
        scanf("%d",&n);
        for(i=1;i<=200;i++)
        {
            for(j=1;j<=200;j++)
            {
                val[i][j]=-1;
            }
        }
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=i;j++)
            {
                scanf("%d",&valtmp[i][j]);
            }
        }
        for(i=n+1;i<=2*n-1;i++)
        {
            for(j=1;j<=2*n-i;j++)
            {
                scanf("%d",&valtmp[i][j]);
            }
        }
        answer=1000000000;
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=i;j++)
            {
                val[i][j]=valtmp[i][j];
            }
        }
        for(i=n+1;i<=2*n-1;i++)
        {
            for(j=1;j<=2*n-i;j++)
            {
                val[i][j]=valtmp[i][j];
            }
        }
        ans();
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=i;j++)
            {
                val[i][j]=valtmp[i][i+1-j];
            }
        }
        for(i=n+1;i<=2*n-1;i++)
        {
            for(j=1;j<=2*n-i;j++)
            {
                val[i][j]=valtmp[i][2*n-i+1-j];
            }
        }
        ans();
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=i;j++)
            {
                val[i][j]=valtmp[2*n-i][j];
            }
        }
        for(i=n+1;i<=2*n-1;i++)
        {
            for(j=1;j<=2*n-i;j++)
            {
                val[i][j]=valtmp[2*n-i][j];
            }
        }
        ans();
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=i;j++)
            {
                val[i][j]=valtmp[2*n-i][i+1-j];
            }
        }
        for(i=n+1;i<=2*n-1;i++)
        {
            for(j=1;j<=2*n-i;j++)
            {
                val[i][j]=valtmp[2*n-i][2*n-i+1-j];
            }
        }
        ans();
        printf("Case #%d: %d\n",iii,answer);
    }
	return 0;
}

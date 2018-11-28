#include <iostream>
#include <cstdio>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cstring>

#define INF 1000000000

using namespace std;

int t,iii;
int p,i,j,k,l;
int val[10000];
int mic[3000][20];
int ans;

int minn(int tmpx,int tmpy)
{
    if(tmpx<tmpy)
    return tmpx;
    else
    return tmpy;
}

int main()
{
    scanf("%d",&t);
    for(iii=1;iii<=t;iii++)
    {
        scanf("%d",&p);
        for(i=p;i>=0;i--)
        {
            for(j=0;j<(1<<i);j++)
            scanf("%d",&val[(1<<i)+j]);
        }
        /*
        for(i=1;i<=((1<<(p+1))-1);i++)
        {
            printf("%d ",val[i]);
        }
        printf("\n");
        */
        for(i=(1<<p)-1;i>=1;i--)
        {
            for(k=0;k<=p;k++)
            {
                mic[i][k]=INF;
                if(i>=(1<<(p-1)))
                {
                    if(k<=minn(val[2*i],val[2*i+1])-1)
                    {
                        mic[i][k]=minn(mic[i][k],0);
                    }
                    if(k<=minn(val[2*i],val[2*i+1]))
                    {
                        mic[i][k]=minn(mic[i][k],val[i]);
                    }
                }
                else
                {
                    for(j=0;j<=p;j++)
                    {
                        for(l=0;l<=p;l++)
                        {
                            if(k<=minn(j,l)-1)
                            {
                                mic[i][k]=minn(mic[i][k],mic[2*i][j]+mic[2*i+1][l]);
                            }
                            if(k<=minn(j,l))
                            {
                                mic[i][k]=minn(mic[i][k],mic[2*i][j]+mic[2*i+1][l]+val[i]);
                            }
                        }
                    }
                }
                //printf("%d %d %d %d\n",i,val[i],k,mic[i][k]);
            }
        }
        ans=INF;
        for(k=0;k<=p;k++)
        {
            if(mic[1][k]<ans)
            ans=mic[1][k];
        }
        printf("Case #%d: %d\n",iii,ans);
    }
	return 0;
}

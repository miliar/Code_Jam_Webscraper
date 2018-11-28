#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>

using namespace std;
int j[210];
double res[210];
int flag[210];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n;
    scanf("%d",&t);
    int sum=0;
    for(int k=0;k<t;k++)
    {
        sum=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&j[i]);
            sum+=j[i];
            flag[i]=1;
        }
        printf("Case #%d:",k+1);

        bool f=true;
        int total=n;
        int totalsum=sum;
        while(f)
        {
            for(int i=0;i<n;i++)
            {
                if(flag[i]==1)
                {
                    res[i]=(1.0-(double)(total*j[i]-totalsum)/(double)sum)/(double)total;
                    if(res[i]<0)
                    {
                        res[i]=0;
                        flag[i]=0;
                        //cout<<"i="<<i<<"sum="<<sum<<endl;
                        totalsum-=j[i];
                        total--;
                        //cout<<"i="<<i<<"sum="<<sum<<endl;
                        break;
                    }
                }

                if(i==n-1||total==0)f=false;
            }
        }
        //cout<<"total="<<total<<endl;
        for(int i=0;i<n;i++)
        {
            //cout<<"flag="<<i<<" :"<<flag[i]<<endl;
            /*if(flag[i])
            {
                double ret=(1.0-(double)(total*j[i]-totalsum)/(double)sum)/(double)total;

                printf(" %.6f",ret*100);
            }
            else
            {
                double ret=0;
                printf(" %.6f",ret);
            }*/
            printf(" %.6f",res[i]*100);
        }
        printf("\n");
    }

    return 0;
}

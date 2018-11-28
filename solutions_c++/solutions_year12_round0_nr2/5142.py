#include<iostream>
#include<unistd.h>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<string.h>
#include<algorithm>

using namespace std;

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t;
    int n,s,p;
    int score[5];
    int sur[5];
    int nor[5];
    int flag[5];
    scanf("%d",&t);

    for(int j=1;j<=t;j++)
    {
        int y=0;
        printf("Case #%d:",j);
        scanf("%d %d %d",&n,&s,&p);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&score[i]);
        }
        for(int i=0;i<n;i++)
        {
            if(score[i]>=5)
            {
                sur[i]=(score[i]+4)/3;
                nor[i]=(score[i]+2)/3;
            }
            else if(score[i]==0)
            {
                sur[i]=0;
                nor[i]=0;
            }
            else if(score[i]==5)
            {
                sur[i]=3;
                nor[i]=2;
            }
            else if(score[i]==4)
            {
                sur[i]=2;
                nor[i]=2;
            }
            else if(score[i]==3)
            {
                sur[i]=2;
                nor[i]=1;
            }
            else if(score[i]==2)
            {
                sur[i]=2;
                nor[i]=1;
            }
            else if(score[i]==1)
            {
                sur[i]=1;
                nor[i]=1;
            }
            if(sur[i]>=p && nor[i]>=p)
            {
                flag[i]=2;
                y++;
            }
            else if(sur[i]>=p && nor[i]<p)
            {
                flag[i]=1;
            }
            else
            {
                flag[i]=0;
            }
        }
        for(int i=0;i<n;i++)
        {
            if(flag[i]==1)
            {
                if(s>0)
                {
                    y++;
                    s--;
                }
            }
        }

        printf(" %d\n",y);
    }

    return 0;
}

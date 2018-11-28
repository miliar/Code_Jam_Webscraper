#include<iostream>
#include<cstdio>
using namespace std;

int a[100],n,s,p;
int sol[31][2][3];
int calculate()
{
        int i,j,k,val;

        for(i=0;i<=10;i++)
        {
            for(j=i;j<=i+2;j++)
            {
                for(k=j;k<=i+2;k++)
                {
                    if(k<j)
                    continue;
                    val=i+j+k;

                    if(k==i+2||j==i+2||k==j+2)
                    {
                        sol[val][1][0]=i;
                        sol[val][1][1]=j;
                        sol[val][1][2]=k;

                    }
                    else
                    {
                        sol[val][0][0]=i;
                        sol[val][0][1]=j;
                        sol[val][0][2]=k;

                    }
                }
            }
        }
}
int main()
{
    int t,i,j,count,flag,tot;

    calculate();

    scanf("%d",&t);
    tot=t;
    while(t--)
    {
        count=0;
        flag=0;

        scanf("%d%d%d",&n,&s,&p);

        for(i=0;i<n;i++)
        scanf("%d",a+i);

        for(i=0;i<n;i++)
        {
            flag=0;
            for(j=0;j<3;j++)
            {
                if(sol[a[i]][0][j]>=p)
                {
                    //cout<<a[i]<<" "<<sol[a[i]][0][j]<<"\n";
                    //getchar();
                    count++;
                    flag=1;
                    break;
                }

            }

            if(flag==0&&s!=0)
            {
                for(j=0;j<3;j++)
                {
                    if(sol[a[i]][1][j]>=p)
                    {
                        //cout<<a[i]<<" "<<sol[a[i]][0][j]<<"\n";
                        //getchar();
                        count++;
                        s--;
                        break;
                    }
                }
            }
        }

        printf("Case #%d: %d\n",tot-t,count);

    }
    return 0;
}

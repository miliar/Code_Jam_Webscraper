#include<iostream>
#include<cstdio>
using namespace std;

void board();

int array[100];
int n,s,p;
int ans[31][2][3];
int main()
{
    int test,total,i,j;

    int times, point;

    board();

    cin>>test;
    total=test;
    while(test--)
    {scanf("%d%d%d",&n,&s,&p);

        for(i=0;i<n;i++)
        scanf("%d",array+i);

        times=0;
        point=0;


        for(i=0;i<n;i++)
        {
            point=0;
            for(j=0;j<3;j++)
            {
                if(ans[array[i]][0][j]>=p)
                {
                    point=1;
                    times++;
                    break;
                }

            }

            if(point==0&&s!=0)
            {
                for(j=0;j<3;j++)
                {
                    if(ans[array[i]][1][j]>=p)
                    {
                        times++;
                        s--;
                        break;
                    }
                }
            }
        }


        cout<<"Case #"<<total-test<<": "<<times<<"\n";


    }
    return 0;
}
void board()
{
        int i,j,k,number;

        for(i=0;i<=10;i++)
        {
            for(j=i;j<=i+2;j++)
            {
                for(k=j;k<=i+2;k++)
                {
                    if(k<j)
                    continue;
                    number=i+j+k;

if(k==i+2||j==i+2||k==j+2)
                    {
                      ans[number][1][1]=j;
                        ans[number][1][2]=k;
                        ans[number][1][0]=i;


                    }
    else
                    {
                        ans[number][0][0]=i;
                ans[number][0][1]=j;
            ans[number][0][2]=k;

                    }
                }
            }
        }
}

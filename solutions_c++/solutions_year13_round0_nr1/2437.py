#include<iostream>
#include<stdio.h>
#include<climits>
#include<cstring>
#include<math.h>
#include<algorithm>
#include<map>

using namespace std;


char str[4][5];


int main()
{
    int t,flag,flag2;
    char c;
    scanf("%d",&t);
    for(int j=1; j<=t; j++)
    {
        flag=0;
        flag2=0;
        for(int i=0; i<4; i++)
            cin>>str[i];
        for(int i=0; i<4; i++)
        {
            if(flag2)
                break;
            if(str[i][0]=='T')
                c=str[i][1];
            else
                c=str[i][0];
            for(int k=0; k<4; k++)
            {

                if(str[i][k]=='.')
                {
                    flag=1;
                    break;
                }
                if(str[i][k]=='T');
                else if(str[i][k]!=c)
                    break;
                if(k==3)
                {
                    flag2=1;
                    printf("Case #%d: %c won\n",j,c);
                    break;
                }
            }
        }
        if(!flag2)
        {
            for(int i=0; i<4; i++)
            {
                if(flag2)
                    break;
                if(str[0][i]=='T')
                    c=str[1][i];
                else
                    c=str[0][i];
                for(int k=0; k<4; k++)
                {

                    if(str[k][i]=='.')
                    {
                        flag=1;
                        break;
                    }
                    if(str[k][i]=='T');
                    else if(str[k][i]!=c)
                        break;
                    if(k==3)
                    {
                        flag2=1;
                        printf("Case #%d: %c won\n",j,c);
                        break;
                    }
                }
            }
        }
        if(!flag2)
        {
            if(str[0][0]=='T')
                c=str[1][1];
            else
                c=str[0][0];
            for(int i=0; i<4; i++)
            {
                if(str[i][i]=='.')
                    break;
                if(str[i][i]=='T');
                else if(str[i][i]!=c)
                    break;
                if(i==3)
                {
                    flag2=1;
                    printf("Case #%d: %c won\n",j,c);
                    break;
                }
            }
        }
        if(!flag2)
        {
            if(str[0][3]=='T')
                c=str[1][2];
            else
                c=str[0][3];
            for(int i=0; i<4; i++)
            {
                if(str[i][3-i]=='.')
                    break;
                if(str[i][3-i]=='T');
                else if(str[i][3-i]!=c)
                    break;
                if(i==3)
                {
                    flag2=1;
                    printf("Case #%d: %c won\n",j,c);
                    break;
                }
            }
        }
        if((flag2==0)&&(flag==1))
            printf("Case #%d: Game has not completed\n",j);
        if((flag2==0)&&(flag==0))
            printf("Case #%d: Draw\n",j);
    }
    return 0;
}

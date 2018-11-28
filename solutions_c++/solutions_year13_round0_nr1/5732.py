#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
using namespace std;
int main()
{
//    freopen("C:\\Users\\wrathchild\\Desktop\\input.txt","r",stdin);
//    freopen("C:\\Users\\wrathchild\\Desktop\\output.txt","w",stdout);
    int test=0,temp=0;
    scanf("%d",&test);
    for(temp=1;temp<=test;temp++)
    {
        string arr[4];
        int i=0,j=0,o=0,x=0,t=0,dot=0,xwon=0,owon=0;
        for(i=0;i<4;i++)cin>>arr[i];
        dot=0;
        for(i=0;i<4;i++)
        {
            xwon=0;owon=0;x=0;o=0;t=0;
            for(j=0;j<4;j++)
            {
                if(arr[i][j]=='X')x++;
                else if(arr[i][j]=='O')o++;
                else if(arr[i][j]=='T')t++;
                else dot++;
            }
            if(x==4||(x==3 && t==1))
               {xwon=1;break;}
            else if(o==4||(o==3 && t==1))
               {owon=1;break;}
        }
        dot=0;
        if(xwon!=1 && owon!=1)
        {
            for(i=0;i<4;i++)
        {
            xwon=0;owon=0;x=0;o=0;t=0;
            for(j=0;j<4;j++)
            {
                if(arr[j][i]=='X')x++;
                else if(arr[j][i]=='O')o++;
                else if(arr[j][i]=='T')t++;
                else dot++;
            }
            if(x==4||(x==3 && t==1))
               {xwon=1;break;}
            else if(o==4||(o==3 && t==1))
               {owon=1;break;}
        }
        }
            dot=0;
         if(xwon!=1 && owon!=1)
        {
            xwon=0;owon=0;x=0;o=0;t=0;
            for(i=0;i<4;i++)
            {
                if(arr[i][i]=='X')x++;
                else if(arr[i][i]=='O')o++;
                else if(arr[i][i]=='T')t++;
                else dot++;
            }
            if(x==4||(x==3 && t==1))
               {xwon=1;}
            else if(o==4||(o==3 && t==1))
               {owon=1;}
        }
            dot=0;
        if(xwon!=1 && owon!=1)
        {
            xwon=0;owon=0;x=0;o=0;t=0;
               for(i=0;i<4;i++)
        {

            for(j=0;j<4;j++)
            {
                if(i+j==3)
                {
                    if(arr[j][i]=='X')x++;
                    else if(arr[j][i]=='O')o++;
                    else if(arr[j][i]=='T')t++;
                    else dot++;
                }
            }
            if(x==4||(x==3 && t==1))
               {xwon=1;break;}
            else if(o==4||(o==3 && t==1))
               {owon=1;break;}
        }
        }

        if(xwon==1)printf("Case #%d: X won\n",temp);
        else if(owon==1)printf("Case #%d: O won\n",temp);
        else if(xwon==0 && owon==0 && dot==0)printf("Case #%d: Draw\n",temp);
        else printf("Case #%d: Game has not completed\n",temp);
    }
    return 0;
}


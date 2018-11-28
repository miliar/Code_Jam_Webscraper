#include<vector>
#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<time.h>
#include<assert.h>
#include<stdlib.h>
using namespace std;
char arr[5][5];
int main()
{
    int t;
    scanf("%d",&t);

    for(int i=1;i<=t;i++)
    {
      int  dot=0;
        for(int j=0;j<4;j++)
        {
            scanf("%s",arr[j]);
            for(int k=0;k<4;k++)
            if(arr[j][k]=='.')
            dot=1;
        }
        int XW=0,OW=0;
        for(int j=0;j<4;j++)
        {
            int x=0,o=0,t=0,d=0;
            for(int k=0;k<4;k++)
            {
              if(arr[j][k]=='X')
              x=1;
               if(arr[j][k]=='O')
              o=1;
               if(arr[j][k]=='T')
              t=1;
               if(arr[j][k]=='.')
              d=1;
            }

            if(x&&!o&&!d)
            XW=1;
             if(o&&!x&&!d)
            OW=1;
//cout<<x<<" "<<o<<" "<<d<<"\n";
               x=o=t=d=0;

            for(int k=0;k<4;k++)
            {
              if(arr[k][j]=='X')
              x=1;
               if(arr[k][j]=='O')
              o=1;
               if(arr[k][j]=='T')
              t=1;
               if(arr[k][j]=='.')
              d=1;
            }
//cout<<x<<" "<<o<<" "<<d<<"\n";
            if(x&&!o&&!d)
            XW=1;
             if(o&&!x&&!d)
            OW=1;

        }
          int x=0,o=0,t=0,d=0;
    for(int j=0;j<4;j++)
    {


              if(arr[j][j]=='X')
              x=1;
               if(arr[j][j]=='O')
              o=1;
               if(arr[j][j]=='T')
              t=1;
               if(arr[j][j]=='.')
              d=1;



    }
   if(x&&!o&&!d)
            XW=1;
             if(o&&!x&&!d)
            OW=1;
//cout<<x<<" "<<o<<" "<<d<<"\n";
  x=o=t=d=0;
     for(int j=0;j<4;j++)
    {


              if(arr[j][3-j]=='X')
              x=1;
               if(arr[j][3-j]=='O')
              o=1;
               if(arr[j][3-j]=='T')
              t=1;
               if(arr[j][3-j]=='.')
              d=1;



    }
       if(x&&!o&&!d)
            XW=1;
             if(o&&!x&&!d)
            OW=1;
//cout<<x<<" "<<o<<" "<<d<<"\n";


        if(XW)
        printf("Case #%d: X won\n",i);
        else if(OW)
           printf("Case #%d: O won\n",i);
           else if(dot)
            printf("Case #%d: Game has not completed\n",i);
            else
             printf("Case #%d: Draw\n",i);


    }
    return 0;
}

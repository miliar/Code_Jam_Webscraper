#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <sstream>
#include <math.h>
#include <algorithm>
#include <list>
#include <map>
using namespace std;

char ar[5][5];
int ir[4][4];

int main()
{

    int i,j,k,t,s,z,n,tp;
    string a,b,c,d;
    i=1;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        bool isc = false;
        for(j=0;j<4;j++)
            scanf("%s",&ar[j]);
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            {
                switch(ar[j][k])
                {
                    case 'X':ir[j][k] = 1;
                    break;
                    case 'O':ir[j][k] = -1;
                    break;
                    case '.':ir[j][k] = 0;
                    isc = true;
                    break;
                    case 'T':ir[j][k] = 1;
                    break;
                }
            }
        bool bx=false,bo=false;
        for(j=0;j<4;j++)
        {
            if(ir[j][0]+ir[j][1]+ir[j][2]+ir[j][3]==4)
                bx = true;
            //if(ir[j][0]+ir[j][1]+ir[j][2]+ir[j][3]==-3)
              //  bo = true;
            if(ir[0][j]+ir[1][j]+ir[2][j]+ir[3][j]==4)
                bx = true;
         //   if(ir[0][j]+ir[1][j]+ir[2][j]+ir[3][j]==-3)
         //       bo = true;
        }
        if(ir[0][0]+ir[1][1]+ir[2][2]+ir[3][3]==4)
            bx = true;
      //  if(ir[0][0]+ir[1][1]+ir[2][2]+ir[3][3]==-3)
      //      bo = true;
        if(ir[0][3]+ir[1][2]+ir[2][1]+ir[3][0]==4)
            bx = true;
      //  if(ir[0][3]+ir[1][2]+ir[2][1]+ir[3][0]==-3)
     //       bo = true;

        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
                if(ar[j][k]=='T')
                    ir[j][k] = -1;

        for(j=0;j<4;j++)
        {
      //      if(ir[j][0]+ir[j][1]+ir[j][2]+ir[j][3]==3)
      //          bx = true;
            if(ir[j][0]+ir[j][1]+ir[j][2]+ir[j][3]==-4)
                bo = true;
      //      if(ir[0][j]+ir[1][j]+ir[2][j]+ir[3][j]==3)
      //          bx = true;
            if(ir[0][j]+ir[1][j]+ir[2][j]+ir[3][j]==-4)
                bo = true;
        }
   //     if(ir[0][0]+ir[1][1]+ir[2][2]+ir[3][3]==3)
   //         bx = true;
        if(ir[0][0]+ir[1][1]+ir[2][2]+ir[3][3]==-4)
            bo = true;
   //     if(ir[0][3]+ir[1][2]+ir[2][1]+ir[3][0]==3)
   //         bx = true;
        if(ir[0][3]+ir[1][2]+ir[2][1]+ir[3][0]==-4)
            bo = true;

        if(!bx&&!bo&&!isc)
            printf("Case #%d: Draw\n",i+1);
        else if(bx&&!bo)
            printf("Case #%d: X won\n",i+1);
        else if(!bx&&bo)
            printf("Case #%d: O won\n",i+1);
        else if(!bx&&!bo)
            printf("Case #%d: Game has not completed\n",i+1);
    }
    return 0;
}

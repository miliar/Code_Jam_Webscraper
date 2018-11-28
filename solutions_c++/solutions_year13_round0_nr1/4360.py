#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
//#include<fstream>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
   //freopen("A-small-practice.in","r",stdin);
   //freopen("out.txt","w",stdout);
    int test,i,x,o,x1,o1,t,t1,diagx,diago,diagt,ultadiagx,ultadiago,ultadiagt,j,flagx,flago,dot,k;
    char str[5][5];
   freopen("A-large.in","r",stdin);
   freopen("output.txt","w",stdout);
    scanf("%d",&test);
    getchar();
    k=1;
    while(test--)
    {
      //k=1;
      //getchar();
       dot=diago=ultadiago=diagx=diagt=ultadiagx=ultadiagt=x1=o1=x=o=t=t1=0;
       flagx=0;flago=0;
        for(i=0;i<4;i++)
        {
        for(j=0;j<4;j++)
        scanf("%c",&str[i][j]);
        //scanf("\n");
        getchar();
        //scanf("\n");
        }
      // getchar();
        for(i=0;i<4;i++)
        {
        for(j=0;j<4;j++)
        {
         if(str[i][j]=='X')
         x++;
         if(str[i][j]=='O')
         o++;
         if(str[i][j]=='T')
         t++;
          if(str[j][i]=='X')
         x1++;
         if(str[j][i]=='O')
         o1++;
         if(str[j][i]=='T')
         t1++;
         if(str[i][j]=='.')
         dot++;
         if(i==j)
         {
           if(str[i][j]=='X')
           diagx++;
           if(str[i][j]=='O')
           diago++;
           if(str[i][j]=='T')
           diagt++;
         }
        }
        if((x==3&&t==1)||(x==4)||(x1==3&&t1==1)||(x1==4))
        {
        flagx=1;
        //printf("yo");
        break;
        }
         else if((o==3&&t==1)||(o==4)||(o1==3&&t1==1)||(o1==4))
        {
        flago=1;
        break;
        }
        else
        x=o=x1=o1=t=t1=0;
        }
        //if(x
        if((diagx==3&&diagt==1)||(diagx==4))
        {
        flagx=1;
        //printf("yo");
        }
        if((diago==3&&diagt==1)||(diago==4))
        flago=1;
        
           if(str[0][3]=='X')
           ultadiagx++;
           if(str[0][3]=='O')
           ultadiago++;
           if(str[0][3]=='T')
           ultadiagt++;
            if(str[1][2]=='X')
           ultadiagx++;
           if(str[1][2]=='O')
           ultadiago++;
           if(str[1][2]=='T')
           ultadiagt++;
            if(str[2][1]=='X')
           ultadiagx++;
           if(str[2][1]=='O')
           ultadiago++;
           if(str[2][1]=='T')
           ultadiagt++;
            if(str[3][0]=='X')
           ultadiagx++;
           if(str[3][0]=='O')
           ultadiago++;
           if(str[3][0]=='T')
           ultadiagt++;
         
        if((ultadiagx==3&&ultadiagt==1)||(ultadiagx==4))
        {
        flagx=1;
        //printf("yo");
        }
        if((ultadiago==3&&ultadiagt==1)||(ultadiago==4))
        flago=1;
        if(flagx)
        printf("Case #%d: X won\n",k++);
        else if(flago)
        printf("Case #%d: O won\n",k++);
        else if(dot)
        printf("Case #%d: Game has not completed\n",k++);
        else
        printf("Case #%d: Draw\n",k++);
        //printf("\n");
      // getchar();
       getchar();
       //scanf("\n");
        }
    
    return 0;
}

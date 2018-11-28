#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<cstdio>
using namespace std;

int main()
{
   int i,j,k,t,xcount,ocount,tdetected,flag,emptyCount;
   string arr[4];
   
   scanf("%d",&t);
   
   for(k=1;k<=t;k++)   //rows
   {
      for(i=0;i<4;i++)
      cin>>arr[i];
      flag=0;
      for(i=0;i<4;i++)
      {
        xcount=0;
        ocount=0;
        tdetected=0;
        
        for(j=0;j<4;j++)
        {
          if(arr[i][j]=='X')
          xcount++;
          
          else if(arr[i][j]=='O')
          ocount++;
          
          else if(arr[i][j]=='T')
          tdetected=1;
        }
        if(xcount==4||(xcount==3&&tdetected==1))
        {
          printf("Case #%d: X won\n",k);
          flag=1;
          break;
        }
        if(ocount==4||(ocount==3&&tdetected==1))
        {
          printf("Case #%d: O won\n",k);
          flag=1;
          break;
        }
      }
      
      if(flag==0)  //columns
      {
        for(i=0;i<4;i++)
        {
          xcount=0;
          ocount=0;
          tdetected=0;
        
          for(j=0;j<4;j++)
          {
            if(arr[j][i]=='X')
            xcount++;
          
            else if(arr[j][i]=='O')
            ocount++;
          
            else if(arr[j][i]=='T')
            tdetected=1;
          }
          if(xcount==4||(xcount==3&&tdetected==1))
          {
            printf("Case #%d: X won\n",k);
            flag=1;
            break;
          }
          if(ocount==4||(ocount==3&&tdetected==1))
          {
            printf("Case #%d: O won\n",k);
            flag=1;
            break;
          }
        }
      }
      
      if(flag==0)  //tl-br diagonal
      {
        xcount=0;
        ocount=0;
        tdetected=0;
        
        for(i=0;i<4;i++)
        {
          if(arr[i][i]=='X')
          xcount++;
          
          else if(arr[i][i]=='O')
          ocount++;
          
          else if(arr[i][i]=='T')
          tdetected=1;
        }
        
        if(xcount==4||(xcount==3&&tdetected==1))
        {
          printf("Case #%d: X won\n",k);
          flag=1;
        }
        if(ocount==4||(ocount==3&&tdetected==1))
        {
          printf("Case #%d: O won\n",k);
          flag=1;
        }
      }
      
      if(flag==0)  //tr-bl digonal
      {
        xcount=0;
        ocount=0;
        tdetected=0;
        
        for(i=0;i<4;i++)
        {
          if(arr[i][3-i]=='X')
          xcount++;
          
          else if(arr[i][3-i]=='O')
          ocount++;
          
          else if(arr[i][3-i]=='T')
          tdetected=1;
        }
        
        if(xcount==4||(xcount==3&&tdetected==1))
        {
          printf("Case #%d: X won\n",k);
          flag=1;
        }
        if(ocount==4||(ocount==3&&tdetected==1))
        {
          printf("Case #%d: O won\n",k);
          flag=1;
        }
      }
      
      if(flag==0)  //draw or going on
      {
         emptyCount=0;
         for(i=0;i<4;i++)
         for(j=0;j<4;j++)
         if(arr[i][j]=='.')
         {
          emptyCount++;
         }
         
         if(emptyCount==0)
         printf("Case #%d: Draw\n",k);
         
         else printf("Case #%d: Game has not completed\n",k);
      }
   }
}

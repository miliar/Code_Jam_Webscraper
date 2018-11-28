#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string.h>

using namespace std;

int t;
char arr[5][5];

int cek()
{
    bool o = false, x=false;
     
     //vertikal
     for (int j=0; j<4; j++)
     {
         int px=0, pt=0, po=0;
         for (int i=0; i<4; i++)
         {
             if (arr[i][j]=='O') po+=1;
             if (arr[i][j]=='T') pt+=1;
             if (arr[i][j]=='X') px+=1;
         }
         
         if ((po==3) && (pt==1)) o=true;
         else
         if ((px==3) && (pt==1)) x=true;
         else
         if (po==4) o=true;
         else
         if (px==4) x=true;
         
     }
     
     for (int i=0; i<4; i++)
     {
         int px=0, pt=0, po=0;
         for (int j=0; j<4; j++)
         {
             if (arr[i][j]=='O') po+=1;
             if (arr[i][j]=='T') pt+=1;
             if (arr[i][j]=='X') px+=1;
         }
         if ((po==3) && (pt==1)) o=true;
         else
         if ((px==3) && (pt==1)) x=true;
         else
         if (po==4) o=true;
         else
         if (px==4) x=true;
     }
     
     int px=0, pt=0, po=0;
     for (int i=0; i<4; i++)
     {
         
         int j=i;
         //for (int j=0; j<4; j++)
         //{
             if (arr[i][j]=='O') po+=1;
             if (arr[i][j]=='T') pt+=1;
             if (arr[i][j]=='X') px+=1;
         //}
     }
     
     if ((po==3) && (pt==1)) o=true;
     else
     if ((px==3) && (pt==1)) x=true;
     else
         if (po==4) o=true;
         else
         if (px==4) x=true;
     
     
     
     px=0; pt=0; po=0;
     for (int i=0; i<4; i++)
     {
         
         int j=3-i;
         //for (int j=0; j<4; j++)
         //{
             if (arr[i][j]=='O') po+=1;
             if (arr[i][j]=='T') pt+=1;
             if (arr[i][j]=='X') px+=1;
         //}
     }
     
     if ((po==3) && (pt==1)) o=true;
     else
     if ((px==3) && (pt==1)) x=true;
     else
         if (po==4) o=true;
         else
         if (px==4) x=true;
     
     
     
     
     if ((o==true) && (x==true)) return 1;
     if ((o==true) && (x==false)) return 2;
     if ((o==false) && (x==true)) return 3;
     if ((o==false) && (x==false)) return 4;
 }

int main ()
{
    
    scanf("%d",&t);
    getchar();
    
    for (int k=0; k<t; k++)
    {
        int e=0;
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                scanf("%c",&arr[i][j]);
                if (arr[i][j]=='.') e+=1;
            }
            getchar();
        }
        getchar();
        
        int z=cek();
        
//       cout << z << endl;
        if (z==1) printf("Case #%d: Draw\n",k+1);
        else
        if (z==2) printf("Case #%d: O won\n",k+1);
        else
        if (z==3) printf("Case #%d: X won\n",k+1);
        else
        if (e==0) printf("Case #%d: Draw\n",k+1);
        else
        printf("Case #%d: Game has not completed\n",k+1);
        
    }
    return 0;
}

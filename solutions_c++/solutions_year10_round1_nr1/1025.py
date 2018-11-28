#include "stdio.h"
#include "string.h"

bool flag1,flag2;
int n ,k , len , cunt1 , cunt2;
char map1[51][1000],map2[51][1000];

void check1()
{
    for(int i = 0 ; i < n ;i++)
    {   
      
        cunt1=0;cunt2=0;
        for(int j = 0 ; j < len ;j++)
        { 
            if(map2[i][j] == '.')
               continue;   
            if(map2[i][j]=='R')    
            {
                 cunt1++;
                 if(cunt1 == k)
                    flag1 = true;
                 cunt2 = 0;
                    
            }
            else
            {
                  cunt2++;
                  if(cunt2 == k)
                     flag2 = true;
                  cunt1 = 0;   
            }
             
            
         }
     }
}  

void check2()
{
    for(int i = 0 ; i < len ;i++)
    {
        cunt1=0;cunt2=0;
        for(int j = 0 ; j < n ;j++)
        {
           
            if(map2[j][i]=='R')    
            {
                 cunt1++;
                 if(cunt1 == k)
                    flag1 = true;
                  cunt2 = 0;
            }    
            else if(map2[j][i] == 'B')
            {
                  cunt2++;
                  if(cunt2 == k)
                     flag2 = true;
                  cunt1 = 0;   
            }
            else
            {
                   cunt1 = 0 ;
                   cunt2 = 0; 
            }
           // printf("%d %d %d %d\n",j , i, cunt1,cunt2);
       }
   }
}           

void check3()
{
     for(int i = 0 ; i < n ;i++)
     {
       
         for(int j = 0 ; j < len ;j++)
         {
             cunt1=0;cunt2=0;
             int k1 = i , k2 = j;
             while(k1 < n && k2 >=0 )
             {
                if(map2[k1][k2] == 'R')
                {
                    cunt1++;
                    if(cunt1 == k)
                       flag1 = true;
                    cunt2=0; 
                 }
                 else if(map2[k1][k2] == 'B')
                 {
                    cunt2++;
                    if(cunt2 == k)
                       flag2 = true;
                     cunt1 = 0;   
                 }
                 else
                 {
                    cunt1 = 0 ;
                    cunt2 = 0; 
                 }
                
            //     if(i == 3&&j==6)
             //       printf("%d %d %d %d\n",k1 ,k2, cunt1,cunt2);
                 k1++;k2--;  
              }
            //  printf("%d %d %d %d\n",i , j, cunt1,cunt2);
               cunt1=0;cunt2=0;
              k1 = i , k2 = j;
              while(k1 < n && k2 < len )
              {
                 if(map2[k1][k2] == 'R')
                 {
                     cunt1++;
                     if(cunt1 == k)
                        flag1 = true;
                     cunt2=0;   
                 }
                 else if(map2[k1][k2] == 'B')
                 {
                    cunt2++;
                    if(cunt2 == k)
                       flag2 = true;
                     cunt1 = 0;   
                 }
                 else
                 {
                     cunt1 = 0 ;
                     cunt2 = 0; 
                 }
                 k1++;k2++;
              }
              
           }//printf("\n");
       }
}
                            
int main()
{
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);
     int test;
     scanf("%d",&test);
     //printf("%d\n",test);
     for(int t = 1 ; t <= test ;t++)
     {
         scanf("%d%d",&n , &k);
         for(int i = 0 ; i < n ;i++)
         {
            scanf("%s",map1[i]);
         }
        
         len = strlen(map1[0]);
         for(int i = 0 ; i < n ;i++)
           for(int j = 0 ; j < len;j++)
              map2[i][j] = '.';
              
         for(int i = 0 ; i < n ;i++)
         {
             int c = len - 1;
             for(int j = len - 1 ; j >= 0 ;j--)
             {
                   if((map1[i][j]) != '.')
                   {
                      map2[i][c] = map1[i][j];
                     // printf("%d %c ",c , map2[i][c]);
                      c--;
                   }  
             }//printf("\n");
            // printf("%s\n",map2[i]);
         }
      /*   for(int i= 0 ; i < n ;i++)
         {  for(int j = 0 ; j < len ;j++)
              printf("%c ",map2[i][j]);
              printf("\n");}
        */      
         flag1=flag2=false;
         check1();
         check2();
         check3();
         if(flag1 == true && flag2 == true)
            printf("Case #%d: Both",t);
         else if(flag1 == true)
            printf("Case #%d: Red" ,t);
         else if(flag2 == true)
            printf("Case #%d: Blue",t);
         else
            printf("Case #%d: Neither",t);
         printf("\n");              
     }
    // while(1);
     return 0;
}       

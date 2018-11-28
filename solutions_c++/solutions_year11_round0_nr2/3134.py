#include <stdio.h>
#include <stdlib.h>
#include <map>

using namespace std;


int main()
{
   int t; 
   scanf("%d",&t); 
   
   map<char,int> m;
   
   m['Q']=1;
   m['W']=2;
   m['E']=3;
   m['R']=4;
   m['A']=5;
   m['S']=6;
   m['D']=7;
   m['F']=8;
    
   for(int w=1;w<=t;w++) 
   { 
      char comb[10][10];
      int op[10][10]; 
      for(int i=0;i<10;i++)
      {
        for(int j=0;j<10;j++)
        {
          comb[i][j]='*';    
          op[i][j]=0;
        }      
      }
      
      int c;
      scanf("%d",&c); 
    
      for(int i=1;i<=c;i++) 
      {
        char x,y,z;
        scanf(" %c%c%c",&x,&y,&z);
        
        comb[m[x]][m[y]]=z;  
        comb[m[y]][m[x]]=z;  
      }
      
      int d; 
      scanf("%d",&d);
    
      for(int i=1;i<=d;i++)
      {
         char x,y;
         scanf(" %c%c",&x,&y);
      
         op[m[x]][m[y]]=1;
         op[m[y]][m[x]]=1;
      }
    
      int n; 
      scanf("%d",&n);
      
      char resp[110];
      int p=0;
      
      scanf(" %c",&resp[0]);
      
      for(int i=2;i<=n;i++)
      {
         char x;
         scanf("%c",&x);
         
         if((resp[p]!='*') && (comb[m[x]][m[resp[p]]]!='*'))    
         {
            resp[p]=comb[m[x]][m[resp[p]]];
         }
         else
         {
           int ap=p+1;     
           for(int j=0;j<=p;j++)
           {
              if((resp[j]!='*') && (op[m[resp[j]]][m[x]]==1))
              {
                 ap=j;     
                 break;
              }     
           }       
         
           if(ap!=p+1)   
           {   for(int j=0;j<=p;j++)
              {
                resp[j]='*';     
              }
           }
           else
           {
             p++;
             resp[p]=x;     
           }
            
         
         }
      }
      
      printf("Case #%d: [",w);
      
      int print=0;
      
      for(int i=0;i<=p;i++) 
      {
        if(resp[i]!='*') 
        {
          if(print==0)
          {
            printf("%c",resp[i]);      
            print++;
          }    
          else
          {
            printf(", %c",resp[i]);            
            print++;
          }
        
        }  
      }
      printf("]\n");
      
   }
  return 0;   
}

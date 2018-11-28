#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <vector>
#include <cctype>
#include <memory.h>
//#include<conio.h>

using namespace std;

int main()
{
int t,a[4],b[4],d[2],i,j,ck,chk,k;
char c;
FILE *fp, *fs;

fp= fopen("input.txt","r");
fs= fopen("output.out","w");

fscanf(fp,"%d",&t);

for(k=1;k<=t;k++)
{
memset(a,0,sizeof(a));    
memset(b,0,sizeof(b));    
memset(d,0,sizeof(d));    
chk=0;
ck=0;
fscanf(fp,"%c",&c);
for(i=0;i<4;i++)
     {
     for(j=0;j<4;j++)
            {
            fscanf(fp,"%c",&c);
            
            if(c=='.')
                 {
                 a[i]=-1;   b[j]=-1;
                 if(i==j) d[0]=-1;
                 if(i+j==3) d[1]=-1;  
                 chk=1; 
                 }                
                 
            else if(c=='T') continue;
            
            else if(c=='X')
                 {
                 if(a[i]!=-1 && a[i]!=2) a[i]=1;
                 else a[i]=-1; 
                 
                 if(b[j]!=-1 && b[j]!=2) b[j]=1;
                 else b[j]=-1;
                 
                 if(i==j)
                         {
                         if(d[0]!=-1 && d[0]!=2) d[0]=1;
                         else d[0]=-1;    
                         }   
                 if(i+j==3)
                         {
                         if(d[1]!=-1 && d[1]!=2) d[1]=1;
                         else d[1]=-1;    
                         }              
                 }
                 
            else if(c=='O')
                 {
                 if(a[i]!=-1 && a[i]!=1) a[i]=2;
                 else a[i]=-1; 
                 
                 if(b[j]!=-1 && b[j]!=1) b[j]=2;
                 else b[j]=-1;
                 
                 if(i==j)
                         {
                         if(d[0]!=-1 && d[0]!=1) d[0]=2;
                         else d[0]=-1;    
                         }   
                 if(i+j==3)
                         {
                         if(d[1]!=-1 && d[1]!=1) d[1]=2;
                         else d[1]=-1;    
                         }              
                 }
			//printf("a\n");
			//for(k=0;k<4;k++)
			//		printf("%d  ",a[k]);
					
            }
			fscanf(fp,"%c",&c);
		}
    
    
    for(i=0;i<4;i++)
    {
                    if(a[i]==1) 
                                {fprintf(fs,"Case #%d: X won\n",k); ck=2; break;}
                    else if(a[i]==2)            
                                {fprintf(fs,"Case #%d: O won\n",k); ck=2; break;}
    }  
    //printf("here\n");
    
    if(ck==0) 
    for(i=0;i<4;i++)
    {                if(b[i]==1) 
                                {fprintf(fs,"Case #%d: X won\n",k); ck=3; break;}
                    else if(b[i]==2)            
                                {fprintf(fs,"Case #%d: O won\n",k); ck=3; break;}
    } 
    //printf("here2\n");
           
    if(ck==0)
    for(i=0;i<2;i++)
    {                if(d[i]==1) 
                                {fprintf(fs,"Case #%d: X won\n",k); ck=4; break;}
                    else if(d[i]==2)            
                                {fprintf(fs,"Case #%d: O won\n",k); ck=4; break;}
    } 
    //printf("here3\n");     
               
   if(chk==1 && ck==0)
        fprintf(fs,"Case #%d: Game has not completed\n",k);
        
   printf("here4\n");   
    if(chk==0 && ck==0)
        fprintf(fs,"Case #%d: Draw\n",k);
 
   //printf("here100 \n");
   //getch();
}

return 0;
}

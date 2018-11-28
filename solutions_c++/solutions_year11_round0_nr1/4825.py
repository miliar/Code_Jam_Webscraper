#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
 int n;
 FILE *fp=fopen("outputA.txt","w");
 int t;
 scanf("%d",&t);
 int cnt;
 for(cnt=0;cnt<t;cnt++)
 {
 scanf("%d",&n);
 int i;
 int order[100][2];
 int O[100];
 int B[100];
 int o,b;
 o=b=0;
 
 for(i=0;i<n;i++)
 {
  char robo[3];
  scanf("%s",robo);
  scanf("%d",&order[i][1]); 
  
  if(!strcmp(robo,"O"))
  {
   order[i][0]=0;
   O[o++]=order[i][1];
   }
  else
  {
   order[i][0]=1;
   B[b++]=order[i][1];
   }    
  }
   
 int time=0;
 int posO;
 int posB;
 posO=posB=1;
 int oCount,bCount;
 oCount=bCount=0;
 i=0;
 while(o||b)
 {
     time++;
     //cout<<o<<" "<<b<<endl;
     int noO;
     int noB;
     noO=noB=0;
      if(posO==O[oCount] && order[i][0]==0)
      {
       o--;
       oCount++;
       i++;
       noO=1;
       
      }
      else if(posB==B[bCount] && order[i][0]==1)
      {
        b--;
        bCount++; 
        i++;    
        noB=1; 
               
      }
     
     if(posO<O[oCount] && noO==0)
      posO++;
     else if(posO>O[oCount] && noO==0)
      posO--;
      
     if(posB<B[bCount] && noB==0)
      posB++;
     else if(posB>B[bCount] && noB==0)
      posB--; 
           
     // if((posO==O[oCount] && order[i][0]==0) || (posB==B[bCount] && order[i][0]==1))
     //  i++;
      
            
 }
 
    fprintf(fp,"Case #%d: %d\n",cnt+1,time);
    
}
    
    return 0;
    
}

#include<iostream>
#include<vector>
#include<string>
#include<stack>
#include<queue>
#include<fstream>
#include<stdio.h>
#include <stdlib.h>

#define INPUT "test.txt"
#define FOR(i,n) for(int i=0;i<n;i++)
#include<direct.h>

FILE* ifp = fopen(INPUT,"r+");
FILE* ofp = fopen("output.txt","w+");
//FILE* ifp = stdin;

#define MAXP 100
#define MAXN 10

using namespace std;

int main()
{
int t,n, no, nb,temp;
int a[MAXN], O[MAXN], B[MAXN];
char s[MAXN],str[2];

fscanf(ifp,"%d",&t);

FOR(T,t)
{
        fscanf(ifp,"%d",&n);
         no = nb = 0;
        
        FOR(i,n)
        {
                fscanf(ifp,"%s",str);
                fscanf(ifp,"%d",&temp);
               
                a[i] = temp;
                s[i] = str[0];
                 
                if(str[0]=='O')
                    O[no++]=temp;
                else
                    B[nb++]=temp;
        }
     
      /*  
      FOR(i,n)
              cout<<s[i]<<" "<<a[i]<<endl;
      */
             
      int po=0, pb=0;
      int poso=1, posb=1;
      
      int count=0;
      
      FOR(pa,n)
      {
              if(po<no && s[pa]=='O')
              {
                       int dif=abs(poso-a[pa]);
                       count+=dif+1;
                       
                       if(pb<nb)
                              posb += (B[pb]<posb?-1:1)*min(abs(B[pb]-posb),dif+1);   
                       po++;         
                       poso=a[pa];
              }  
              else
              {
                    int dif=abs(posb-a[pa]);
                    count+=dif+1;
                    
                    if(po<no)
                              poso += (O[po]<poso?-1:1)*min(abs(O[po]-poso),dif+1);   
                    pb++;   
                    posb=a[pa];
              }
               
      }

       fprintf(ofp,"Case #%d: %d\n",T+1,count);
}



   

system("Pause");
return 0;
}

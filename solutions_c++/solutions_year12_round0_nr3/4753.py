#include<iostream>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<stdio.h>
#include<fstream>

using namespace std;


main()
{int cc,n,i,j,a,b,sol,m,z,zz;
 char s[100];
 

 ifstream f("C-small-attempt0.in");
 
 ofstream g("try.out");
 
 f>>n;
 
 for(i=1;i<=n;i++)
 { f>>a>>b;
   sol=0;
   cc=1;
   itoa(a,s,10);
   for(j=1;j<=strlen(s)-1;j++) cc=cc*10;
   for(j=a;j<=b;j++)
    {  m=j;
       itoa(j,s,10);
       for(z=0;z<strlen(s)-1;z++)
         {
          m=(m%cc)*10+m/cc;
          if(a<=j && j<m && m<=b) {sol++;
                                         }
          }
     }     
  g<<"Case #"<<i<<": "<<sol<<endl;
   }   
  
  
 
 
 
 
 
      
f.close(); g.close();   
      
      
getch();}



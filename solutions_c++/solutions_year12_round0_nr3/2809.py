/* Enter your code here. Read input from STDIN. Print output to STDOUT */

#include<iostream>
#include<algorithm>
#include<math.h>
#include<map>
#include<algorithm>
#include<set>
#include<utility>
using namespace std;

#define fr(i,a,b) for(i=(a);i<(b);++i)



int main()
    
    
{ 
    set<pair<long int,long int> > s;
  long  int A,B;
    
    char buffer1[33];
    char buffer2[33];
int i,tt;
long int j,count=0;
	freopen( "C:\\code_jam_io_files\\input.txt", "r", stdin );
	freopen( "C:\\code_jam_io_files\\output.txt", "w", stdout );

scanf("%d",&tt);

for(i=0;i<tt;i++)

{       
     s.clear();
  count=0;
   scanf("%d",&A);
   scanf("%d",&B);
   
     for(j=A;j<=B-1;j++)
           {  
            long int x=10;
                    while(j/x!=0)
                     {
                     long  int k=j%x;
                      long  int v=j/x;
                         x*=10;
                      itoa(k,buffer1,10);
                      itoa(v,buffer2,10);  
                      strcat(buffer1,buffer2);
                     
               long  int r= atoi(buffer1);         
                  
                  if(r>j && r>A && r<=B)
                  { pair<long int,long int> temp_pair=make_pair(j,r);
                    if(s.find(temp_pair)==s.end())
                      {
                        count++;
                    
                       s.insert(temp_pair);  
                       }
                  }
             
                 }
           } 
                printf( "Case #%d: ", i+1 );   
       	  printf( "%d\n", count);  
}
return 0;
}






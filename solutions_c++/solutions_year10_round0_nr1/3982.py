#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
 int number, check, m, n, k, i;
 string output;
 scanf("%d",&number);
 for(i=0 ; i<number ; i++)
 {
 scanf("%d",&n);
 scanf("%d",&k); 
 check = 1;
 m = n;
   if(k == 0)
     check = 0;
 while( m > 0 )
  {
   check = check & (k % 2) ;
   k = k/2 ;
   m-- ;
  }
 if(check == 0)
 	output = "OFF";
 else
 	output = "ON"; 
 cout<< "Case #"<< i+1 << ": " << output << "\n";
 }
 return 0;
}
 

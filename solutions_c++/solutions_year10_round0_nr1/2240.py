#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <ctime>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <sstream>
using namespace std;


int BitAt(int x, int i)
{
    return ( x & (1 << (i-1)) );
}



int main() 
{ 
//    freopen("..\\A.in","r",stdin); 
//    freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout); 
//    freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout); 
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout); 
//    freopen("..\\A-small.in","r",stdin);freopen("..\\A-small.out","w",stdout);
    int t,n,k;
    bool flag;
    while (scanf ("%d",&t)!=EOF)
    {
          
          for (int i=1;i<=t;i++)
          {
              flag=true;

                        scanf ("%d %d",&n,&k);
              printf ("Case #%d: ",i);
              for (int j=1;j<=n;j++)
              {
                  if (BitAt(k,j)==0)
                  {
                     flag=false;
                     break;
                  }    
              }        
              if (flag)
                 printf ("ON\n");
              else
                  printf ("OFF\n");      
          }
    }
    return 0; 
} 




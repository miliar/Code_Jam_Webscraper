 #include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>

#define CLR( x , y ) ( memset( (x) , (y) , sizeof( (x) ) ) )
#define EPS 1e-9

using namespace std;

FILE *in=fopen("C-small-attempt0.in","r");

FILE *out=fopen("C.out","w");

int n;

map < int , int > mp;

int ar[10000];

int main()
{

    int tests,retVal;
    fscanf(in,"%d",&tests);
           
    for(int i = 0 ; i < tests; i++)
    {
     int r , k , n ,indx;
     fscanf(in,"%d",&r);        
     fscanf(in,"%d",&k);
     fscanf(in,"%d",&n);
     retVal = 0;
     indx = 0;
     vector<int> input ;
     for(int j = 0 ; j < n ; j++) {int var ; fscanf(in,"%d",&var); input.push_back(var);}
     for(int j = 0 ; j < r ; j++)
     {
      int sum = 0;
      for(int z = 0 ; z < n; z++ )
      {
        if(sum+input[indx] > k) break;
         sum+=input[indx];
         indx = (indx + 1)%n;        
      }
      retVal += sum;
     }
     fprintf(out,"Case #%d: %d\n",i+1,retVal);
    }
    return 0;
}

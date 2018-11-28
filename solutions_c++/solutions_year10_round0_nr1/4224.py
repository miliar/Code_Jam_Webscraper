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

FILE *in=fopen("A-small-attempt0.in","r");

FILE *out=fopen("A.out","w");

int n;

map < int , int > mp;

int ar[10000];

int main()
{

    int tests;
    fscanf(in,"%d",&tests);
        cout<<"here"<<tests;
    for(int i = 0 ; i < tests; i++)
    {
     int n , k;
     fscanf(in,"%d",&n);        
     fscanf(in,"%d",&k);
     int val = 1 << n;
     if(k % val == val-1)
     		fprintf(out,"Case #%d: ON\n",i+1);
     else
     		fprintf(out,"Case #%d: OFF\n",i+1);
    }
    return 0;
}

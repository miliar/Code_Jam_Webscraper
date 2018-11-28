#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <algorithm>
#include <stack>
#include <queue>
#include <list>
#include <deque>
#include <cmath>
#include <iomanip>
#include <numeric>
#include <functional>
#include <math.h>
#include <string>
#include <cstring>
#include <string.h>
#include <new>
#include <utility>
#include <cassert>
#include <climits>
 
int ROTATIONS(int x,int y)
{
if(x<=99 && y<=99)
{
 y=((y%10)*10)+(y/10);
 if (y==x)
 return 1;
}
else if( x>=100 && y>=100)
{
 y=((y%10)*100)+(y/10);
 
 if (y==x)
 return 1;
 y=((y%10)*100)+(y/10);
 if (y==x)
 return 1;
}
 
 
return 0;
 
}
 
 //Main
int main()
{
using namespace std;
ifstream fi;ofstream fo;
 
 
int test;
cin>>test;
for(int k=0;k<test;k++)
{
 cout<<"Case #"<<(k+1)<<": ";
 int a,b,NETTOTAL=0;
 cin>>a>>b;
 
 for(int x=a;x<=b;x++)
 for(int y=a;y<=b;y++)
 { if(x!=y)
        if (ROTATIONS(x,y)==1) NETTOTAL++;
 }
   cout<<NETTOTAL/2<<endl;
}
 
}
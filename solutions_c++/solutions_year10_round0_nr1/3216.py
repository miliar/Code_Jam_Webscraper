#include <vector>
#include <iterator>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    //////////// 
    ////////
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    long long casos,n,ex,k,p;
    cin >> casos;
    for (int i = 1; i<= casos; i++)
     {
       cin >> n >> k;  
         {
           ex = 1;
           for (int p = 1; p<=n; p++)
               ex = ex*2;
           if (((k+1) % ex) == 0)
            cout <<"Case #" << i << ": "<< "ON" <<endl;
            else     
            cout <<"Case #" << i << ": "<< "OFF" <<endl;
         }
     }     
return 0;
}

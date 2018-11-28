#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main()
    {
    int tc;
    cin >> tc;
    for( int t =0 ; t < tc; ++t) 
         {
         int n, k;
         cin >> n >> k;
         string sol;
         if ( (k % (1<<n)) + 1 == (1<<n)) sol = "ON";
         else sol = "OFF";
         printf("Case #%d: %s\n",t+1,sol.c_str());    
         }      
    return 0;
    }

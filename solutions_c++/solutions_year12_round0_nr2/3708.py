#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <string>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
//---------- macros ----------
#define fp(i,a,b) for(int i=a; i<b; i++)
#define fm(i,a,b) for(int i=a; i>b; i--)

using namespace std;

int main()
{
   int T;
   int kase = 1;
   cin >> T;
   while(kase <= T)
   {
     int n,s,p,tot;
     cin >> n >> s >> p;
     int b = 0;
     while( n-->0)
     {
        cin >> tot;
        if(tot || !p ){
        if((tot-p)/2 > p-2)
         b++;
        else if((tot-p)/2 == p-2  && s>0)
        {
          b++;
          s--;
        }
        }
     }
     cout << "Case #" << kase << ": " << b << endl;
     kase++;
   }
//-----------------------------
   //cout << endl;
   //system("pause");
   return 0;
}

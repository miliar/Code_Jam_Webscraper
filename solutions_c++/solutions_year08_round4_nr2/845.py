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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
main ()
{
      int C,x = 1;
     cin >> C;
     //cout << 1%0 <<"\n";
     //cout << gcd ( 5 ,8 ) <<"\n"; 
     while ( C-- )
     {
           long long i,j,k,N,M,A;
           cin >> N>>M>>A;
           long long x1 = 0 ,y1 = 0 ,a ,b,c,ii,jj,d ,ans;
           bool found = false;
           cout << "Case #"<<x++<<": ";  
           for ( i = 0; i <=N && !found;i++)
               for ( j =0 ;j <=M && !found ;j++)
               {
                   if ( i== 0&& j==0) continue;
                   for ( k =0 ;k <=N && !found ; k++)
                       for ( ii= 0 ;ii <=M && !found ;ii++)
                       {
                           if ( ii == j && k == i )continue;
                           if (  ii == 0 && k == 0) continue;
                           ans = abs ( ( k*j - i*ii) );
                           if ( ans == A )
                           {
                              cout << 0 <<" "<<0 <<" "<<i<<" "<<j<<" "<<k<<" "<<ii<<"\n";
                              found = true;
                              break;
                            }
                       }
               }
               if ( !found )
           cout << "IMPOSSIBLE\n";
     
     }
}

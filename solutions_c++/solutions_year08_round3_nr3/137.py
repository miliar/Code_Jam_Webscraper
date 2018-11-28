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
#define MOD 1000000007
long long Seq [500010 ],Array [500010] ,DP [500010];
main()
{
 int N,x = 1;
     cin >> N;
     while ( N-- )
     {
           long long i,j,k;
           long long  n,m,X,Y,Z;
           cin>>n>>m>>X>>Y>>Z;
           for ( i = 0 ; i < m;i++)
           cin>>Array[i];
           for ( i = 0 ;i <n ;i++)
           {
               DP [i] = 1;
               Seq [i] = Array [i%m];
              // cout << Seq [i] <<" ";
               Array [i%m] = ( X*Array[i%m] + Y* (i+1) )%Z;
           }
           //cout <<"\n";
           for  (i = 0 ; i < n ;i++)
                for ( j = i+1; j < n ;j++)
                {
                    if ( Seq [j] > Seq [i]  )
                    {
                          DP[j] +=  ( DP[i]%MOD );
                          DP [j] %= MOD;
                    }
                }
           long long ans = 0;
           for ( i = 0; i < n ;i++ )
           {
               ans += ( DP[i]%MOD);
               ans %= MOD;
           }
           cout <<"Case #"<<x++<<":"<<" "<<ans<<"\n";
     }
}
           

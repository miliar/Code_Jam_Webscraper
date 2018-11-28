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
struct Key
{
       long long indx,freq;
}key [1010];
bool cmp ( Key a ,Key b )
{
     if ( a.freq > b.freq ) return true;
     if ( a.freq < b.freq ) return false;
     if ( a.indx > b.indx ) return true;
     return false;
}
main ()
{
     int N,X = 1;
     cin >> N;
     while ( N-- )
     {
           long long i,j,k;
           long long P,K,L;
           cin >> P>>K>>L;
           for ( i = 0; i < L ;i++)
           cin>>key[i].freq,key[i].indx = i;
           sort ( key,key+L,cmp );
           long long ans  = 0;
           for ( i = 0; i < L ; i++)
           {
               ans += key[i].freq *(1LL+i/K);
           }
            cout <<"Case #"<<X++<<":"<<" "<<ans<<"\n";
     }
}
               

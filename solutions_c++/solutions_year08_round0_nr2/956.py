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
int N ,NA, NB,T;
struct node
{
       int Time,sta;
};
int cnt_A,cnt_B;
bool cmp ( const node &a ,const node &b)
{
     if ( a.Time < b.Time ) return true;
     if ( a.Time > b.Time ) return false;
     if ( a.sta %2 == 0 ) return true ;
     else return false;
}
main ()
{
     cin >> N;
     int kase = 1;
     while ( N-- )
     {
           cin  >> T >> NA >>NB;
           string tmp ,a ,b ,c;
           int i,j,k;
           node state ;
           vector < node > sche;
           cnt_A = cnt_B =0;
           queue <int > Q_A,Q_B;
           for ( i = 0; i < NA ;i++ )
           {
               cin >> tmp;
               j = ( ( tmp[0] - '0' )*10 + (tmp [1] - '0' ) )*60 + (tmp [3] - '0' )*10 +( tmp [4] - '0' );
               state.Time = j ;
               state.sta = 1;
               sche.push_back ( state );
               cin >> tmp;
               j = ( ( tmp[0] - '0' )*10 + (tmp [1] - '0' ) )*60 + (tmp [3] - '0' )*10 +( tmp [4] - '0' ) +T;
               state.Time = j ;
               state.sta = 2;
               sche.push_back ( state );
           }
           for ( i = 0; i < NB ;i++ )
           {
               cin >> tmp;
               j = ( ( tmp[0] - '0' )*10 + (tmp [1] - '0' ) )*60 + (tmp [3] - '0' )*10 +( tmp [4] - '0' );
               state.Time = j ;
               state.sta = 3;
               sche.push_back ( state );
               cin >> tmp;
               j = ( ( tmp[0] - '0' )*10 + (tmp [1] - '0' ) )*60 + (tmp [3] - '0' )*10 +( tmp [4] - '0' )+T;
               state.Time = j ;
               state.sta = 0;
                sche.push_back ( state );
           }
           sort ( sche.begin(),sche.end() ,cmp);
           //for ( i = 0 ;i < sche.size() ; i++ ) cout << sche [i].Time <<" " <<sche [i].sta <<"\n";
           queue < node > Q;
           for ( i = 0; i< sche.size() ;i++) Q.push ( sche [i] );
           while ( !Q.empty () )
           {
                 state = Q.front();
                 Q.pop();
                 if ( state.sta == 0 )
                 Q_A.push ( 1 );
                 if ( state.sta == 2 ) 
                 Q_B.push ( 1);
                 if ( state.sta == 1 )
                 if ( Q_A.empty () ) cnt_A++;
                 else Q_A.pop();
                 if ( state.sta ==3 ) 
                 if ( Q_B.empty() ) cnt_B++;
                 else Q_B.pop();
           }
           cout << "Case #"<<kase++<<": ";
           cout << cnt_A <<" "<<cnt_B<<"\n";
     }
}

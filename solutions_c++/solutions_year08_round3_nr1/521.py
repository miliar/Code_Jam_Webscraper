#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <cmath>
#include <list>
#include <set>

#define FOR( i, n ) for( unsigned long long (i) = 0; (i) < (n); ++(i) ) 
#define FORR( i, n, m ) for(unsigned long long (i) = (n); (i) <= (m); ++(i) ) 
#define FOREACH(_it,_l) for(__typeof((_l).begin()) _it=((_l).begin());(_it)!=(_l).end();(_it)++) 
#define ALL(x) (x).begin(),(x).end() 
#define eatDel( ifs, del ) while( ifs.peek() == del ) ifs.ignore(); 
#define isMaped( m, element ) ((m).find( (element) ) != (m).end()) 

using namespace std;

int main()
{
    
    ifstream ifs( "A-large.in" );
    ofstream ofs( "a.out" );
    
    unsigned long long caseNum;
    ifs>>caseNum;
    cout<<caseNum<<endl;
    for( unsigned long long case_num = 1; case_num <= caseNum; ++case_num )
    {
         unsigned long long P, K, L;
         ifs>>P>>K>>L;
         vector<unsigned long long> freq;
         map<unsigned long long,unsigned long long> keyz;
         FOR( i, L )
         {
              unsigned long long f;
              ifs>>f;
              freq.push_back( f );
          }
          
          FOREACH( el, freq ) cout<<*el<<" ";
          cout<<endl;
          
          FOR( i, K ) keyz[i] = 0;
          if( K * P < L  ) ofs<<"Case #"<<case_num<<": IMPOSSIBLE"<<endl;
          
          sort( ALL( freq ) );
          reverse( ALL( freq ) );
          unsigned long long ret = 0;
          unsigned long long deep = 1;
          unsigned long long key = 0;
          bool unsolvable = false;
          while( deep <= P && key < L )
          {
                 FOR( i, K )
                 {
                      /*
                      if( key >=  L + 1 )
                      {
                          unsolvable = true;
                          break;
                      }
                      */
                      cout<<deep<<" "<<ret<<endl;
                      ret += deep * freq[key];
                      key++;
                      if( key >= L ) break;
                  }
                  deep++;
          }
          if( !unsolvable ) ofs<<"Case #"<<case_num<<": "<<ret<<endl;
          else ofs<<"Case #"<<case_num<<": IMPOSSIBLE"<<endl;
          
          cout<<"==============================="<<endl;
          
     }
     system( "pause" );
}

#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<cstdio>
using namespace std;
int n , q; vector<int> query;
map<string, int> m;
int dp [105][1005];
int doit( int cur, int pos ) 
{
 if( pos == q ) return 0;
 if( cur == query[pos] ) return -2;
 int &ref = dp[cur][pos] ; if( ref != -1 ) return ref;
 int ret = q;
     for( int i =0 ; i<n ; i++) 
      {
          int rec = doit( i, pos + 1 ) ; 
          if( rec == -2 ) continue;
          rec +=(cur != i);    
          ret = min ( ret, rec );
      }
 return ref=ret;
}
int main ()
{
    int tc;
    cin>>tc;
    for( int cse = 1; cse <=tc; cse ++)
    {
          m.clear();
          query.resize(0);
          memset( dp, -1, sizeof dp);
          scanf( "%d\n", &n);
          string s;
          for( int i =0 ; i<n ;i++) 
          {
           getline(cin, s);       
           m[s] = i;
          // cout<<s<<" "<<i<<endl;
          }
          
          scanf( "%d\n", &q);
          for( int i =0 ; i<q ;i++) 
          {
           getline(cin, s);       
           query.push_back( m[s] );
           //cout<<query.back()<<endl;
          }
          int ret = q;
          for( int i =0 ; i<n ; i++)
          {
               int rec = doit( i, 0) ; if( rec == -2 ) continue;
               ret = min ( ret, rec );
          }
          printf("Case #%d: %d\n", cse, ret);
    }
    return 0;
}

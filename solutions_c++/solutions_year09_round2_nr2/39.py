#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<set>
using namespace std ;
typedef long long LL ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)  
main()
{
      ios_base::sync_with_stdio(0) ;
      int C, i ;
      cin >> C ;
      for(int test=1 ; test<=C ; test++)
      {
            cout << "Case #" << test << ":" << " " ;
            vector<int> t ;
            string s ;
            cin >> s ;
            REP(i,s.size()) t.push_back(s[i]-'0') ;
            if(next_permutation(t.begin(), t.end())) {
                  REP(i,t.size()) cout << t[i] ;
                  cout << endl ;
            }
            else
            {
                  int zera = 0 ;
                  for(i=0 ; i<t.size() ; )
                        if(t[i]==0) {
                              zera++ ;
                              swap(t[i],t.back()) ;
                              t.pop_back() ;
                        }
                        else i++ ;
                  sort(ALL(t)) ;
                  cout << t[0] ;
                  zera++ ;
                  while(zera--) cout << 0 ;
                  for(i=1 ; i<t.size() ; i++) cout << t[i] ;
                  cout << endl ;
            }
      }

      
}

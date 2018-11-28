#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std ;
typedef long long LL ;
#define REP(i,n) for(i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)  
main()
{
      ios_base::sync_with_stdio(0) ;
      int L, D, N, i, j ;
      cin >> L >> D >> N ;
      vector<string> t ;
      string s ;
      while(D--)
      {
            cin >> s ;
            t.push_back(s) ;
      }
      for(int test=1 ; test <= N ; test++)
      {
            cin >> s ;
            vector<set<char> > zbior ;
            for(i=0 ; i<s.size() ; i++)
            {
                  set<char> z ;
                  if(s[i]!= '(') z.insert(s[i]) ;
                  else
                  {
                        i++ ;
                        while(s[i] != ')') {
                              z.insert(s[i]) ;
                              i++ ;
                        }
                  }
                  zbior.push_back(z) ;
            }
            long long odp = 0 ;
            FOREACH(q,t)
            {
                  bool jest = true ;
                  for(i=0 ; i<L ; i++)
                        if(zbior[i].find((*q)[i])==zbior[i].end()) jest = false ;
                  if(jest) odp++ ;
            }
            cout << "Case #" << test << ": " << odp << endl ;
      }
}

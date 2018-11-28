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
struct tree
{
      double prob ;
      string name ;
      tree* l, *r ;
} ;
tree* wczytaj()
{
    //  cout << "(" ;
      tree* a = new tree() ;
      char x ;
      cin >> x ; // (
      cin >> a->prob ;
    //  cout << "wczytalem " << a->prob << " " ;
      cin >> x ;
      if(x!=')')
      {
            cin.putback(x) ;
            cin >> a->name ;
       //     cout << a->name << " " ;
            a->l = wczytaj() ;
            a->r = wczytaj() ;
            cin >> x ; // )
      }
   //   cout << ") " ;
      return a ;
}
main()
{
      ios_base::sync_with_stdio(0) ;
      int C ;
      tree* root ;
      cin >> C ;
      for(int test=1 ; test<=C ; test++)
      {
            cout << "Case #" << test << ":" << endl ;
            int niepotrzebne ; cin >> niepotrzebne ;
            root = wczytaj() ;
            int n, m ;
            cin >> n ;
            while(n--)
            {
                  string nazwa ;
                  cin >> nazwa >> m ;
                  set<string> cechy ;
                  while(m--) {
                        cin >> nazwa ;
                        cechy.insert(nazwa) ;
                  }
                  tree* wsk = root ;
                  double p=wsk->prob ;
                  while(wsk->name != "")
                  {
                        if(cechy.find(wsk->name)!=cechy.end()) wsk = wsk->l ;
                        else wsk = wsk->r ;
                        p *= wsk->prob ;
                  }
                  cout.setf(ios::fixed) ;
                  cout.precision(7) ;
                  cout << p << endl ;
            }
      }
}

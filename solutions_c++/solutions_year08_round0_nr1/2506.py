#include <iostream>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
typedef long long LL;


 map<string,int> wiad;
 string pom;

int main(){
   int n,s,q;
    cin >> n;
    REP(i,n) {
      int wynik = 0;
      cin >> s;
      string tab[s];
      char a;
      cin.get(a);
      REP(j,s) {
        getline(cin, tab[j], '\n');
        wiad[tab[j]] = 0;
      }

      cin >> q;
      string tab2[q];
      int ile = 0;


      cin.get(a);
      ile = s;
      REP(j,q) {

        getline(cin, tab2[j], '\n');
        map<string,int>::iterator iter = wiad.find(tab2[j]);
        if( iter != wiad.end() ) {
          if (wiad[tab2[j]] == 0) ile--;
          if (ile == 0) {
             ile = s-1;
             wynik++;
             map<string,int>::iterator iter3;
             for( iter3 = wiad.begin(); iter3 != wiad.end(); iter3++ ) {
                 (*iter3).second = 0 ;
             }
          }

        }
                  wiad[tab2[j]] += 1;
      }
       cout << "Case #" << i+1 << ": " << wynik << "\n";
      }
  return 0;
}

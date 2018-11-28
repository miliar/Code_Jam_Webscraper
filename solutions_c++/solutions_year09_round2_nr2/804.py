#include <iostream>
#include <algorithm>
using namespace std;

#define FCO(i,a,b) for(int i=a,_b=b;i<_b;++i)
#define FOR(i,n) FCO(i,0,n)
#define ALL(s) s.begin(),s.end()
#define SZ(s) signed(s.size())

int main() {
  int T; scanf("%d", &T);
  FOR(casenum,T) {
    string s; cin>>s; fprintf(stderr, "Got #%s#\n", s.c_str());
    bool d = next_permutation(ALL(s));
    cerr<<s<<" "<<boolalpha<<d<<endl;

    if(!d) {
      sort(ALL(s));
      FOR(i,SZ(s)) {
        if(s[i]!='0') {
          swap(s[0],s[i]);
          break;
        }
      }
      s.insert(1, 1, '0');
      cerr<<s<<endl;
      char c = *min_element(ALL(s));
    }
    printf("Case #%d: %s\n", casenum+1, s.c_str());
  }
  return 0;
}

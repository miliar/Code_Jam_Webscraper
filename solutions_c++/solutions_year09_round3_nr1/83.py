#include<iostream>
#include<set>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int tno = 0; tno < T; tno++){
    printf("Case #%d: ", tno + 1);
    string str;
    cin >> str;

    set<char> st;
    for(int i = 0; i < str.size(); i++){
      st.insert( str[i] );
    }
    int base = st.size();

    if( base == 1 ) base = 2;
    
    int table[256];
    int use[256];
    memset(table, -1, sizeof(table));
    memset(use, 0, sizeof(use));

    table[str[0]] = 1;
    use[1] = 1;

    for(int i = 0; i < str.size(); i++){
      if( table[ str[i] ] == -1 ) {
        for(int j = 0; j < 256; j++){
          if( use[j] == 0 ) {
            table[str[i]] = j;
            use[j] = 1;
            break;
          }
        }
      }
    }

    long long ans = 0;
    for(int i = 0; i < str.size(); i++) {
      ans = ans * base + table[str[i]];
    }
    cout << ans << endl;
  }
}

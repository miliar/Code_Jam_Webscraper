#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>

using namespace std;

int main(){
  int casos;
  cin >> casos;
  for (int caso = 1; caso <= casos; caso++) {
    char combine[27][27];
    bool opposed[27][27];
    memset(combine,0,sizeof(combine));
    memset(opposed,0,sizeof(opposed));
    
    string invoke;
    int quan;
    cin >> quan;
    for (int i = 0; i < quan; i++) {
      string tmp; cin >> tmp;
      combine[ tmp[0] - 'A' ][ tmp[1] - 'A' ] = tmp[2]-'A';
      combine[ tmp[1] - 'A' ][ tmp[0] - 'A' ] = tmp[2]-'A';
    }

    cin >> quan;
    for (int i = 0; i < quan; i++) {
      string tmp; cin >> tmp;
      opposed[ tmp[0] - 'A' ][ tmp[1] - 'A' ] = 1;
      opposed[ tmp[1] - 'A' ][ tmp[0] - 'A' ] = 1;
    }
    
    cin >> quan >> invoke;

    vector<int> ans;

    for (int i = 0; i < invoke.size() ; i++) {
      char c = invoke[i] - 'A';
      if ( ans.empty() ) {
        ans.push_back( c );
        continue;
      }
      
      int l = ans[ans.size() - 1];
      if ( combine[l][c] ) {
        c = combine[l][c];
        ans.resize(ans.size() - 1);
        ans.push_back( c );
        continue;
      }

      bool add = true;
      for (int i = 0; i < ans.size() ; i++) {
        if ( opposed[ans[i]][c] ) {
          ans.clear();
          add = false;
          break;
        }
      }
      if ( add )
        ans.push_back( c );

    }

    cout << "Case #" << caso << ": [";
    for (int i = 0; i < ans.size() - 1 && !ans.empty(); i++) {
      cout << (char)(ans[i]+'A') << ", ";
    }
    if ( !ans.empty() ) {
      cout << (char)(ans[ans.size() - 1]+'A');
    }
    cout << "]" << endl;

  }
  return 0;
}



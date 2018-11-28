#include <iostream>

using namespace std;

int
main() {
  int n;
  
  cin >> n;
  
  for(int i = 0; i < n; i++) {
    int n_combine;
    int n_oppose;
    int l;
    char output[100];
    char input[100];
    int e = 0;
    char combine[26][26];
    char oppose[26][26];
    
    for(int j = 0; j < 26; j++)  {
      for(int k = 0; k < 26; k++) {
        combine[k][j] = '\0';
        oppose[k][j] = 0;
      }
    }
    
    cin >> n_combine;
    for(int j = 0; j < n_combine; j++) {
      char c[4];
      cin >> c;
      combine[c[0]-'A'][c[1]-'A'] = c[2];
      combine[c[1]-'A'][c[0]-'A'] = c[2];
    }
    
    cin >> n_oppose;
    for(int j = 0; j < n_oppose; j++) {
      char c[3];
      cin >> c;
      oppose[c[0]-'A'][c[1]-'A'] = 1;
      oppose[c[1]-'A'][c[0]-'A'] = 1 ;
    }
    
    cin >> l >> input;    
    for(int j = 0; j < l; j++) {
      if(e == 0) {
        output[e] = input[j];
        e++;
      } else {
        char c = combine[output[e-1]-'A'][input[j]-'A'];
        
        if(c != '\0') {
          e--;
          output[e] = c;
        } else {
          output[e] = input[j];
        }
        
        e++;
        
        for(int k = e-1; (k >= 0) && (e != 0); k--) {
          if(oppose[output[e-1]-'A'][output[k]-'A'] == 1) {
            e = 0;
          }
        }
      }
    }
    
    cout << "Case #" << (i+1) << ": [";
    if(e > 0) {
      cout << output[0];
      for(int j = 1; j < e; j++) {
        cout << ", " << output[j];     
      }
    }
    cout << "]" << endl;
  }    
}

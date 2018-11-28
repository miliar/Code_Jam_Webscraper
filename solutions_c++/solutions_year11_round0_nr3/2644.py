#include <iostream>
#include <list>

using namespace std;

int
main() {
  int N;
  
  cin >> N;
  
  for(int i = 0; i < N; i++) {
    int n;
    list<int> candy;
    
    cin >> n;
    
    for(int j = 0; j < n; j++) {
      int c;
      cin >> c;
      candy.push_back(c);
    }
    
    candy.sort();
    
    int patrick = 0;
    int sean = 0;
    int sean_as_patrick = 0;
    
    for(list<int>::iterator j = candy.begin(); j != candy.end(); j++) {
      sean += (*j);
      sean_as_patrick ^= (*j);
    }
    
    list<int>::iterator s = candy.begin();
    if(s != candy.end()) {
      int c = (*s);
      // give patrick one candy
      sean -= c;
      sean_as_patrick ^= c;
      patrick ^= c;
      s++;
      
      // keep giving patrick least wanted candy untill hes happy
      while((sean_as_patrick != patrick) && (s != candy.end())) {
        c = (*s);
        sean -= c;
        sean_as_patrick ^= c;
        patrick ^= c;
        s++;
      }
    }
    
    cout << "Case #" << (i+1) << ": ";
    if(s == candy.end()) {
      cout << "NO";
    } else {
      cout <<  sean;
    }
    cout << endl;
  }
  
  return 0;
}

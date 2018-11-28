/*! if g++ -g qa1.cpp -o qa1.out; then ./qa1.out < qa1.test; fi
 */


#include <string>
#include <map>
#include <iostream>



using namespace std;


int main(int argc, char *argv[]){
  string key = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string val = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

  map<char, char> m;
  for(size_t i = 0; i < key.size(); ++i){
    m[key[i]] = val[i];
  }
  m['q'] = 'z';
  m['z'] = 'q';

  int T;
  string G;
  cin >> T;
  getline(cin, G);
  for(size_t i = 0; i < T; ++i){
    getline(cin, G);
    cout << "Case #" << i+1 << ": ";
    for(size_t j = 0; j < G.size(); ++j){
      cout << m[G[j]];
    }
    cout << endl;
  }
  
  return 0;
}

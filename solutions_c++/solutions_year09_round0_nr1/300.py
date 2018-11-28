// 2009/09/03 Naoyuki Hirayama

#include <iostream>
#include <string>
#include <vector>

int main() {
  int L, D, N;
  std::cin >> L >> D >> N;

  std::vector<std::string>  dic;
  for (int i = 0 ; i < D ; i++ ) {
    std::string s;
    std::cin >> s;
    dic.push_back(s);
  }
  for (int i = 0 ; i < N; i++ ) {
    std::string s;
    std::cin >> s;

    int match = 0;
    for( size_t j = 0 ; j < dic.size(); j++ ) {
      const char* p = s.c_str();

      const std::string& t = dic[j];
      const char* q = t.c_str();

      int c;
      while( c = *p++ ){
        bool ok = false;
        if( c == '(' ) {
          while( ( c=*p++ ) != ')' ){
            if(*q == c) {
              ok = true;
            }
          }
        } else if(*q == c) {
          ok = true;
        } 
        if(!ok) { goto next; }
        q++;
      }
      match++;
     next:;
    }
    std::cout << "Case #" << (i+1) << ": " << match << std::endl;
  }
}

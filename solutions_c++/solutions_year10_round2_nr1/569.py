#include <cstdio>
#include <string>
#include <vector>
#include <set>

using namespace std;

int main () {
  int T, N, M;
  scanf ("%d", &T);
  for(int i = 1; i <= T; i++) {
    set<string> directories = set<string> ();
    int num = 0;
    scanf ("%d%d", &N, &M);
    for (int j = 0; j < N; j++) {
      char s[200];
      scanf ("%s", s);
      string st;
      st.push_back('/');
      for (int k = 1; s[k] != '\0'; k++) {
        if (s[k] == '/') {
          if (directories.find(st) == directories.end()) {
            directories.insert(st);
            //printf ("N: %s\n", st.c_str());
          }
        }
        st.push_back(s[k]);
      }
      if (directories.find(st) == directories.end()) {
        directories.insert(st);
       // printf ("N: %s\n", st.c_str());
      }
    }
    for (int j = 0; j < M; j++) {
      char s[200];
      scanf ("%s", s);
      string st;
      st.push_back('/');
      for (int k = 1; s[k] != '\0'; k++) {
        if (s[k] == '/') {
          if (directories.find(st) == directories.end()) {
            directories.insert(st);
            num++;
            //printf ("M: %s\n", st.c_str());
          }
        }
        st.push_back(s[k]);
      }
      if (directories.find(st) == directories.end()) {
        directories.insert(st);
        num++;
        //printf ("M: %s\n", st.c_str());
      }
    }
    printf ("Case #%d: %d\n", i, num);
  }
  return 0;
}

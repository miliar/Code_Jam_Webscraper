#include <string>
#include <cstdio>
#include <set>
using namespace std;

int main() {
  char buff[10000];
  fgets(buff, 10000, stdin);
  int N,S,Q;
  sscanf(buff, "%d", &N);
  for(int n=0;n<N;++n) {
    fgets(buff, 10000, stdin);
    sscanf(buff, "%d", &S);
    set<string> eng;
    for(int s=0;s<S;++s) {
      fgets(buff, 10000, stdin);
      eng.insert(string(buff));
    }
    fgets(buff, 10000, stdin);
    sscanf(buff, "%d", &Q);
    set<string> eng2=eng;
    int nr=0;
    for(int q=0;q<Q;++q) {
      fgets(buff, 10000, stdin);
      string str(buff);
      eng2.erase(str);
      if(eng2.size()==0) {
	++nr;
	eng2=eng;
	eng2.erase(str);
      }
    }
    printf("Case #%d: %d\n", n+1, nr);
  }
}

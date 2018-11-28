#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <list>

using namespace std;

int nt, nt0;
int n, l, h;

typedef list<int> li;

int main() {
  scanf(" %d", &nt0);
  for(nt = 1 ; nt <= nt0 ; nt++) {
    scanf(" %d %d %d", &n, &l, &h);

    li lista;
    for(int i=l ; i<=h ; i++)
      lista.push_back(i);

    for(int i=0 ; i<n ; i++) {
      int f;
      scanf(" %d", &f);
      for(li::iterator it = lista.begin() ; it != lista.end() ; it++)
	if(f % (*it) != 0 && (*it) % f != 0)
	  lista.erase(it);
    }

    printf("Case #%d: ", nt);
    if(lista.empty()) puts("NO");
    else printf("%d\n", lista.front());
  }
  return 0;
}

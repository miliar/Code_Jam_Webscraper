#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cctype>

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

char mapping[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};


int main (int argc, char *argv[]) {
  int n;
  char buffer[150];

  scanf ("%d\n",&n);
  for (int i = 0; i < n; i++) {
    printf ("Case #%d: ",i+1);
    fgets(buffer,sizeof(buffer),stdin);
    for (char *p = buffer; *p; p++) {
      char c = *p;
      if (isalpha(*p) && isupper(*p)) {
        c = mapping[*p-'A'];
      } else if (isalpha(*p) && islower(*p)) {
        c = mapping[*p-'a'];
      }
      printf ("%c",c);
    }
  }

  return 0;
}

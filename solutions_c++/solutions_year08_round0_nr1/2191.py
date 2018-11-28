#include <iostream>
#include <map>
#include <cstdio>

using namespace std;

int main () {
  int t, s, q, i;
  map <string, int> m1;
  map <string, int> :: iterator it;
  char str[1000];
  string engine;
  int sum, ans;
  int j;
  j = 1;
  scanf("%d\n", &t);
  while(t --) {
    scanf("%d\n", &s);
    m1.clear();
    sum = s;
    ans = 0;
    for (i = 0; i < s; i ++) {
      gets(str);
      engine = string(str);
      m1[engine] = 1;
    }

    scanf("%d\n", &q);
    for (i = 0; i < q; i ++) {
      gets(str);
      engine = string(str);
      if (m1[str] == 1) {
	if (sum != 1) {
	  m1[str] = 0;
	  sum --;	
	}
	else {
	  sum = s-1;
	  it = m1.begin();
	  while (it != m1.end()) {
	    it -> second = 1 - (it -> second);
	    it ++;
	  }
	  ans ++;
	}
      }
    }
    printf ("Case #%d: %d\n", j, ans);
    j ++;
  }
  return 0;
}

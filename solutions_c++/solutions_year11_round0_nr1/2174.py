#include<cstdio>
#include<algorithm>
#include<cmath>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);
  for(int C=1; C<=T; ++C) {
    int n;
    scanf("%d", &n);
    int o = 1, b = 1, to = 0, tb = 0, tm = 0;
    while(n--) {
      char s[4];
      int p;
      scanf("%s%d", s, &p);
      if(s[0] == 'O') {
	tm += max(0, abs(o-p) - abs(tm-to));
	o = p;
	to = ++tm;
      } else {
	tm += max(0, abs(b-p) - abs(tm-tb));
	b = p;
	tb = ++tm;
      }
    }
    printf("Case #%d: %d\n", C, tm);
  }
  return 0;
}

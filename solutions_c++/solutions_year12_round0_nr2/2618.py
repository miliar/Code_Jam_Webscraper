#include <cstdio>
#include <algorithm>

using namespace std;


int main()
{
  int casos;
  scanf(" %d", &casos);
  for(int h = 1; h <= casos; h++){
    int n, s, p;
    scanf(" %d %d %d", &n, &s, &p);

    int c1 = 0, c2 = 0;
    for(int i = 0; i < n; i++){
      int x;
      scanf(" %d", &x);
      if(x == 0){
	if(p == 0) c1++;
	continue;
      }
      else if(x == 1){
	if(p <= 1) c1++;
	continue;
      }
      else if(x == 2){
	if(p <= 1) c1++;
	else if(p == 1) c2++;
	continue;
      }
      switch(x % 3){
      case 0:
	if(p <= x/3) c1++;
	else if(p <= x/3 + 1) c2++;
	break;
      case 1:
	if(p <= x/3 + 1) c1++;
	break;
      case 2:
	if(p <= x/3 + 1) c1++;
	else if(p <= x/3 + 2) c2++;
	break;
      }
    }

    int resp = c1 + min(s, c2);
    printf("Case #%d: %d\n", h, resp);
  }
  return 0;
}

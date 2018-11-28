#include <cstdio>
#include <cstdlib>

using namespace std;

int main(){
  int t, n, k;
  bool on;

  scanf("%d", &t);
  for (int ca = 1; ca <= t; ca++){
    scanf("%d", &n);
    scanf("%d", &k);
    on = true;
    for (int i = 0; i < n; i++){
      if (k%2 == 0){
	on = false;
	break;
      }
      k /= 2;
    }
    printf("Case #%d: ", ca);
    if (on)
      printf("ON\n");
    else
      printf("OFF\n");
  }
}

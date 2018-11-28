#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int main(){
  int c, n, k, b, t, x[55], v[55];

  scanf("%d", &c);
  for (int caso = 1; caso <= c; caso ++){
    scanf("%d %d %d %d", &n, &k, &b, &t);
    for (int i = 0; i < n; i++)
      scanf("%d", &x[i]);
    for (int i = 0; i < n; i++)
      scanf("%d", &v[i]);

    int chega[55];
    int total = 0;
    for (int i = 0; i < n; i++){
      if (abs(x[i]-b) <= v[i]*t){
	chega[i] = 1;
	total++;
	//printf("s");
      }
      else{
	chega[i] = 0;
	//printf("n");
      }
      
    }

    if (total < k){
      printf("Case #%d: IMPOSSIBLE\n", caso);
      continue;
    }

    int fim = 0;
    int troca = 0;
    int invs = 0;
    for (int i = n-1; i >= 0 && fim < k; i--){
      if (chega[i] == 0){
	invs++;
      }
      else{
	troca += invs;
	fim++;
      }
    }
    printf("Case #%d: %d\n", caso, troca);
  }
  
  return 0;
}

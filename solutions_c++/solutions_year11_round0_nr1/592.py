#include <cstdio>
#include <algorithm>

int main(){
  char r[111];
  int b[111];
  int n, cas;

  scanf("%d", &cas);
  for (int ka = 1; ka <= cas; ka++){
    scanf("%d", &n);
    for (int x = 0; x < n; x++){
      scanf(" %c %d", &r[x], &b[x]);
    }

    int t = 0;
    int po = 1;
    int pb = 1;
    int exB = 0, exO = 0;
    for (int x = 0; x < n; x++){
      if (r[x] == 'O'){
	int cost = abs(b[x]-po);
	if (cost-exO > 0){
	  t += cost-exO;
	  exB += cost-exO;
	}
	t++;
	exB++;
	exO = 0;
	po = b[x];
      }
      else{
	int cost = abs(b[x]-pb);
	if (cost-exB > 0){
	  t += cost-exB;
	  exO += cost-exB;
	}
	t++;
	exO++;
	exB = 0;
	pb = b[x];
      }
    }
    printf("Case #%d: %d\n", ka, t);
  }

  return 0;
}

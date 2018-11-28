#include <cstdio>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <set>
#include <map>
using namespace std;

typedef struct time{
  int orig;
  int dest;
} * Time;

struct time ab[131], ba[131];
Time abo[131], abd[131], bao[131], bad[131];

int compo(const void * x, const void * y){
  Time a = *(Time *)x;
  Time b = *(Time *)y;

  return a->orig - b->orig;
}

int compd(const void * x, const void * y){
  Time a = *(Time *)x;
  Time b = *(Time *)y;

  return a->dest - b->dest;
}

int main(){
  int n, t, na, nb, k, i, ha, ma, hb, mb, trem, j;

  scanf("%d", &n);
  for (k = 1; k <= n; k++){
    scanf("%d", &t);
    scanf("%d %d", &na, &nb);
    for (i = 0; i < na; i++){
      scanf("%d:%d %d:%d", &ha, &ma, &hb, &mb);
      ab[i].orig = ma + ha*60;
      ab[i].dest = mb + hb*60;
      abo[i] = abd[i] = &ab[i];
    }
    for (i = 0; i < nb; i++){
      scanf("%d:%d %d:%d", &hb, &mb, &ha, &ma);
      ba[i].orig = mb + hb*60;
      ba[i].dest = ma + ha*60;
      bao[i] = bad[i] = &ba[i];
    }
    
    qsort(abo, na, sizeof(Time), compo);
    qsort(abd, na, sizeof(Time), compd);
    qsort(bao, nb, sizeof(Time), compo);
    qsort(bad, nb, sizeof(Time), compd);

    /*    printf("abo\n");
    for (i = 0; i < na; i++)
    printf("%d %d\n", abo[i]->orig, abo[i]->dest);
      printf("\nabd\n");
    for (i = 0; i < na; i++)
    printf("%d %d\n", abd[i]->orig, abd[i]->dest);
      printf("\nbao\n");
    for (i = 0; i < nb; i++)
    printf("%d %d\n", bao[i]->orig, bao[i]->dest);
    printf("\nbad\n");
    for (i = 0; i < nb; i++)
    printf("%d %d\n", bad[i]->orig, bad[i]->dest);
      printf("\n");*/

    i = j = 0;
    trem = 0;
    while (i < na && j < nb){
      if (bad[j]->dest + t <=  abo[i]->orig)
	j++;
      else
	trem++;
      i++;
    }
    if (i < na) trem += na-i;
    printf("Case #%d: %d ", k, trem);
    i = j = 0;
    trem = 0;
    while (i < na && j < nb){
      //      printf("%d: %d-%d x ", j, bao[j]->orig, bao[i]->dest);
      //      printf("%d: %d-%d\n", i, abd[i]->orig, abd[i]->dest);
      if (abd[i]->dest + t <=  bao[j]->orig)
	i++;
      else
	trem++;
      //      printf("Trens = %d\n");
      j++;
    }
    if (j < nb) trem += nb-j;
    printf("%d\n", trem);
  }
  
  return 0;
}

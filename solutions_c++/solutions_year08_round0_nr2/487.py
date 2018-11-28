#include <stdio.h>
#include <string.h>

#define min(a,b) ((a)<(b)?(a):(b))

int main()
{
  int lv[48*60][2];
  int ar[48*60][2];
  int a,b,sa,sb,na,nb;
  int n,cs=1,i,j,t,k,s;

  scanf("%d", &n);
  for (;cs<=n;cs++)
  {
    sa = sb = a = b = 0;
    memset(lv, 0, sizeof(lv));
    memset(ar, 0, sizeof(ar));

    scanf("%d", &t);
    scanf("%d %d", &na, &nb);
    for (i=0;i<na;i++)
    {
      scanf("%d:%d", &j, &k);
      lv[j*60+k][0]++;
      scanf("%d:%d", &j, &k);
      ar[j*60+k+t][1]++;
    }

    for (i=0;i<nb;i++)
    {
      scanf("%d:%d", &j, &k);
      lv[j*60+k][1]++;
      scanf("%d:%d", &j, &k);
      ar[j*60+k+t][0]++;
    }

    for (i=0;i<24*60;i++)
    {
      a += ar[i][0];
      b += ar[i][1];

      s = min(a, lv[i][0]);
      a -= s;
      lv[i][0] -= s;
      sa += lv[i][0];

      s = min(b, lv[i][1]);
      b -= s;
      lv[i][1] -= s;
      sb += lv[i][1];
    }
    
    printf("Case #%d: %d %d\n", cs, sa, sb);
  }

  return 0;
}

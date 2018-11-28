#include <cstdio>

#define MAX_N 10000

int n;
int d[MAX_N];
int le[MAX_N];
int rl[MAX_N];
int D;

void read_input()
{
  scanf("%d",&n);
  for(int i=0; i<n; i++)
    scanf("%d %d",&d[i],&le[i]);
  scanf("%d",&D);
}

bool process()
{
  int r = 0;

  for(int i=0; i<n; i++)
    rl[i] = -1;
  
  rl[0] = le[0];
  if(rl[0]>d[0])
    rl[0] = d[0];
  r=1;
  for(int l=0; l<n; l++) {
    if(rl[l]==-1)
      break;
    while((r<n) && (d[l]+rl[l] >= d[r])) {
      rl[r] = (le[r] < d[r] - d[l]) ? le[r] : d[r]-d[l];
      //printf("%d,%d\n", r, rl[r]);
      r++;
    }
  }
  if(rl[0]+d[0]>=D)
    return true;
  if(rl[n-1]==-1)
    return false;
  else
    return d[n-1] + rl[n-1] >= D;
}

main()
{
  int t;
  scanf("%d",&t);
  for(int tt=0; tt<t; tt++) {
    read_input();
    //printf("%d\n",n);
    if(process())
      printf("Case #%d: YES\n",tt+1);
    else
      printf("Case #%d: NO\n",tt+1);
  }
}

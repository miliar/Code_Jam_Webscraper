#include <cstdio>
#include <cstdlib>

#define MIN_X ((-100000 - 500)*2)
#define MAX_X ((100000 + 500)*2)
#define RANGE (MAX_X - MIN_X + 10)
#define MAX_C 20

int cost[MAX_C+1][RANGE];
int cost2[MAX_C+1][RANGE];
int d;
int c;
int p[MAX_C];
int v[MAX_C];
int tv;

void read_input()
{
  scanf("%d %d",&c,&d);
  d *= 2;
  tv = 0;
  for(int i=0; i<c; i++) {
    scanf("%d %d",&p[i],&v[i]);
    p[i] *= 2;
    tv += v[i];
  }
}

int solve()
{
  int min_range = p[0]-d*(tv-1);
  int max_range = p[c-1]+d*(tv-1);

  for(int i=0; i<c; i++)
    p[i] -= min_range;
  max_range -= min_range;
  min_range = 0;

  for(int j=0; j<=c; j++)
    for(int i=min_range; i<=max_range; i++) {
      cost[j][i] = 0;
      cost2[j][i] = 0;
    }
  //printf("max-range = %d (%d)\n",max_range,RANGE);

  int pleft = 0;
  int ibest = 0;

  for(int i=c-1; i>=0; i--) {
    int cmaxleft = max_range - (pleft-1)*d;
    int cmax = max_range - pleft*d - ((v[i]-1)*d);
    for(int cp=min_range; cp<=cmax; cp++) {
      int cc = abs(p[i] - cp);
      int cc2 = abs(p[i] - (cp + (v[i]-1)*d));
      if(cc2 > cc)
	cc = cc2;
      
      int lmin = cost2[i+1][cp + v[i]*d];

      /*for(int l=cp+v[i]*d+1; l<=cmaxleft; l++)
	if(cost[i+1][l] < lmin)
	  lmin = cost[i+1][l];
      */

      if(lmin > cc)
	cost[i][cp] = lmin;
      else
	cost[i][cp] = cc;
    
      //printf("%d,%d = %d\n",i,cp,cost[i][cp]);
  
      if(cp==min_range)
	ibest = cost[i][cp];
      else if(cost[i][cp] < ibest) {
	ibest = cost[i][cp];
      }
    }

    for(int cp=cmax; cp >= min_range; cp--) {
      if(cp==cmax)
	cost2[i][cp] = cost[i][cp];
      else {
	if(cost[i][cp] < cost2[i][cp+1])
	  cost2[i][cp] = cost[i][cp];
	else
	  cost2[i][cp] = cost2[i][cp+1];
      }
    }
    pleft += v[i];
  } 
  return ibest;
}

main()
{
  int tt;
  scanf("%d",&tt);
  for(int t=0; t<tt; t++) {
    read_input();
    int ans = solve();
    printf("Case #%d: %f\n",t+1, (float)ans/2.0);
  }
}



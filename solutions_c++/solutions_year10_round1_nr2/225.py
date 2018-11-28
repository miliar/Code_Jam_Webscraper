#include <cstdio>
#include <cstdlib>

#define MAX_VAL 255
#define MAX_N   100

int c[MAX_N+1][MAX_VAL + 1];
int a[MAX_N+1];
int D, I, M, n;

void read_input()
{
  scanf("%d %d %d %d",&D,&I,&M,&n);
  for(int i=1; i<=n; i++)
    scanf("%d",&a[i]);
}

void initialize()
{
  for(int y=0; y <= MAX_VAL; y++)
    c[0][y] = 0;
}

void inline update_min(int& cand, int newmin)
{
  if((cand == -1) || (cand > newmin))
    cand = newmin;
}

void compute(int i)
{
  for(int y=0; y <= MAX_VAL; y++) {
    // ----- delete
    c[i][y] = c[i-1][y] + D;

    // ----- change & insert
    int update_cost = abs(a[i] - y);
    int candidate = -1;
    for(int oy = 0; oy <= MAX_VAL; oy++) {
      int diff = abs(oy - y);
      if(diff <= M)
	update_min(candidate, c[i-1][oy]);
      else {
	if(M!=0) 
	  // need to insert something
	  update_min(candidate, c[i-1][oy] + ((diff + M - 1)/M - 1)*I);
      }
    }
    
    if((candidate!=-1) && (candidate + update_cost < c[i][y]))
      c[i][y] = candidate + update_cost;
  }

  /*
  for(int y=0; y<=MAX_VAL; y++)
    printf("%d:%d ", y,c[i][y]);
    printf("\n\n");
  */
}

int do_one()
{
  read_input();
  initialize();
  for(int i=1; i<=n; i++)
    compute(i);

  int min = c[n][0];
  for(int y=1; y <= MAX_VAL; y++)
    if(c[n][y] < min)
      min = c[n][y];

  return min;
}

main()
{
  int T;

  scanf("%d", &T);
  for(int t=0; t<T; t++)
    printf("Case #%d: %d\n",t+1,do_one());
}




#include <cstdio>

#define MAX_N  1000

int r, k, n;
long long gtotal;
int g[MAX_N];
int skip[MAX_N];
int rev[MAX_N];

void read_input()
{
  gtotal = 0;
  scanf("%d %d %d",&r,&k,&n);
  for(int i=0; i<n; i++) {
    scanf("%d",&g[i]);
    gtotal += g[i];
  }
}

void preprocess()
{
  for(int i=0; i<n; i++) {
    int j = 0;
    int c = 0;
    int rv = 0;
    int s = 0;
    while(c < k) {
      c += g[(i + j) % n];
      j++;
      if(c<=k) {
	rv = c;
	s = j;
      }
    }
    rev[i] = rv;
    skip[i] = s;
    //printf("(%d) r: %d, s: %d\n",i,rev[i],skip[i]);
  }
}

void process(int t)
{
  long long money;
  read_input();
  if(k>=gtotal) {
    money = ((long long)r) * (gtotal);
    printf("Case #%d: %lld\n",t+1,money);
    return;
  }

  preprocess();
  money = 0;
  int cur_pos = 0;
  //printf("--\n");
  for(int i=0; i<r; i++) {
    money += rev[cur_pos];
    cur_pos = (cur_pos + skip[cur_pos]) % n;
    //printf("%lld\n",money);
  }
  printf("Case #%d: %lld\n",t+1,money);
}

main()
{
  int T;
  scanf("%d",&T);
  for(int t=0; t<T; t++) {
    fprintf(stderr,"%d\n",t);
    process(t);
  }
}

#include <cstdio>
#include <iostream>
#include <utility>

int main(void) {
  int t,n,r,k;
  int g[1234];
  int v[1234];
  std::pair<int,int> cy[1234];
  scanf(" %d",&t);
  for(int c=1;c<=t;c++) {
    scanf(" %d %d %d",&r,&k,&n);
    for(int i=0;i<n;i++) {
      scanf(" %d",g+i);
      v[i] = -1;
    }
    int p = 0;
    int cn = 0;
    unsigned long long cp;
    int cs;
    unsigned long long tp = 0;
    for(int i=0;i<std::min(n+1,r);i++) {
      int acc = 0;
      int j;
      if (v[p] >= 0) {
	// achou rho;
	cp = 0;
	cs = 0;
	for(int z=cn-1;z>=0;z--) {
	  ++cs;
	  cp += cy[z].second;
	  if(cy[z].first == p) break;
	}
	int missing = r - i;
	tp += (missing/cs)*cp;
	for(int v=0;v<missing%cs;v++) {
	  tp += cy[cn-cs+v].second;
	}
	break;
      }
      v[p] = i;
      for(j=p;;) {
	if (acc + g[j] > k) 
	  break; 
	acc += g[j];
	if ((j=(j+1)%n) == p)
	  break;
      }
      cy[cn++] = std::make_pair(p,acc);
      p = j;
      tp += acc;
    }
    printf("Case #%d: %Lu\n",c,tp);
  }
  return(0);
}

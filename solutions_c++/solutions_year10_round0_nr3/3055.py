#include <cstdio>
using namespace std;

int main() {
  freopen("inp.in", "r" , stdin);
  freopen("output.txt", "w", stdout);
  int t,r,k,n,g[1000];

  scanf("%d", &t);

  for(int tc=1; tc<=t; tc++) {
  scanf("%d%d%d", &r, &k, &n);
  for(int i=0; i<n; i++)
	scanf("%d", &g[i]);

  int total = 0, temp, cnt, pos=0;
  for(int i=0; i<r; i++) {
    temp = 0;
	cnt = 0;
	while(cnt<n && temp+g[pos]<=k) {
	  temp += g[pos];
	  pos = (pos+1)%n;
	  cnt++;
	}
	total += temp;
  }

  printf("Case #%d: %d\n", tc, total);
  }

  return 0;

}
#include <cstdio>
using namespace std;

int main() {
  int n,k,r,t;
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  scanf("%d", &t);
  for(int tc=1; tc<=t; tc++) {
	scanf("%d%d", &n, &k);
	r=1;
	for(int i=1; i<=n; i++) r*=2;
	k++;

	if(k%r==0)
	  printf("Case #%d: ON\n", tc);
	else
	  printf("Case #%d: OFF\n", tc);
  }

  return 0;
}
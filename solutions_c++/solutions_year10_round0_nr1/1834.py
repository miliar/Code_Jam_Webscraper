#include<stdio.h>

int main() {
  int cs, step = 0;
  scanf("%d",&cs);
  while(cs--) {
	step ++;
    int n, k;
	scanf("%d%d",&n,&k);
	bool re = true;
	while(n--) {
		if(k % 2 == 0) re = false;
		k = k / 2;
	}
	printf("Case #%d: %s\n", step, re?"ON":"OFF");
  }
  return 0;
}
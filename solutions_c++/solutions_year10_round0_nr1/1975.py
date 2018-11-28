#include <iostream>
#include <cstdio>

using namespace std;

int n, k, bit, i;

int main() {
    
int t;

scanf("%d", &t);
for(int tt=0;tt<t;tt++){
  
  cin >> n >> k;
  for (i=n-1; i>=0; i--) {
      bit = ((k >> i) & 1);
      if(bit != 1){
	printf("Case #%d: OFF\n", tt+1);
	break;
      }
  }
  if(i == -1) printf("Case #%d: ON\n", tt+1);
}

return 0;
}
#include <iostream>
#include <cstdio>

using namespace std;

int other[1000];

int main(){

  int TT;
  scanf("%d", &TT);
  for(int T = 0; T < TT; T++){
    
    int n, l,h;
    scanf("%d %d %d", &n, &l, &h);
    for(int i=0; i<n; i++)
      scanf("%d", &other[i]);
    
    bool can;
    int i;
    for(i=l; i<=h; i++){
      can = true;
      for(int j=0; j<n; j++){
	if(other[j] % i != 0 && i % other[j] != 0){
	  can = false;
	  break;
	}
      }
      if(can) break;
    }
    if(can)
      printf("Case #%d: %d\n", T+1, i);
    else
      printf("Case #%d: NO\n", T+1);
  }
  
  return 0;
}
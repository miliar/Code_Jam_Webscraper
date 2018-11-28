#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int main(){
  //freopen("a.in", "r", stdin);
  //freopen("a.out", "w", stdout);
  
  int testcases;
  scanf("%d", &testcases);
  
  int d, from, to;
  int players[1000];
  for(int test = 0; test < testcases; test++){
    scanf("%d %d %d", &d, &from, &to);
    for(int i = 0; i < d; i++)
      scanf("%d ", &players[i]);
    
     bool g = false;
    for(int i = from; i <= to; i++){
      bool gerai = true;
      for(int j = 0; j < d; j++){
	if(i > players[j] && i % players[j] != 0)
	  gerai = false;
	if(i < players[j] && players[j] % i != 0)
	  gerai = false;
	}
	if(gerai){
	  printf("Case #%d: %d\n", test + 1, i);
	  g = true;
	  break;
	  }
    }
    if(!g)
      printf("Case #%d: NO\n", test + 1);
    
  }
  
  return 0;
}
#include <cstdio>
#include <vector>
using std::vector;

int main(){
  int t;
  scanf("%d", &t);
  for(int i = 0; i < t; i++){
    vector<bool> snappers;
    int n, k;
    scanf("%d %d", &n, &k);
    for(int j = 0; j < n; j++)snappers.push_back(false);
    for(int j = 0; j < k; j++){
      //snap fingers
      int light = 0;
      while(snappers[light]){
	snappers[light] = false;
	light++;
	if(light >= n)break;
      }
      if(light < snappers.size())snappers[light] = !snappers[light];
    }
    int count = 0;
    for(int j = 0; j < snappers.size(); j++)count += snappers[j];
    if(count == n){
      printf("Case #%d: ON\n",i+1);
    }
    else printf("Case #%d: OFF\n",i+1);
  }
  return 0;
}
      
  
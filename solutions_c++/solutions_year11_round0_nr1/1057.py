#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>

int n, position;
char who;

void simulate(int& position, int target, int moves) {
  if (abs(position - target) <= moves){ position = target; return ; }
  int dx = (position < target ? 1 : -1);
  position += dx * moves; 
}

int readAndSolveSingleCase(){
  std::vector<int> blue, orange, all, type;
  
  scanf("%d",&n);
  for (int i = 1; i <= n; i++) {
    scanf(" %c %d",&who,&position);
    all.push_back(position);
    type.push_back(who);
    
    if (who == 'B') blue.push_back(position);
    else orange.push_back(position);
  }
  
  int btarget = 0, otarget = 0;
  int bposition = 1, oposition = 1;
  
  int res = 0;
  for(int i = 0; i < n; i++) {
    int moves = 0;
    if (type[i] == 'B') moves = abs(bposition - all[i]);
    else moves = abs(oposition - all[i]);
    
    if (btarget != blue.size()) simulate(bposition, blue[btarget], moves);
    if (otarget != orange.size()) simulate(oposition, orange[otarget], moves);
    
    if (type[i] == 'O'){
      otarget++;
      if (btarget != blue.size()) simulate(bposition, blue[btarget], 1);
    }
    else{
      btarget++;
      if (otarget != orange.size()) simulate(oposition, orange[otarget], 1);
    }
    
    res += moves + 1;
  }
  return res;
}

int main(){
  int cases;
  scanf("%d", &cases);
  for (int i = 1; i <= cases; i++) {
    printf("Case #%d: %d\n",i, readAndSolveSingleCase());
  }
  return 0;
}

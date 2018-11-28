#include <iostream>
#include <cstdlib>

using namespace std;

const int INFTY = 0x7FFFF;

int min(int x, int y){
  if(x < y)
    return x;
  return y;
}

int min(int x, int y, int z){
  return min(x,min(y,z));
}

struct binarytree{
  int type; // 0 = leaf, 1=and, 2=or
  bool val; // defined <=> leaf
  bool canchange;
  binarytree* left;
  binarytree* right;
  int mintoTrue;
  int mintoFalse;
  void update(){
    int andoffset = 0;
    int oroffset = 0;
    switch(type){
    case 0:
      if(val){
	mintoTrue = 0;
	mintoFalse = INFTY;
      }
      else{
	mintoTrue = INFTY;
	mintoFalse = 0;
      }
      return;
    case 1:
      if(canchange) oroffset = 1;
      else oroffset = INFTY; 
      break;
    case 2:
      if(canchange) andoffset = 1;
      else andoffset = INFTY;
      break;
    }
    left->update();
    right->update();
    mintoTrue = min(andoffset + left->mintoTrue + right->mintoTrue, oroffset + left->mintoTrue, oroffset + right->mintoTrue);
    mintoFalse = min(andoffset + left->mintoFalse, andoffset + right->mintoFalse, oroffset + left->mintoFalse + right->mintoFalse);
    if(mintoTrue > INFTY) mintoTrue = INFTY;
    if(mintoFalse > INFTY) mintoFalse =INFTY;
  }
};

void solve(int caseno){
  int M,V;
  cin >> M >> V;
  binarytree *nodes = new binarytree[M+1];
  for(int i=1; i<=(M-1)/2; ++i){
    int G,C;
    cin >> G >> C;
    nodes[i].type = 2-G;
    nodes[i].canchange = (C == 1);
    nodes[i].left = nodes+2*i;
    nodes[i].right = nodes+2*i+1;
  }
  for(int i=(M+1)/2; i<=M; ++i){
    int I;
    cin >> I;
    nodes[i].type = 0;
    nodes[i].val = (I == 1);
  }
  nodes[1].update();
  int ans;
  if(V == 1)
    ans = nodes[1].mintoTrue;
  else ans = nodes[1].mintoFalse;

  /*
  for(int i=1; i<=M; ++i){
    cout << nodes[i].mintoTrue << " " << nodes[i].mintoFalse << " " << nodes[i].canchange << endl;
  }
  */

  if(ans >= INFTY){
    printf("Case #%d: IMPOSSIBLE\n", caseno);
  }
  else{
    printf("Case #%d: %d\n", caseno, ans);
  }
}

int main(){
  int n;
  cin >> n;
  for (int i=0; i<n; ++i){
    solve(i+1);
  }
  return 0;
}

#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
using namespace std;

vector <int> arvore;
vector <int> gates;
vector <int> change;
int m;

void fillTree(int n){
  int x, y;

  if (n > (m-1)/2) return;
  fillTree(2*n);
  fillTree(2*n + 1);
  x = arvore[2*n];
  y = arvore[2*n + 1];
  if (gates[n] == 1 && x == 1 && y == 1)
    arvore[n] = 1;
  else if (gates[n] == 0 && (x == 1 || y == 1))
    arvore[n] = 1;
  else
    arvore[n] = 0;
  return;
}

int arruma(int p, int v){
  int x, y, ans;

  if (arvore[p] == v) return 0;
  if (p > (m-1)/2) return -1;
  if (v == 1){
    if (change[p] == 1 && gates[p] == 1 &&
	(arvore[2*p] == 1 || arvore[2*p+1] == 1)){
      gates[p] = 0;
      return 1;
    }
    if (change[p] == 1 && gates[p] == 1){
      // And ch
      x = arruma(2*p, 1);
      y = arruma(2*p+1, 1);

      if (x == -1 && y == -1) return -1;
      if (x == -1) return y+1;
      if (y == -1) return x+1;

      ans = x + y;
      if (ans > x + 1)
	ans = x + 1;
      if (ans > y + 1)
	ans = y + 1;
      return ans;
    }
    else if (gates[p] == 1){
      // And
      x = arruma(2*p, 1);
      y = arruma(2*p+1, 1);

      if (x == -1 || y == -1) return -1;
      ans = x + y;
      return ans;
    }
    else{
      // Or
      x = arruma(2*p, 1);
      y = arruma(2*p+1, 1);

      if (x == -1 && y == -1) return -1;
      if (x == -1) return y;
      if (y == -1) return x;

      if (x < y) return x;
      else return y;
    }
  }
  else{
    if (change[p] == 1 && gates[p] == 0){
      x = arruma(2*p, 0);
      y = arruma(2*p+1, 0);
      
      if (x == -1 && y == -1) return -1;
      if (x == -1){
	//printf("Troca %d dir\n", p);
	return y+1;
      }
      if (y == -1){
	//printf("Troca %d esq\n", p);
	return x+1;
      }

      ans = x+y;
      if (ans > x+1){
	//printf("Troca %d esq\n", p);
	ans = x+1;
      }
      if (ans > y+1){
	//printf("Troca %d dir\n", p);
	ans = y+1;
      }
      return ans;
    }
    else if (gates[p] == 0){
      x = arruma(2*p, 0);
      y = arruma(2*p+1, 0);
      
      if (x == -1 || y == -1) return -1;
      
      return x+y;
    }
    else{
      x = arruma(2*p, 0);
      y = arruma(2*p+1, 0);
      
      if (x == -1 && y == -1) return -1;
      if (x == -1) return y;
      if (y == -1) return x;

      if (x < y) return x;
      else return y;
    }
  }
}

int main(){
  int n, ka, v, i, g, c, val, mov;

  scanf("%d", &n);
  for (ka = 1; ka <= n; ka++){
    scanf("%d %d", &m, &v);
    arvore.clear();
    arvore.push_back(-1);
    change.clear();
    change.push_back(-1);
    gates.clear();
    gates.push_back(-1);
    for (i = 1; i <= (m-1)/2; i++){
      scanf("%d %d", &g, &c);
      arvore.push_back(-1);
      gates.push_back(g);
      change.push_back(c);
    }
    for (i = (m-1)/2 + 1; i <= m; i++){
      scanf("%d", &val);
      arvore.push_back(val);
    }

    fillTree(1);
    
    mov = 0;
    if (arvore[1] != v){
      mov = arruma(1, v);
    }

    printf("Case #%d: ", ka);
    if (mov == -1)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", mov);
  }


  return 0;
}

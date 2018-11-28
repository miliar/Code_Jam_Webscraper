#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
using namespace std;

int permut[6];
char s[1010];
string str;

int confere(int tam){
  int i, j, groups = 0;
  char ant = '?';
  
  for (i = 0, j = 0; tam*j + i < str.length(); i++){
    if (i == tam){
      i = 0;
      j++;
    }
    //printf("%c vs %c\n", str[tam*j + permut[i]], ant);
    if (str[tam*j + permut[i]] != ant){
      groups++;
      //      printf("%c%c ", ant, str[tam*j + permut[i]]);
      ant = str[tam*j + permut[i]];
    }
    //printf("\n");
  }
  return groups;
}

int permuta(int ini, int fim){
  int i, at, ops, ans, x;

  ans = 1111;
  if (ini == fim){
    x = confere(fim);
    //    for (i = 0; i < fim; i++)
    //  printf("%d", permut[i]);
    //printf(" %d\n", x);
    return x;
  }

  for (at = 0; at < fim; at++){
    ops = 0;
    for (i = 0; i < ini; i++){
      if (permut[i] == at){
	ops = 1;
	break;
      }
    }
    //    printf("%d (%d)\n", at, ops);
    if (ops == 1) continue;
    permut[ini] = at;
    //    printf(".\n");
    x = permuta(ini+1, fim);
    if (ans > x)
      ans = x;
  }
  return ans;
}

int main(){
  int n, ka, k, x;
  
  scanf("%d", &n);

  for (ka = 1; ka <= n; ka++){
    scanf("%d", &k);
    scanf("%s", s);
    str = s;
    x = permuta(0, k);
    
    printf("Case #%d: %d\n", ka, x);
  }

  return 0;
}

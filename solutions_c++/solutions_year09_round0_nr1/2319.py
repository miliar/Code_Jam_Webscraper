#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <set>

using namespace std;

int main(){
  int l, d, n;
  set <char> seven[20];
  char word[5050][20];
  
  scanf("%d %d %d", &l, &d, &n);

  for (int i = 0; i < d; i++){
    scanf("%s", word[i]);
  }
  getchar();

  for (int i = 1; i <= n; i++){
    for (int j = 0; j < l; j++)
      seven[j].clear();
    bool in = false;
    int j = 0;
    
    char c = getchar();
    while (c != '\n'){
      if (c == '('){
	in = true;
      }
      else if (c == ')'){
	in = false;
	j++;
      }
      else{
	seven[j].insert(c);
	if (!in)
	  j++;
      }
      c = getchar();
    }

    int howmany = 0;
    for (int j = 0; j < d; j++){
      bool ok = true;
      for (int k = 0; k < l; k++){
	if (seven[k].count(word[j][k]) == 0){
	  ok = false;
	  break;
	}
      }
      if (ok){
	howmany++;
      }
    }

    printf("Case #%d: %d\n", i, howmany);
  }
  
  return 0;
}

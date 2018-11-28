#include<stdio.h>
#include<string.h>
#include<list>

using namespace std;

list<char> L;
list<char>::iterator it;


int main(){
  int t, c, d, n;
  int i, j, pos, band, ncase;
  char element, back, c1, c2, c3, d1, d2;
  char C[30][30], D[30][30];

  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);

  scanf("%d", &t);
  for(ncase=1; ncase <= t; ncase++){
    scanf("%d", &c);
    getchar();

    memset(C, 0, 30*30*sizeof(C[0][0]));
    memset(D, 0, 30*30*sizeof(D[0][0]));

    for(i=1; i<= c; i++){
      c1 = getchar() - 'A';
      c2 = getchar() - 'A';
      c3 = getchar();
      C[c1][c2] = c3;
      C[c2][c1] = c3;
      getchar();
    }

    scanf("%d", &d);
    getchar();
    for(i=1; i<= d; i++){
      d1 = getchar() - 'A';
      d2 = getchar() - 'A';
      D[d1][d2] = 1;
      D[d2][d1] = 1;
      getchar();
    }
    
    scanf("%d", &n);
    getchar();
    L.clear();
    for(j=1; j<= n; j++){
      element = getchar() - 'A';
      if(!L.size()){
	L.insert(L.end(), element+'A');
	continue;
      }
      band = 1;
      back = L.back() - 'A';
      if(C[element][back]){
	L.pop_back();
	band = 0;
	L.insert(L.end(), C[element][back]);
      }
      else{
	for(it=L.begin(); it != L.end(); it++){
	  if(D[element][*it-'A']){
	    L.clear();
	    band = 0;
	    break;
	  }
	}
      }
      if(band){
	L.insert(L.end(), element+'A');
      }
    }
    if(L.size() == 0)
      printf("Case #%d: []\n", ncase);
    else if(L.size() == 1){
      it = L.begin();
      printf("Case #%d: [%c]\n", ncase, *it);
    }
    else{
      it = L.begin();
      printf("Case #%d: [%c", ncase, *it);
      it++;
      for(; it != L.end(); it++){
	printf(", %c", *it);
      }
      printf("]\n");
    }

  }
  return 0;
}

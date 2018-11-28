#include <cstdio>
#include <string>
#include <cstring>
#include <set>
#include <vector>
#include <map>
using namespace std;

struct par {
  long long x;
  long long y;
};

int main(){
  vector <struct par> trees;
  struct par aux;
  int ka, Nc, n;
  long long a, b, c, d, x0, y0, m, i, x, y, j, k;
  long long triangulo;

  scanf("%d", &Nc);
  for (ka = 1; ka <= Nc; ka++){
    scanf("%d %lld %lld %lld %lld %lld %lld %lld", &n, &a, &b, &c, &d, &x0, &y0, &m);
    trees.clear();
    aux.x = x0;
    aux.y = y0;
    trees.push_back(aux);
    //    printf("%lld,%lld\n", aux.x, aux.y);
    for (i = 1; i <= n-1; i++){
      aux.x = (a*aux.x + b)%m;
      aux.y = (c*aux.y + d)%m;
      trees.push_back(aux);
      //printf("%lld,%lld\n", aux.x, aux.y);
    }
    triangulo = 0;
    for (i = 0; i < trees.size(); i++){
      for (j = i + 1; j < trees.size(); j++){
	for (k = j+1; k < trees.size(); k++){
	  if ( (trees[i].x + trees[j].x + trees[k].x)%3 == 0 &&
	       (trees[i].y + trees[j].y + trees[k].y)%3 == 0)
	    triangulo++;
	}
      }

    }

    printf("Case #%d: %lld\n", ka, triangulo);
  }

  return 0;
}

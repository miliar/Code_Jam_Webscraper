#include <cstdio>
#include <cstdlib>
#include <cmath>

#define DIST(X1,Y1,X2,Y2) sqrt( (X2-X1)*(X2-X1) + (Y2-Y1)*(Y2-Y1))

using namespace std;

int main(){
  int c, n, x[4], y[4], r[4];

  scanf("%d", &c);

  for (int caso = 1; caso <= c; caso++){
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++){
      scanf("%d %d %d", &x[i], &y[i], &r[i]);
    }
    
    double raio;
    if (n == 1) raio = r[0];

    if (n == 2) {
      raio = r[0];
      if (raio < r[1])
	raio = r[1];

      double aux = (DIST(x[0], y[0], x[1], y[1]) + r[0] + r[1])/2;
      if (raio > aux) raio = aux;
    }

    if (n == 3){
      raio = (DIST(x[0], y[0], x[1], y[1]) + r[0] + r[1])/2;
      double aux = (DIST(x[0], y[0], x[2], y[2]) + r[0] + r[2])/2;
      double aux2 = (DIST(x[1], y[1], x[2], y[2]) + r[1] + r[2])/2;

      if (raio < r[2]) raio = r[2];
      if (aux < r[1]) aux = r[1];
      if (aux2 < r[0])aux2 = r[0];

      if (raio > aux) raio = aux;
      if (raio > aux2) raio = aux2;
    }

    printf("Case #%d: %lf\n", caso, raio);
  }

  return 0;
}

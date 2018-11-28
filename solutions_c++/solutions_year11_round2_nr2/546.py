#include <cstdio>

#define INF (1<<29);
#define max(A,B) (A>B? A : B)

using namespace std;

int c, d;
int p[222], v[222];

bool canDo(double x){
  double lastP = -INF;
  /*bool dim = true;*/
  for (int i = 0; i < c; i++){
    for (int j = 0; j < v[i]; j++){
      if (lastP+d <= p[i]){
	lastP = max(lastP+d, p[i]-x);
	continue;
      }
      else{
	if (lastP+d > p[i]+x)
	  return false;
	/*if (lastP+d == p[i]+x)
	  dim = false;*/
	lastP += d;
      }
    }
  }
  return true;
}

int main(){
  int t;
  scanf("%d", &t);
  for (int ka = 1; ka <= t; ka++){
    scanf("%d %d", &c, &d);
    for (int i = 0; i < c; i++){
      scanf("%d %d", &p[i], &v[i]);
    }
    double ini = 0.0;
    double fim = 1.0;
    

    /*if (canDo(ini) <= 0){
      printf("Case #%d: %lf\n", 0.0);
      continue;
      }*/
    while(!canDo(fim))
      fim *= 2;
    while (fim-ini > 1e-10){
      double m = (ini+fim)/2.0;
      if (canDo(m))
	fim = m;
      else
	ini = m;
    }
    printf("Case #%d: %.10lf\n", ka,fim);
  }

  return 0;
}

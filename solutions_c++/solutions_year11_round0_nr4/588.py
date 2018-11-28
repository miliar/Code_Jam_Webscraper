#include <cstdio>

using namespace std;

double mark[1010][1010];

int fat(int n){
  if (n == 0) return 1;
  return n*fat(n-1);
}

int dis(int n){
  if (n == 0) return 1;
  if (n == 1) return 0;
  return (n-1)*(dis(n-1)+dis(n-2));
}

int choose(int n, int k){
  return (fat(n))/(fat(k)*fat(n-k));
}

double prob(int i, int j){
  //printf("(%d,%d) ch=%d dis=%d fat=%d\n",i,j, choose(i,j),dis(i-j),fat(i));
  return ((double) choose(i,j)*dis(i-j))/fat(i);
}

void fillMark(int n){
  mark[0][0] = 1;
  for (int j = 1; j <= n; j++)
    mark[0][j] = 0;
  for (int i = 1; i <= n; i++){
    for (int j = 0; j <= i; j++)
      mark[i][j] = prob(i,i-j);
    for (int j = i+1; j <= n; j++)
      mark[i][j] = 0;
  }
}

int main(){
  int t, n;
  scanf("%d", &t);

  for (int ka = 1; ka <= t; ka++){
    int c;
    scanf("%d", &n);
    c = n;
    for (int i = 1; i<= n;i++){
      int bla;
      scanf("%d", &bla);
      if (i == bla) c--;
    }
    printf("Case #%d: %d.000000\n", ka, c);
  }

  return 0;
}

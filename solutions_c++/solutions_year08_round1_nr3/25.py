#include <iostream>
#include <cstdlib>

using namespace std;

struct matrix{
  int a,b,c,d;
};

matrix operator*(const matrix &m1, const matrix &m2){
  matrix res;
  res.a = (m1.a*m2.a + m1.b*m2.c)%1000;
  res.b = (m1.a*m2.b + m1.b*m2.d)%1000;
  res.c = (m1.c*m2.a + m1.d*m2.c)%1000;
  res.d = (m1.c*m2.b + m1.d*m2.d)%1000;
  return res;
}

matrix exp(const matrix &m, int n){
  if(n == 0){
    matrix id;
    id.a = 1;
    id.b = 0;
    id.c = 0;
    id.d = 1;
    return id;
  }
  if(n % 2 == 0){
    return exp(m*m, n/2);
  }
  return m*exp(m,n-1);
}

int ans(int n){
  matrix m;
  m.a = 0;
  m.b = 1;
  m.c = -4;
  m.d = 6;
  matrix s;
  s.a=2;
  s.b=6;
  s.c=6;
  s.d=28;
  matrix r = exp(m,n)*s;
  int ret = r.a-1;
  while(ret < 0){
    ret+=1000;
  }
  return ret;
}

void solve(int caseno){
  int k;
  cin >> k;
  printf("Case #%d: %.3d\n",caseno, ans(k));
}

int main(){
 
  int n;
  cin >> n;
  for (int i=0; i<n; ++i)
    solve(i+1);

  return 0;
}

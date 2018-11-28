#include<cstdio>
#include<vector>
#include<cmath>
#include<iostream>
#include<set>

using namespace std;


set<pair<int, int> > z;
set<int> v;

void check(int n, int a, int b){
  int tx = n;
  int p = (int)pow(10, int(log10(n)));
  int pl = int(log10(n));
  int q = 1;
  while(pl-- && tx%10){
    q = tx%10;
    tx/=10;
    tx+=q*p;

    if(tx>=a && tx<=b && tx!=n){
      if(z.find(make_pair(tx,n))==z.end()){
        z.insert(make_pair(n, tx));
      } else
      return;
 //   printf("%d\n", tx);
    }
  }

}

int testcase(int a, int b){
  z.clear();
  int w = 0;
  for (int i=a; i <=b; i++) {
    check(i, a, b);
  }
  return z.size();
}


int main(int argc, const char *argv[]){
  int n,a,b;
  scanf("%d", &n);
  for(int i = 0; i < n; i++){
    scanf("%d%d", &a, &b);
    printf("Case #%d: %d\n", i+1, testcase(a,b));
  }
  
  return 0;
}


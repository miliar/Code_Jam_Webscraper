#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }


int main(){
  int tn;
  scanf("%d",&tn);
  for (int ii=1;ii<=tn;ii++){
    long long n,k,bit;
    scanf("%lld%lld",&n,&k);
    bit = (1<<n)-1;
    if ((k&bit)==bit){
      printf("Case #%d: ON\n",ii);
    }else{
      printf("Case #%d: OFF\n",ii);
    }

  }
  return 0;
}

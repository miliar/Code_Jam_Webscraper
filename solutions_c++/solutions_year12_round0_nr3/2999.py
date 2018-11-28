#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cas,tt,lb,ub,i,ans,number,digit;
    int pow[9];
    pow[0] = 1;
    for(i = 1;i <= 9;++i) pow[i] = pow[i - 1] * 10;
    scanf("%d",&tt);
    for(cas = 1; cas <= tt;++cas) {
      scanf("%d %d",&lb,&ub);
      for(i = lb,digit = 0;i;i /= 10) digit++;
      ans = 0;
      for(i = lb;i <= ub;++i) {
        number = i;
        do {
          number = number % 10 * pow[digit - 1] + number / 10;
          if(number > i && number >= lb && number <= ub) ans++;
        }while(number != i);
      }
      printf("Case #%d: %d\n",cas,ans);
    }
}

#include <stdio.h>
using namespace std;

int abs(int i){
    if (i<0) return -i;
    else return i;
}

int main(){
    int blue, orgran, tot, t, n, whi, timeB, timeO, ii, kk; // Blue  ii,  Orgran  jj
    long ans;
    char c;
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    scanf("%d", &t);
    tot = 0;
    while (t>0){
          ans = 0;   tot ++;
          blue = 1; orgran = 1; timeB = 0; timeO =0;
          scanf("%d", &n);
          while (n>0){
                scanf("%s%d", &c, &whi);
                if (c == 'O'){
                      //printf("::: %d|%d :::\n", whi, orgran);
                      if (timeO<timeB){
                           //timeO = timeB;
                           timeO += abs(whi-orgran);
                           if (timeO < timeB) timeO = timeB;
                           timeO ++;  orgran = whi;
                      }
                      else{
                           timeO += abs(whi-orgran);
                           timeO ++; orgran = whi;
                      } 
                }
                else{
                     //printf("::: %d|%d :::\n", whi, blue);
                     if (timeB<timeO){
                         timeB += abs(whi-blue);
                         if (timeB < timeO) timeB = timeO;
                         timeB ++; blue = whi;
                     }
                     else{
                         timeB += abs(whi-blue);
                         timeB ++;   blue = whi;
                     }
                }
                n --;
                //printf("--------%d %d ---------\n", timeO, timeB);
          }
          if (timeB > timeO) ans = timeB;
          else ans = timeO;
          printf("Case #%d: %d\n", tot, ans);
          t --;
    }
    return 0;
}

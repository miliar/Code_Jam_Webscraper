#include <vector>
#include <set>
#include <deque>
#include <string>

using namespace std;

int ni() {
    int foo;
    scanf("%d", &foo);
    return foo;
}


int gcd(int a, int b) {
  while(b) {
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

int lcm(int a,int b){
  int ret = (a * b) / gcd(a,b);
  //printf("lcm of %d and %d is %d\n", a, b, ret);
  return ret;
}

int players[2 << 16];

int main() {
   int c = ni();

   for(int i=0;i<c;i++) {
     int n,l,h;
     scanf("%d %d %d", &n, &l, &h);
     for(int j=0;j<n;j++) {
       scanf("%d", players + j);
     }
     
     int res =1;
     int gcdres = 1;
     for(int j=0;j<n;j++) {
       res = lcm(res, players[j]);
       gcdres = gcd(gcdres, players[j]);
     }

     int ans = -1;

     for(int j=l;j<=h;j++) {
       bool satisfied = true;
       for(int k=0;k<n;k++) {
         int rem = players[k] % j;
         int revrem = j % players[k];

         // printf("Trying note of %d vs player with %d\n", j, players[k]);
         
         if((j > players[k] && revrem) || (j <= players[k] && rem)) {
           //printf("not Satisfied with %d\n", j);
           satisfied = false;
           continue;
         }
       }

       if(satisfied) { ans = j; break;}
     }

 
   printout:
     printf("Case #%d: ", i+1);
     if(ans == -1) {
       printf("NO\n");
     } else {
       printf("%d\n", ans);
     }
   }
}


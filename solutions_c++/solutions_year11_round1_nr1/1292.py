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

int main() {
   int c = ni();

   for(int i=0;i<c;i++) {
     int games, pd, pg;
     scanf("%d %d %d\n", &games, &pd, &pg);

     bool poss = false;
     if(games >= 100) {
       poss = true;
     } else {
       for(int j=1;j<=games;j++) {
         if(!((pd * j) % 100) && ((pg != 100 || pd == 100))) {
           poss = true;
           if(pg==0 && pd != 0) { poss = false;} 
           else {
             break;
           }
         }
       }
     }

 
     printf("Case #%d: ", i+1);
     printf("%s\n", poss ? "Possible" : "Broken");
   
   }
}


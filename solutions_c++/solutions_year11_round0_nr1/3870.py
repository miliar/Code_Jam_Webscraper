#include<stdio.h>              
#include<algorithm>
using namespace std;
int T, N;
int max(int a, int b) { return (a>b) ? a : b;}

int main() {
  scanf("%d", &T);int tei = 0;
  for (int i = 0;i < T;i++ ) {
    scanf("%d", &N);
    int tahy = 0, tahyd=0, btB=1, btO=1, last = -1;
    for (int k = 0; k < N; k++) {
      char c; int l; scanf("%s%d", &c, &l);
      if (c == 'B') {
        if (last == 0) {
          tahy+=max(l-btB, btB-l) + 1;
          tahyd += max(l-btB, btB-l) + 1;          
        }
        else {
          last = 0;
          tahy += max(0, max(l-btB, btB-l)-tahyd)+1;
          tahyd = max(0, max(l-btB, btB-l)-tahyd)+1;  
        }
        btB = l;  
      }
      else {
        if (last == 1) {
          tahy+=max(l-btO, btO-l) + 1;
          tahyd += max(l-btO, btO-l) + 1;          
        }
        else {
          last = 1;
          tahy += max(0, max(l-btO, btO-l)-tahyd)+1;
          tahyd = max(0, max(l-btO, btO-l)-tahyd)+1;  
        }
        btO = l;
      }
      
    }
    printf("Case #%d: %d\n", i+ 1, tahy);
  }
 return 0;
}

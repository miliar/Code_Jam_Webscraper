#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define MAX_N 300

char Com[MAX_N][MAX_N];
bool Opp[MAX_N][MAX_N];

char Src[MAX_N];
char Des[MAX_N];
int Cnt;

void proCom() {
     if (Cnt < 2) {
        return;        
     }
     char c1 = Des[Cnt - 2];
     char c2 = Des[Cnt - 1];
     if (Com[c1][c2]) {
        Des[Cnt - 2] = Com[c1][c2];
        Cnt--;       
     }
}

void proOpp() {
     if (Cnt < 1) {
        return;
     }
     char c1 = Des[Cnt - 1];
     for (int i = 0; i < Cnt - 1; i++) {
         char c2 = Des[i];
         if (Opp[c1][c2]) {
            Cnt = 0;
            break;
         }
     }
}

void init() {
     memset(Com, 0, sizeof(Com));
     memset(Opp, 0, sizeof(Opp));     
}

void solve() {
     Cnt = 0;
     for (int i = 0; Src[i]; i++) {
         Des[Cnt++] = Src[i];
         proCom();
         proOpp();
     }
}

void output(int cse) {
     //Case #1: [E, A]
     printf("Case #%d: [", cse);
     for (int i = 0; i < Cnt; i++) {
         if (i > 0) {
            printf(", ");      
         }
         printf("%c", Des[i]);    
     }
     printf("]\n");
}

int main() {
    int T;
    freopen("C:\\setup\\in2.txt", "r", stdin);
    freopen("C:\\setup\\out2.txt", "w", stdout);
    scanf("%d", &T);
    int cse = 0;
    while (T--) {
          cse++;
          init();
          int n;
          char buf[10];
          scanf("%d", &n);
          for (int i = 0; i < n; i++) {
              scanf("%s", buf);
              Com[buf[0]][buf[1]] = buf[2];
              Com[buf[1]][buf[0]] = buf[2];    
          }
          scanf("%d", &n);
          for (int i = 0; i < n; i++) {
              scanf("%s", buf);
              Opp[buf[0]][buf[1]] = true;
              Opp[buf[1]][buf[0]] = true;
          }
          scanf("%d", &n);
          scanf("%s", Src);
          Src[n] = 0;
          solve();
          output(cse);
    }
    return 0;    
}

#include <cstdio>
#include <ctype.h>
#include <string.h>

//#define DBG

int T;

char A[128];

char G[102];

void readInput() {
   fgets(G, 102, stdin);
}


void solve() {
   //for (char* c=G; islower(*c) || *c == ' '; c++) printf("%c", A[*c]);
   int l = strlen(G);
   for (int i=0; i<l && (islower(G[i]) || G[i] == ' '); i++) {
      //fprintf(stderr, "--%zu--%c--\n", (size_t)(G[i]), A[(size_t)(G[i])]);
      printf("%c", A[(size_t)(G[i])]);
   }
   printf("\n");
}



int main() {
   A[32] = ' ';

   A[97] = 'y';
   A[98] = 'h';
   A[99] = 'e';
   A[100] = 's';
   A[101] = 'o';
   A[102] = 'c';
   A[103] = 'v';
   A[104] = 'x';
   A[105] = 'd';
   A[106] = 'u';
   A[107] = 'i';
   A[108] = 'g';
   A[109] = 'l';
   A[110] = 'b';
   A[111] = 'k';
   A[112] = 'r';
   A[113] = 'z';
   A[114] = 't';
   A[115] = 'n';
   A[116] = 'w';
   A[117] = 'j';
   A[118] = 'p';
   A[119] = 'f';
   A[120] = 'm';
   A[121] = 'a';
   A[122] = 'q';

   scanf("%d ", &T);
   //fgets(G, 5, stdin); // consume newline
   for (int i=1; i<=T; ++i) {
      readInput();
      printf("Case #%d: ", i);
      solve();
   }

}


#include <cstdio>
#include <cctype>
using namespace std;

int M[26];
void populateM() {
  M[4]  = 14;
  M[9]  = 20;
  M[15] = 17;
  M[12] = 11;
  M[24] = 0;
  M[18] = 13;
  M[11] = 6;
  M[2]  = 4;
  M[10] = 8;
  M[3]  = 18;
  M[23] = 12;
  M[21] = 15;
  M[13] = 1;
  M[17] = 19;
  M[8]  = 3;
  M[1]  = 7;
  M[19] = 22;
  M[0]  = 24;
  M[7]  = 23;
  M[22] = 5;
  M[5]  = 2;
  M[14] = 10;
  M[20] = 9;
  M[6]  = 21;
  M[16] = 25;
  M[25] = 16;
}


int main() {
  int T;
  char c;
  freopen("problem_a.in", "r", stdin); populateM();

  scanf("%d", &T); c = getchar();
  for (int i = 1; i <= T; i++) {
    printf("Case #%d: ", i);
    c = getchar();
    while (isalpha(c) || c == ' ') {
      if (c != ' ') {
        putchar(M[c-'a'] + 'a');
      } else {
        putchar(c);
      }
      c = getchar();
    }
    putchar('\n');
  }
}
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>

char s[239];


int p[20], pc;
long long data;

int main () {
  int tn;
  scanf ("%d", &tn); gets (s);
  for (int tc = 1; tc <= tn; tc++) {
    gets (s);
    int l = strlen (s);
    data = 0;
    pc = 0;
    for (int i = 0; i < l; i++) {
      if (s[i] == '0') {
        data *= 2;
      } else if (s[i] == '1') {
        data = data * 2 + 1;
      } else {
        data *= 2;
        p[pc++] = l - i - 1;
      }
    }


    int h;
    long long v2 = -1, cd = -1;

    for (h = 0; h < (1 << pc); h++) {
      cd = data;
      int s = h ^ (h >> 1);

      //printf ("%08x\n", s);

      for (int j = 0; j < pc; j++)
        if (s & (1 << j))
          cd |= 1LL << p[j];
      v2 = (long long)sqrtl (cd);
      if (v2 * v2 == cd) break;
      ++v2;
      if (v2 * v2 == cd) break;
      v2 -= 2;
      if (v2 * v2 == cd) break;
    }

    assert (h != (1 << pc));

    data = (long long)cd;
    pc = 0;
    do {
      s[pc++] = (data % 2) + '0';
      data /= 2;
    } while (data);
    printf ("Case #%d: ", tc);
    for (int i = pc - 1; i >= 0; i--) putchar (s[i]);
    puts ("");
  }
}
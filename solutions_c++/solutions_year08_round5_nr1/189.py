#include <cstdio>

const int d[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

int T, n, t, x, y, mxx[256], mnx[256], a, v, z;
char s[256];

void c(char q) {
  if (q == 'R')
    ++z;
  else if (q == 'L')
    --z;
  else {
    int px = x, py = y;
    x += d[z&3][0];
    y += d[z&3][1];
    a += x*py - y*px;
    if (!(z&3)) {
      if (mxx[px] < py)
        mxx[px] = py;
      if (mnx[px] > py)
        mnx[px] = py;
    } else if ((z&3) == 2) {
      if (mxx[x] < y)
        mxx[x] = y;
      if (mnx[x] > y)
        mnx[x] = y;
    }
  }
}

int main() {
  scanf("%d", &T);
  for (int r = 1; r <= T; ++r) {
    for (int i = 0; i < 256; ++i)
      mxx[i] = 0;
    for (int i = 0; i < 256; ++i)
      mnx[i] = 256;
    x = y = 128;
    a = v = z = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
      scanf("%s%d", s, &t);
      for (int j = 0; j < t; ++j)
        for (int k = 0; s[k]; ++k)
          c(s[k]);
    }
    for (int i = 0; i < 256; ++i)
      for (int j = 0; j < 256; ++j)
        for (int k = i + 1; k < j; ++k) {
          if (mxx[k] < mxx[i] && mxx[k] < mxx[j])
            mxx[k] = mxx[i] < mxx[j] ? mxx[i] : mxx[j];
          if (mnx[k] > mnx[i] && mnx[k] > mnx[j])
            mnx[k] = mnx[i] > mnx[j] ? mnx[i] : mnx[j];
        }
    for (int i = 0; i < 256; ++i)
      if (mxx[i] > mnx[i])
        v += mxx[i] - mnx[i];
    if (a < 0)
      a = -a;
    printf("Case #%d: %d\n", r, v - a/2);
    /*
    printf("? %d\n", a/2);
    for (int i = 0; i < 256; ++i)
      if (mxx[i] > mnx[i])
        printf("- %d : %d %d\n", i, mxx[i], mnx[i]);
    */
  }
  return 0;
}
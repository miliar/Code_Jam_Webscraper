#include <cstdio>
#include <string.h>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;

const int MAX_LEN = 51;
const int MAX_TERM = 5;
const int MAX_DEG = 4;
const int NUM_CHAR = 26;
const int MAXN = 100;
const int MAXK = 10;
const int modulo = 10009;

int main () {
  int t, c, i, j, n, k, d;
  char poly[MAX_LEN], buf[MAX_LEN], s;
  int terms[MAX_TERM][MAX_DEG], count[MAXN][NUM_CHAR];
  int len, term_count, term_i;
  int power_n[MAXK];
  int ans, tmp, deg;
  int x[MAX_DEG];
  int v;

  int sum[MAX_TERM][1 << MAX_DEG];
  int selected, available;
  
  scanf("%d\n", &t);
  for (c = 1; c <= t; ++c) {
    scanf("%s %d\n", &poly, &k);

    /* terms */
    len = strlen(poly); term_count = 0; term_i = 0;
    for (j = 0; j <= len; ++j) {
      if (poly[j] != '+' && poly[j] != '\0')
	terms[term_count][term_i++] = poly[j] - 'a';
      else {
	terms[term_count][term_i] = -1;
	term_count++;
	term_i = 0;
      }
    }
    fprintf(stderr, "term_count: %d\n", term_count);
    for (i = 0; i < term_count; ++i) {
      for (j = 0; terms[i][j] != -1; ++j)
	fprintf(stderr, "%c", terms[i][j]+'a');
      fprintf(stderr, "\n");
    }

    scanf("%d\n", &n);
    for (i = 0; i < n; ++i) {
      scanf("%s\n", &buf);
      
      /* count */
      len = strlen(buf);
      for (j = 0; j < NUM_CHAR; ++j)
	count[i][j] = 0;
      for (j = 0; j < len; ++j)
	++count[i][buf[j] - 'a'];
    }

    /* power_n */
    power_n[0] = 1;
    for (i = 1; i < MAXK; ++i)
      power_n[i] = power_n[i-1] * n % modulo;
    
    /* sum */
    for (j = 0; j < term_count; ++j) {
      for (deg = 0; (deg < 4) && (terms[j][deg] != -1); ++deg);
      for (selected = 0; selected < (1 << deg); ++selected) {
	sum[j][selected] = 0;
	for (i = 0; i < n; ++i) {
	  tmp = 1;
	  for (v = 0; v < deg; ++v)
	    if (selected & (1 << v)) {
	      tmp *= count[i][terms[j][v]];
	      tmp %= modulo;
	    }
	  sum[j][selected] += tmp;
	  sum[j][selected] %= modulo;
	}
      }
    }
      
    /* calculation */
    printf("Case #%d:", c);

    for (d = 1; d <= k; ++d) {
      ans = 0;
      for (j = 0; j < term_count; ++j) {
	memset(x, 0, MAX_DEG * sizeof(x[0]));
	for (deg = 0; (deg < 4) && (terms[j][deg] != -1); ++deg);
	while (1) {
	  available = (1 << deg) - 1; tmp = 1;
	  for (i = 0; i < d; ++i) {
	    selected = 0;
	    for (v = 0; v < deg; ++v)
	      if (x[v] == i)
		selected += (1 << v);
	    available = available & ~selected;
	    tmp *= sum[j][selected];
	    tmp %= modulo;
	  }
	  ans += tmp;
	  ans %= modulo;
	  
	  for (i = deg - 1; i >= 0 && (x[i] == d - 1); --i);
	  if (i >= 0) {
	    ++x[i];
	    for (++i; i < deg; ++i)
	      x[i] = 0;
	  }
	  else
	    break;
	}
      }
      printf(" %d", ans);
    }
    printf("\n", ans);
  }
  
  return 0;
}

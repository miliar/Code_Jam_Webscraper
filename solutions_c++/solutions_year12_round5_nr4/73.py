#include <cstdio>
#include <cassert>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;


int g[36][36], in[36], out[36], was[36], gg[36][36];

vector <int> to[26];

char s[10000];

int dfs (int v) {
  int res = out[v] != in[v];
  was[v] = 1;
  for (int i = 0; i < 36; i++) {
    if (!was[i] && gg[v][i]) {
      res |= dfs (i);
    }
  }
  return res;
}

int main (void) {
  int test_n;
  cin >> test_n;

  for (int i = 0; i < 26; i++) {
    to[i].push_back (i);
  }
  string x = "oieastbg",
         y = "01345789";
  for (int i = 0; i < (int)x.size(); i++) {
    to[x[i] - 'a'].push_back (y[i] - '0' + 26);
  }


  

  for (int test_id = 1; test_id <= test_n; test_id++) {
    printf ("Case #%d:", test_id);
    int k;
    scanf ("%d", &k);
    assert (k == 2);

    scanf ("%s", s);
    memset (g, 0, sizeof (g));
    memset (gg, 0, sizeof (gg));
    memset (in, 0, sizeof (in));
    memset (out, 0, sizeof (out));
    memset (was, 0, sizeof (was));
    int edges = 0;
    for (int i = 0; s[i] && s[i + 1]; i++) {
      int c1 = s[i] - 'a', c2 = s[i + 1] - 'a';
      for (int a = 0; a < (int)to[c1].size(); a++) {
        for (int b = 0; b < (int)to[c2].size(); b++) {
          int ca = to[c1][a], cb = to[c2][b];
          if (!g[ca][cb]) {
            g[ca][cb] = 1;

            gg[ca][cb] = 1;
            gg[cb][ca] = 1;
            
            out[ca]++;
            edges++;
            in[cb]++;
//            fprintf (stderr, "%d->%d\n", ca, cb);
          }
        }
      }
      
    }
    edges *= 2;
    for (int i = 0; i < 36; i++) {
      edges -= min (in[i], out[i]);
    }
    for (int i = 0; i < 36; i++) {
      if (!was[i] && out[i] && !dfs (i)) {
        edges++;
      }
    }
    printf (" %d\n", edges);
  }

  return 0;
}
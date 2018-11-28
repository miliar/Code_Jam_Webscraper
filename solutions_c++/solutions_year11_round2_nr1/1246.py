#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

const int nmax = 105;

int nt;
int adj[nmax][nmax];

struct TeamInfo {
  double wp;
  double owp;
  double oowp;
  double rri;
  int nwin;
  int np;
} ti[nmax];


double calculate_oowp(int t, int ta) {
  double oowp;

  return oowp;
}


double calculate_owp(int t, int ta) {
  if (adj[t][ta] == 1) {
    return (double)ti[ta].nwin / (double)(ti[ta].np - 1);
  } else {
    return (double)(ti[ta].nwin - 1) / (double)(ti[ta].np - 1);
  }
}


double calculate_rri(int t) {
  ti[t].rri = 0.25 * ti[t].wp + 0.50 * ti[t].owp + 0.25 * ti[t].oowp;

  return ti[t].rri;
}

int main(void) {
  int nc;

  freopen("A-large.in", "r", stdin);
  freopen("A.large.out", "w", stdout);

  scanf("%d", &nc);

  for (int c = 1; c <= nc; c++) {
    scanf("%d\n", &nt);

    memset(adj, -1, sizeof(adj));

    for (int i = 0; i < nt; ++i) {
      for (int j = 0; j < nt; ++j) {
        char ch;
        scanf(" %c", &ch);

        if (ch == '1') {
          adj[i][j] = 1;
        } else if (ch == '0') {
          adj[i][j] = 0;
        }
      }
    }

    for (int i = 0; i < nt; ++i) {
      double num = 0.0;
      double den = 0.0;

      ti[i].np = ti[i].nwin = 0;
      for (int j = 0; j < nt; ++j) {
        if (adj[i][j] == 0) {
          den = den + 1.0;
          ti[i].np++;
        } else if (adj[i][j] == 1){
          num = num + 1.0;
          den = den + 1.0;
          ti[i].np++;
          ti[i].nwin++;
        }
      }

      ti[i].wp = num / den;
    }

    for (int i = 0; i < nt; ++i) {
      double num = 0.0;
      double den = 0.0;

      for (int j = 0; j < nt; ++j) {
        if (adj[i][j] == 0 || adj[i][j] == 1) {
          num += calculate_owp(i, j);
          den = den + 1.0;
        }
      }

      ti[i].owp = num / den;
    }


    for (int i = 0; i < nt; ++i) {
      double num = 0.0;
      double den = 0.0;

      for (int j = 0; j < nt; ++j) {
        if (adj[i][j] == 0 || adj[i][j] == 1) {
          num += ti[j].owp;
          den = den + 1.0;
        }
      }

      ti[i].oowp = num / den;
    }

    for (int i = 0; i < nt; ++i) {
      calculate_rri(i);
    }

    printf("Case #%d:\n", c);
    for (int i = 0; i < nt; ++i) {
      printf("%f\n", ti[i].rri);
    }


  }

}
#include <algorithm>
#include <cstdio>
#include <vector>
#include <utility>

#include <glpk.h>

using namespace std;

const int N = 32*200;

double element[N];
int row[N];
int col[N];

int main() {
  int T; scanf("%d", &T);
  for(int t=1; t<=T; ++t) {
    int d, n; scanf("%d%d", &n, &d);
    vector<pair<int, int> > a(n);
    for(int i=0; i<n; ++i) {
      scanf("%d%d", &a[i].first, &a[i].second);
    }
    sort(a.begin(), a.end());

    glp_prob * lp = glp_create_prob();
    glp_add_rows(lp, 6*n - 1);
    glp_add_cols(lp, 1 + 2*n);

    glp_set_col_bnds(lp, 1, GLP_LO, 0., 0.);
    for(int i=2; i<=2*n+1; ++i) {
      glp_set_col_bnds(lp, i, GLP_FR, 0., 0.);
    }

    int m = 0;
    for(int i=0; i<n; ++i) {
      int r = 1+6*i;
      int v = 1+1+2*i;

      /* |left - start| <= t */
      element[m] = 1;
      row[m]     = r;
      col[m]     = v; ++m;
      element[m] = -1;
      row[m]     = r;
      col[m]     = 1; ++m;
      glp_set_row_bnds(lp, r, GLP_UP, 0., a[i].first);
      ++r;
      
      element[m] = -1;
      row[m]     = r;
      col[m]     = v; ++m;
      element[m] = -1;
      row[m]     = r;
      col[m]     = 1; ++m;
      glp_set_row_bnds(lp, r, GLP_UP, 0., -a[i].first);
      ++r;
      
      /* |right - start| <= t */
      element[m] = 1;
      row[m]     = r;
      col[m]     = v+1; ++m;
      element[m] = -1;
      row[m]     = r;
      col[m]     = 1; ++m;
      glp_set_row_bnds(lp, r, GLP_UP, 0., a[i].first);
      ++r;
      
      element[m] = -1;
      row[m]     = r;
      col[m]     = v+1; ++m;
      element[m] = -1;
      row[m]     = r;
      col[m]     = 1; ++m;
      glp_set_row_bnds(lp, r, GLP_UP, 0., -a[i].first);
      ++r;
      
      /* right - left >= (m - 1)*d */
      element[m] = 1;
      row[m]     = r;
      col[m]     = v; ++m;
      element[m] = -1;
      row[m]     = r;
      col[m]     = v+1; ++m;
      glp_set_row_bnds(lp, r, GLP_UP, 0., -d*(a[i].second-1));
      ++r;
      
      if (i+1 < n) {
	/* right + d <= next_left */
	element[m] = 1;
	row[m]     = r;
	col[m]     = v+1; ++m;
	element[m] = -1;
	row[m]     = r;
	col[m]     = v+2; ++m;
	glp_set_row_bnds(lp, r, GLP_UP, 0., -d);
	++r;
      }
    }

    glp_load_matrix(lp, m, row-1, col-1, element-1);

    glp_set_obj_dir(lp, GLP_MIN);
    glp_set_obj_coef(lp, 1, 1.);
    
    glp_smcp parm;
    glp_init_smcp(&parm);
    parm.msg_lev = GLP_MSG_OFF;
    glp_simplex(lp, &parm);

    double ans = glp_get_obj_val(lp);
    
    printf("Case #%d: %lf\n", t, ans);

    /*
    for(int i=0; i<n; ++i) {
      int v = 2+2*i;
      printf("left = %g, right = %g\n", glp_get_col_prim(lp, v), glp_get_col_prim(lp, v+1));
      }*/
    
    glp_delete_prob(lp);
  }
}

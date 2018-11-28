#include <algorithm>
#include <bitset>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <vector>
#include <glpk.h> // http://www.gnu.org/software/glpk/
using namespace std;
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORI(i,v) FOR(i,(int)v.size())
#define BEND(v) v.begin(),v.end()
#define dump(x) cerr << #x << " = " << (x) << endl;
typedef long long ll; typedef long double ld;

const int inf = 123456789;
int cas = 0;
int X[1024],Y[1024],Z[1024];
int P[1024];
int N;
void doit() {
  scanf("%d",&N);

  FOR(i,N) {
    scanf("%d%d%d%d",&X[i],&Y[i],&Z[i],&P[i]);
  }

  const size_t MAX_ASZ = 4*8*1024;
  size_t ASZ = 4*8*N;
  int ia[1+MAX_ASZ], ja[1+MAX_ASZ];
  double ar[1+MAX_ASZ];

  glp_prob *lp = glp_create_prob();
  glp_set_prob_name(lp, "C");
  glp_set_obj_dir(lp, GLP_MIN);

  glp_add_rows(lp, 8*N);

  int cur = 1;
  FOR(i,N) FOR(a,2) FOR(b,2) FOR(c,2) {
    int a1 = a?1:-1, b1 = b?1:-1, c1 = c?1:-1;

    char name[128];
    sprintf(name, "abs_%d_%d_%d_%d",i,a,b,c);
    glp_set_row_name(lp, cur, name);
    glp_set_row_bnds(lp, cur, GLP_LO,
      -a1*X[i]-b1*Y[i]-c1*Z[i], 0.0);

    ia[cur*4-3] = ia[cur*4-2] = ia[cur*4-1] = ia[cur*4] = cur;
    ja[cur*4-3] = 1;
    ja[cur*4-2] = 2;
    ja[cur*4-1] = 3;
    ja[cur*4] = 4;

    ar[cur*4-3] = P[i];
    ar[cur*4-2] = -a1;
    ar[cur*4-1] = -b1;
    ar[cur*4] = -c1;

    cur++;
  }

  glp_add_cols(lp,4);
  glp_set_col_name(lp, 1, "q");
  glp_set_col_name(lp, 2, "x");
  glp_set_col_name(lp, 3, "y");
  glp_set_col_name(lp, 4, "z");

  glp_set_col_bnds(lp, 1, GLP_LO, 0.0, 0.0);
  glp_set_col_bnds(lp, 2, GLP_FR, 0.0, 0.0);
  glp_set_col_bnds(lp, 3, GLP_FR, 0.0, 0.0);
  glp_set_col_bnds(lp, 4, GLP_FR, 0.0, 0.0);

  glp_set_obj_coef(lp, 1, 1.0);
  glp_set_obj_coef(lp, 2, 0.0);
  glp_set_obj_coef(lp, 3, 0.0);
  glp_set_obj_coef(lp, 4, 0.0);

  glp_load_matrix(lp, ASZ, ia, ja, ar);

  glp_smcp parm;
  glp_init_smcp(&parm);
  parm.msg_lev = GLP_MSG_OFF;
  assert(0 == glp_simplex(lp, &parm));

  int status = glp_get_status(lp);

  assert(status == GLP_OPT);

/*
  dump(glp_get_col_prim(lp,2));
  dump(glp_get_col_prim(lp,3));
  dump(glp_get_col_prim(lp,4));*/
  printf("Case #%d: %.6lf\n",++cas,glp_get_col_prim(lp,1));
  cerr << "ding" << endl;
}
int T;
int main() {
scanf("%d",&T);
FOR(i,T)doit();
}

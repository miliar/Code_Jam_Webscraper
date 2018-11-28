#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <math.h>
#include <string>
#include <set>
#include <ctype.h>
using namespace std;

#define all(V) (V).begin(),(V).end()
#define rall(V) (V).rbegin(),(V).rend()
#define _foreach(it, a, b) for (typeof(a) it = a; it != b; ++it)
#define foreach(x...) _foreach(x)
#define fu(a, b) foreach(a, 0, b)
#define MSET(a, b) memset(a, b, sizeof(a))

set<string> carac;
double prob[100000];
string car[100000];
int filho[100000][2];
int L, A, n, N;
char buf[200], buf2[200];
int pos;
string arv;

double faz(int no) {
  double resp = prob[no];
  if (filho[no][0] == -1)
    return resp;
  if (carac.count(car[no]))
    return resp*faz(filho[no][0]);
  return resp*faz(filho[no][1]);
}
void constroi() {
  while (arv[pos] != '(') pos++;
  pos++;
  int qtd;
  sscanf(arv.c_str() + pos, " %lf%n", &prob[N], &qtd);
  pos += qtd;
  while (arv[pos] == ' ') pos++;
  if (arv[pos] == ')') {
    filho[N][0] = filho[N][1] = -1;
    N++;
    pos++;
    return;
  }
  sscanf(arv.c_str() + pos, "%s%n", buf, &qtd);
  pos += qtd;
  car[N] = buf;
  int eu = N;
  N++;
  filho[eu][0] = N;
  constroi();
  filho[eu][1] = N;
  constroi();
  while (arv[pos] != ')') pos++;
  pos++;
  return;
}
int main() {
  int _42;
  gets(buf);
  sscanf(buf, "%d", &_42);
  for (int _41 = 0; _41 < _42; _41++) {
    printf("Case #%d:\n", _41+1);
    gets(buf);
    sscanf(buf,"%d", &L);
    arv = "";
    fu(i, L) {
      gets(buf);
      arv += " ";
      arv += buf;
    }
    pos = 0;
    N = 0;
    constroi();
    gets(buf);
    sscanf(buf, "%d", &A);
    fu(a, A) {
      gets(buf);
      sscanf(buf, " %*s %d%n", &n, &pos);
      carac.clear();
      fu(i, n) {
        int qtd;
        sscanf(buf + pos, " %s%n", buf2, &qtd);
        pos += qtd;
        carac.insert(buf2);
      }
      printf("%.7lf\n", faz(0));
    }
  }
  return 0;
}

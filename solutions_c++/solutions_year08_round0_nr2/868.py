#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int la[105];
int lb[105];
int aa[105];
int ab[105];
int n, na, nb;
int ta, tb;
int t;

void init()
{
  scanf(" %d", &t);
  scanf(" %d %d", &na, &nb);

  char *tmp1, *tmp2;
  tmp1 = new char[6];
  tmp2 = new char[6];
  
  for (int i = 0; i < na; ++i) {
    scanf(" %s %s", tmp1, tmp2);
    la[i] = (tmp1[0]-'0')*600+(tmp1[1]-'0')*60+(tmp1[3]-'0')*10+(tmp1[4]-'0');
    ab[i] = (tmp2[0]-'0')*600+(tmp2[1]-'0')*60+(tmp2[3]-'0')*10+(tmp2[4]-'0');
  }
  for (int i = 0; i < nb; ++i) {
    scanf(" %s %s", tmp1, tmp2);
    lb[i] = (tmp1[0]-'0')*600+(tmp1[1]-'0')*60+(tmp1[3]-'0')*10+(tmp1[4]-'0');
    aa[i] = (tmp2[0]-'0')*600+(tmp2[1]-'0')*60+(tmp2[3]-'0')*10+(tmp2[4]-'0');
  }
  ta = na;
  tb = nb;
}

void proc()
{
  int j;

  sort(la, la+na);
  sort(lb, lb+nb);
  sort(ab, ab+na);
  sort(aa, aa+nb);

  j = 0;
  for (int i = 0; i < na; ++i ) {
    if (j == nb) {break;}
    if (la[i] >= t+aa[j]) {
      --ta;
      ++j;
    }
  }
  j = 0;
  for (int i = 0; i < nb; ++i) {
    if (j == na) {break;}
    if (lb[i] >= t+ab[j]) {
      --tb;
      ++j;
    }
  }
}

void outp()
{
  printf(" %d %d\n", ta, tb);
}

int main()
{
  scanf(" %d", &n);
  for (int i = 0; i < n; ++i) {
    init();
    proc();
    printf("Case #%d:", i+1);
    outp();
  }
}

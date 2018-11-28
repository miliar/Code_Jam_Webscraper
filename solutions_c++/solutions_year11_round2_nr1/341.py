#include <cstdio>
#include <vector>

void solve()
{
  int N;
  scanf("%d", &N);
  std::vector<std::vector<int> > table(N, std::vector<int>(N));
  std::vector<int> wins(N), losses(N), total(N);
  std::vector<double> wp(N), owp(N), oowp(N);
  for(int i=0; i<N; ++i) {
    for(int j=0; j<N; ++j) {
      char c;
      scanf(" %c", &c);
      switch(c) {
      case '0':
	table[i][j] = 0;
	++losses[i];
	++total[i];
	break;
      case '1':
	table[i][j] = 1;
	++wins[i];
	++total[i];
	break;
      case '.':
	table[i][j] = -1;
      }
    }
    wp[i] = (double)wins[i]/(double)total[i];
  }
  for(int i=0; i<N; ++i) {
    for(int j=0; j<N; ++j) {
      if(table[i][j] == 1)
	owp[i] += (double)wins[j]/(double)(total[j]-1);
      else if(table[i][j] == 0)
	owp[i] += (double)(wins[j]-1)/(double)(total[j]-1);
    }
    owp[i] /= total[i];
  }
  for(int i=0; i<N; ++i) {
    for(int j=0; j<N; ++j) {
      if(table[i][j] >= 0)
	oowp[i] += owp[j];
    }
    oowp[i] /= total[i];
  }
  for(int i=0; i<N; ++i) {
    printf("%.12lf\n", .25*wp[i] + .50*owp[i] + .25*oowp[i]);
  }
}

int main()
{
  int T;
  scanf("%d", &T);
  for(int Ts=1; Ts<=T; ++Ts) {
    printf("Case #%d:\n", Ts);
    solve();
  }
  return 0;
}

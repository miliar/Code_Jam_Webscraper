#include<cstdio>
#include<vector>

using namespace std;

char matrix[200][200];

int main() {
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int N;
    scanf("%d", &N);
    for(int i = 0; i < N; i++)
      scanf("%s", matrix[i]);

    vector<double> WP(N, 0), OWP(N, 0), OOWP(N, 0), opp(N, 0);
    for(int i = 0; i < N; i++)
      for(int j = 0; j < N; j++)
        if(matrix[i][j] != '.')
          opp[i]++;

    for(int i = 0; i < N; i++)
      for(int j = 0; j < N; j++)
        if(matrix[i][j] == '1')
          WP[i]+=1/opp[i];

    for(int i = 0; i < N; i++)
      for(int j = 0; j < N; j++)
        if(matrix[i][j] == '1')
          OWP[i]+=(WP[j]*opp[j]/(opp[j]-1))/opp[i];
        else if(matrix[i][j] == '0')
          OWP[i]+=((WP[j]*opp[j]-1)/(opp[j]-1))/opp[i];

    for(int i = 0; i < N; i++)
      for(int j = 0; j < N; j++)
        if(matrix[i][j] != '.')
          OOWP[i]+=OWP[j]/opp[i];

    printf("Case #%d:\n", t);
    for(int i = 0; i < N; i++)
      printf("%.12lf\n", 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]);
  }
}

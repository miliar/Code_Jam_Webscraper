#include <cstdio>
#include <cstdlib>
#include <stack>
#include <map>
using namespace std;


int main(int argc, const char *argv[])
{
  int T; //Number of cases

  scanf("%d\n", &T);

  for (int i = 0; i < T; i++) {
    double result[100];
    int N = 0;        //Number of team
    int table[100][100];

    scanf("%d\n", &N);

    for (int j = 0; j < N; j++) {
      for (int k = 0; k < N; k++) {
        char r_char;
        scanf("%c", &r_char);
        if (r_char == '.') {
          table[j][k] = -1;
        } else if (r_char == '0') {
          table[j][k] = 0;
        } else if (r_char == '1') {
          table[j][k] = 1;
        }
      }
      result[j] = 0;
      scanf("\n");
    }
    
    double WP[100];
    double OWP[100];
    double OOWP[100];
    int totalWin[100];
    int totalMatch[100];
    for (int j = 0; j < N; j++) {
      totalWin[j] = 0;
      totalMatch[j] = 0;
      WP[j] = 0;
      for (int k = 0; k < N; k++) {
        if (table[j][k] >= 0) {
          totalMatch[j]++;
          totalWin[j]+=table[j][k];
        }
      }
      WP[j] = totalMatch[j]==0?0: 1.0 *totalWin[j] / totalMatch[j];
    fprintf(stderr, "WP[%d] %d / %d = %f\n", j, totalWin[j], totalMatch[j], WP[j]);
    }

    for (int k = 0; k < N; k++) {
      double TotalOWP = 0;
      for (int j = 0; j < N; j++) {
        if (table[j][k] != -1) {
          TotalOWP += (1.0 * totalWin[j]-table[j][k]) / (totalMatch[j]-1);
        }
      }
      OWP[k] = (totalMatch[k] == 0)?0:TotalOWP / totalMatch[k];
      fprintf(stderr, "OWP::%f / %d = %f\n", TotalOWP, totalMatch[k], OWP[k]);
    }

    for (int j = 0; j < N; j++) {
      double TotalOOWP = 0;
      int TotalMatch = 0;
      for (int k = 0; k < N; k++) {
        if ((j != k) && (table[j][k] != -1)) {
          TotalMatch++;
          TotalOOWP += OWP[k];
      fprintf(stderr, "Add OWP[%d]:= %f\n", k, OWP[k]);
        }
      }
      OOWP[j] = TotalOOWP / TotalMatch;
      fprintf(stderr, "OOWP::%f / %d = %f\n", TotalOOWP, N-1, OOWP[j]);
    }

    printf("Case #%d:\n", i+1);
    for (int j = 0; j < N; j++) {
      result[j] = 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j];
    fprintf(stderr, "%f %f %f\n", WP[j], OWP[j], OOWP[j]);
      printf("%f\n", result[j]);
    }
  }

  return 0;
}

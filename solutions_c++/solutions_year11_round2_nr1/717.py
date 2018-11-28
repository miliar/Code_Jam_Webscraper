#include <cstdio>
#include <cstring>

using namespace std;

#define SZ(a) int((a).size())

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

int N;
char B[104][104];

//RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
int wins[104];
int games[104];
double WP[104];
double OWP[104];
double OOWP[104];

int main(int argc, char* argv[]) {
   int TC;
   scanf("%d", &TC);
   for (int tc = 1; tc <= TC; ++tc) {
      printf("Case #%d:\n", tc);
      scanf("%d", &N);
      for (int i = 0; i < N; ++i)
         scanf("%s", B[i]);
      memset(games, 0, sizeof(games));
      memset(wins, 0, sizeof(wins));

//      fprintf(stderr, "WP\n");
      for (int i = 0; i < N; ++i) {
         for (int j = 0; j < N; ++j) {
            if (i == j || B[i][j] == '.') continue;
            ++games[i];
            if (B[i][j] == '1') ++wins[i];
         }
         WP[i] = wins[i] * 1.0 / games[i];
//         fprintf(stderr, "%d: %.3lf\n", i, WP[i]);
      }
//      fprintf(stderr, "\n");

//      fprintf(stderr, "OWP\n");
      for (int i = 0; i < N; ++i) {
         int nopps = 0;
         OWP[i] = 0.0;
         for (int j = 0; j < N; ++j) {
            if (i == j || B[j][i] == '.') continue;
            ++nopps;
            double d = (wins[j] - (B[j][i]-'0')) * 1.0 / (games[j]-1);
/*
            if (i == 3)
               fprintf(stderr, "###  %d %d %d  %.3lf\n", j, wins[j], games[j], d);
*/
            OWP[i] += d;
         }
         OWP[i] /= nopps;
//         fprintf(stderr, "%d: %.3lf %d\n", i, OWP[i], nopps);
      }
//      fprintf(stderr, "\n");

      for (int i = 0; i < N; ++i) {
         int nopps = 0;
         OOWP[i] = 0.0;
         for (int j = 0; j < N; ++j) {
            if (i == j || B[j][i] == '.') continue;
            ++nopps;
/*
            if (i == 0)
               fprintf(stderr, "###  %d %.3lf\n", j, OWP[j]);
*/
            OOWP[i] += OWP[j];
         }
         OOWP[i] /= nopps;
      //   fprintf(stderr, "%d: %.3lf\n", i, OOWP[i]);
      }

      for (int i = 0; i < N; ++i) {
         double rpi = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
         printf("%.10lf\n", rpi);
      }

   }
   return 0;
}

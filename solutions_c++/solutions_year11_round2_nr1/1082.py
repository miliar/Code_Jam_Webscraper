#include <cstdio>
#include <cstring>

#define MAX 110
int teams;

struct team {
  int against[MAX];
  int victory[MAX];
  int tot,victories;
  double wp, owp_value,oowp_value;
  double calc_wp(int without) {
    int t_vict = 0;
    int t_games = 0;
    for (int i = 0 ; i < teams ; i++) {
      if (against[i] == 1 && i != without) {
	t_games++;
	t_vict += victory[i];
      }
    }
    return ((double)t_vict*1.0)/t_games;
  }
  void calc_wp() {
    wp = calc_wp(-1);
  }
 
}times[MAX];
void calc_owp(int me) {
    int tot_elements = 0;
    double calc = 0;
    for (int i = 0 ; i < teams ; i++) {
      if (times[me].against[i] == 1) {
	tot_elements++;
	calc += times[i].calc_wp(me);
      }
    }
    times[me].owp_value = calc/(double)tot_elements;
}
void calc_oowp(int me) {
  int tot_elements = 0;
    double calc = 0;
    for (int i = 0 ; i < teams ; i++) {
      if (times[me].against[i] == 1) {
	tot_elements++;
	calc += times[i].owp_value;
      }
    }
    times[me].oowp_value = calc/(double)tot_elements;
}
int main() {
  int n_tests;
  char aux_read[1<<20];
  scanf("%d",&n_tests);
  for (int t = 1 ; t <= n_tests; t++) {
    
    scanf("%d",&teams);
    for (int i = 0 ; i < teams ; i++) {
      scanf("%s",aux_read);
      times[i].tot = times[i].victories = 0;
      for (int j = 0 ; j < teams ; j++) {
	if (aux_read[j] == '.') {
	  times[i].against[j] = 0;
	  continue;
	}
	times[i].against[ j] = 1;
	times[i].victory[ j ] = aux_read[j] -'0';
	times[i].victories +=  times[i].victory[ j ];
	times[i].tot += 1;
      }
      times[i].against[ i ] = -1;
      times[i].calc_wp();
    }
    for (int i = 0 ; i < teams ; i++)
      calc_owp(i);
    for (int i = 0 ; i < teams ; i++)
      calc_oowp(i);
    printf("Case #%d:\n",t);
    for (int i = 0 ; i <teams ; i++)
      printf("%.10f\n",0.25*times[i].wp + 0.5*times[i].owp_value + 0.25*times[i].oowp_value);
  }
  return 0;
}

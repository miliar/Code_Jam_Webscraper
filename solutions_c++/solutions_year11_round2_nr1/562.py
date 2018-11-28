#include <cstdio>
#include <cstring>

using namespace std;

int G[111][111];
int n;
double wp[111];
double owp[111];
double oowp[111];

void calcWP(){
  for (int i = 0; i < n; i++){
    int win = 0;
    int gam = 0;
    for (int j = 0; j < n; j++){
      if (G[i][j] == 0) continue;
      if (G[i][j] > 0)
	win++;
      gam++;
    }
    wp[i] = ( (double) win)/gam;
    //printf("wp %d %f\n", i, wp[i]);
  }
}

void calcOWP(){
  for (int i = 0; i < n; i++){
    int op = 0;
    double sowp = 0;
    for (int j = 0; j < n; j++){
      if (G[i][j] == 0) continue;
      op++;
      int win = 0;
      int gam = 0;
      for (int k = 0; k < n; k++){
	if (k == i) continue;
	if (G[j][k] == 0) continue;
	if (G[j][k] > 0)
	  win++;
	gam++;
      }
      sowp += ((double)win)/gam;
    }
    owp[i] = sowp/op;
    //printf("owp %d %f (%f/%d)\n", i, owp[i], sowp, op);
  }
}

void calcOOWP(){
  for (int i = 0; i < n; i++){
    int op = 0;
    double sum = 0;
    for (int j = 0; j < n; j++){
      if (G[i][j] == 0) continue;
      sum += owp[j];
      op++;
    }
    oowp[i] = sum/op;
    //printf("oowp %d %f\n", i, oowp[i]);

  }
}

double rpi(int i){
  return (0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i]);
}

int main(){
  int t;
  scanf("%d", &t);
  for (int ka = 1; ka <= t; ka++){
    scanf("%d", &n);
    memset(G, 0, sizeof(G));
    for (int i = 0; i < n; i++){
      char buf[111];
      scanf("%s", buf);
      for (int j = i+1; j < n; j++){
	if (buf[j] == '1'){
	  G[i][j] = 1;
	  G[j][i] = -1;
	}
	else if (buf[j] == '0'){
	  G[i][j] = -1;
	  G[j][i] = 1;
	}
      }
    }
    calcWP();
    calcOWP();
    calcOOWP();

    printf("Case #%d:\n", ka);
    for (int i = 0; i < n; i++){
      printf("%.11lf\n", rpi(i));
    }
  }

  return 0;
}

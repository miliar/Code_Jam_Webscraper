#include "utils.h"

vector<int> t_x;
vector<int> t_y;
int num_ts;
unsigned long long int A, B, C, D, x_0, y_0, M;

void RunTCase(int n) {
  unsigned long long int result = 0;
  for(int i = 0; i < num_ts - 2; i++) {
    for(int j = i + 1; j < num_ts - 1; j++) {
      for(int k = j + 1; k < num_ts; k++) {
	if ((((t_x[i] + t_x[j] + t_x[k]) % 3) == 0) &&
	    (((t_y[i] + t_y[j] + t_y[k]) % 3) == 0)) {
	  result++;
	}
      }
    }
  }
  printf("Case #%d: %lld\n", n, result); 
}

void GetInputs() {
  fscanf(ifile, "%d", &N);
  for(int i = 0; i < N; i++) {
    t_x = vector<int>();
    t_y = vector<int>();

    fscanf(ifile, "%d %lld %lld %lld %lld %lld %lld %lld", &num_ts, &A, &B, &C, &D, &x_0, &y_0, &M);
    t_x.PB(x_0);
    t_y.PB(y_0);
    for(int j = 1; j <= num_ts - 1; j++) {
      x_0 = (A * x_0 + B) % M;
      y_0 = (C * y_0 + D) % M;
      t_x.PB(x_0);
      t_y.PB(y_0);
    }

    RunTCase(i + 1);
  }
}

int main(int argc, char **argv) {
  GetOptions(argc, argv);
  GetInputs();

  fclose(ifile);
}

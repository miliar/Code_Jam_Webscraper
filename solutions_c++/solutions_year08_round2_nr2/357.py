#include "utils.h"

unsigned long long A, B, P;
vector<int> sm;
vector<unsigned long long> ps_orig;
vector<unsigned long long> ps;
vector<vector<int> > smps;
unsigned long long int sms;

void gen_ps_orig() {
  vector<int> v;
  for(int i = 0; i < 1000001; i++) {
    v.PB(1);
  }
  for(int i = 2; i < 1000001; i++) {
    for(int j = 2 * i; j < 1000001; j += i) {
      v[j] = 0;
    }
  }
  for(uint i = 2; i < 1000001; i++) {
    if (v[i])
      ps_orig.PB(i);
  }
  
  //  for(uint i = 0; i < ps.SZ; i++)
  //    printf("%d.\n", ps[i]);
}

void gen_ps() {
  ps = vector<unsigned long long>();
  for(uint i = 0; i < ps_orig.SZ; i++) {
    if (ps_orig[i] >= P)
      ps.PB(ps_orig[i]);
  }

  //  for(uint i = 0; i < ps.SZ; i++)
  //    printf("%lld.\n", ps[i]);
}

void gen_smps() {
  for(unsigned long long i = A; i <= B; i++) {
    smps.PB(vector<int>());
    for(uint j = 0; j < ps.SZ; j++) {
      if ((i % ps[j]) == 0)
	smps[smps.SZ - 1].PB(ps[j]);
    }
  }
  //  for(uint i = 0; i < smps.SZ; i++)
  //    for(uint j = 0; j < smps[i].SZ; j++)
  //      printf("smps[%d][%d] = %d.\n", i, j, smps[i][j]);

}

int is_common(uint i, uint j) {
  for(uint x = 0; x < smps[i].SZ; x++) {
    for(uint y = 0; y < smps[j].SZ; y++) {
      if (smps[i][x] == smps[j][y])
	return 1;
    }
  }
  return 0;
}

void RunTCase(int n) {
  sm = vector<int>();
  smps = vector<vector<int> >();
  sms = B - A + 1;
  int result = sms;

  for(uint i = 0; i < sms; i++)
    sm.PB(i);

  gen_smps();

  for(unsigned long long i = 0; i < sms - 1; i++) {
    for(unsigned long long j = i + 1; j < sms; j++) {
      if (is_common(i, j)) {
	if (sm[i] != sm[j]) {
	  result--;

	  int tj = sm[j];
	  int ti = sm[i];
	  
	  for(uint k = 0; k < sms; k++) {
	    if (sm[k] == tj) {
	      sm[k] = ti;
	    }
	  }
	}
      }
    }
  }
  printf("Case #%d: %d\n", n, result); 
}

void GetInputs() {
  gen_ps_orig();

  fscanf(ifile, "%d", &N);
  for(int i = 0; i < N; i++) {
    fscanf(ifile, "%lld %lld %lld", &A, &B, &P);
    gen_ps();
    RunTCase(i + 1);
  }
}

int main(int argc, char **argv) {
  GetOptions(argc, argv);
  GetInputs();

  fclose(ifile);
}

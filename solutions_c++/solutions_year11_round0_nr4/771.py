#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstring>

using namespace std;

int main(int argc, char *argv[]) {
  if(argc < 3)
    return 0;

  ifstream ifs(argv[1]);
  ofstream ofs(argv[2]);

  int num_cases;
  ifs >> num_cases;
  for(int i=1;i<=num_cases;i++){
    ofs << "Case #" << i << ": ";

    int n;
    ifs >> n;
    int numbers[1000];
    bool flags[1000];
    for(int k=0;k<n;k++) {
      ifs >> numbers[k];
      flags[k] = true;
    }

    int num_cycles[1000];
    memset(num_cycles, 0, sizeof(int) * 1000);
    for(int k=0;k<n;k++) {
      int c = k;
      if(flags[k]) {
	int cycle = 1;
	flags[c] = false;
	while(flags[numbers[c]-1]) {
	  c = numbers[c]-1;
	  flags[c] = false;
	  cycle++;
	}
	num_cycles[cycle - 1]++;
      }
    }

    double total = 0;
    for(int c=1;c<1000;c++){
      total += (double)num_cycles[c] * (c + 1);
    }
    ofs.setf(std::ios_base::fixed, std::ios_base::floatfield);
    ofs << setprecision(6) << total << endl;
  }

  ifs.close();
  ofs.close();

  return 0;
}

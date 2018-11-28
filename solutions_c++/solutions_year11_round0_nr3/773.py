// in this program, I assume that character code is ascii (or compatible to ascii),
// and that the values of 'A' to 'Z' are continuous. 

#include <iostream>
#include <fstream>
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

    unsigned long c_min, c_patrick_sum, c_sum;
    c_min = 0;
    c_patrick_sum = 0;
    c_sum = 0;
    for(int k=0;k<n;k++){
      unsigned long c;
      ifs >> c;

      if(k == 0 || c < c_min)
	c_min = c;

      c_patrick_sum ^= c;
      c_sum += c;
    }

    if(c_patrick_sum == 0)
      ofs << (c_sum - c_min);
    else
      ofs << "NO";
    ofs << endl;
  }

  ifs.close();
  ofs.close();

  return 0;
}

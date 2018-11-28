#include <iostream>
#include <fstream>
#include <cmath>

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
    long long int N;
    ifs >> N;

    long long int pd, pg;
    ifs >> pd;
    ifs >> pg;

    bool f = false;
    for(int d=1;d<=N;d++) {
      if((pd * d) % 100 == 0){
	f = true;
	break;
      }
    }

    if(pg == 100 && pd != 100)
      f = false;
    if(pg == 0 && pd != 0)
      f = false;

    if(f)
      ofs << "Possible" << endl;
    else
      ofs << "Broken" << endl;
  }

  ifs.close();
  ofs.close();

  return 0;
}

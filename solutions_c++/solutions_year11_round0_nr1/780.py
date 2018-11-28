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
    int n;
    ifs >> n;

    int bt, bp, ot, op;
    bt = ot = 0;
    bp = op = 1;

    for(int k=0;k<n;k++){
      char c;
      int p;
      ifs >> c;
      ifs >> p;
      if(c == 'B') {
	bt += abs(p - bp);
	if(bt < ot)
	  bt = ot;
	bt++;
	bp = p;
      }
      else if(c == 'O') {
	ot += abs(p - op);
	if(ot < bt)
	  ot = bt;
	ot++;
	op = p;
      }
      else{
	cout << "error" << endl;
	return 0;
      }
    }
    ofs << max(ot, bt) << endl;
  }

  ifs.close();
  ofs.close();

  return 0;
}

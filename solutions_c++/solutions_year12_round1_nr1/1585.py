#include <iostream>
#include <fstream>
using namespace std;

int main(){

  ifstream fin;
  fin.open("A-small-attempt0.in");
  ofstream fout;
  fout.open("A-small-submit.out");

  int nCase;
  fin >> nCase;

  for (int i = 1; i <= nCase; i++){
    int a,b,n;
    fin >> a >> b;

    fout << "Case #" << i << ": " << n << endl;
    cout << "Case #" << i << ": " << n << endl;
  }

  fin.close();
  fout.close();
  return 0;
}

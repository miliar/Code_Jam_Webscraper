#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <queue>
#include <algorithm>
#include <fstream>
#include <cmath>

#define For(i,n) for(int i=0;i<(n);i++)
#define For1(i,n) for(int i=1;i<=(n);i++)
#define ll long long
#define clear(d) memset(d,0,sizeof(d))
#define INF 2000000000

using namespace std;

int main(int argc, char** argv){
  fstream fin(argv[1], ios::in);
  fstream fout("./result.out", ios::out);
  int CN;
  fin >> CN;
  For1(CI,CN){
    long long N;
    int PD, PG;
    fin >> N >> PD >> PG;
    int t=100;
    int p=PD;
    int pp;

    if (PG == 100) {
      if (PD != 100) {
        //No
        cout << "Case #" << CI << ": Broken" << endl;
        fout << "Case #" << CI << ": Broken" << endl;
      }
      else {
        //Yes
        cout << "Case #" << CI << ": Possible" << endl;
        fout << "Case #" << CI << ": Possible" << endl;
      }
      continue;
    }

    if (PG == 0) {
      if (PD != 0) {
        //No
        cout << "Case #" << CI << ": Broken" << endl;
        fout << "Case #" << CI << ": Broken" << endl;
      }
      else {
        //Yes
        cout << "Case #" << CI << ": Possible" << endl;
        fout << "Case #" << CI << ": Possible" << endl;
      }
      continue;
    }

    if (PD == 100) {
      if (PG == 0) {
        //No
        cout << "Case #" << CI << ": Broken" << endl;
        fout << "Case #" << CI << ": Broken" << endl;
      }
      else {
        //Yes
        cout << "Case #" << CI << ": Possible" << endl;
        fout << "Case #" << CI << ": Possible" << endl;
      }
      continue;
    }

    if (PD == 0) {
      if (PG == 100) {
        //No
        cout << "Case #" << CI << ": Broken" << endl;
        fout << "Case #" << CI << ": Broken" << endl;
      }
      else {
        //Yes
        cout << "Case #" << CI << ": Possible" << endl;
        fout << "Case #" << CI << ": Possible" << endl;
      }
      continue;
    }

    while(p){
      pp = p;
      p = t % p;
      t = pp;
    }
    int n = 100/pp;
    if (n <= N) {
      cout << "Case #" << CI << ": Possible" << endl;
      fout << "Case #" << CI << ": Possible" << endl;
    }
    else {
      cout << "Case #" << CI << ": Broken" << endl;
      fout << "Case #" << CI << ": Broken" << endl;
    }

  }
  fin.close();
  fout.close();
}

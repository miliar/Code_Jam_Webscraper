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
    int n;
    int x;
    int tot = 0;
    int totx = 0;
    int mi = 1000000;
    fin >> n;
    For(i,n){
      fin >> x;
      tot += x;
      totx ^= x;
      mi = min(x, mi);
    }
    if (totx){
      cout << "Case #" << CI << ": " << "NO" << endl;
      fout << "Case #" << CI << ": " << "NO" << endl;
    }
    else{
      int res = tot - mi;
      cout << "Case #" << CI << ": " << res << endl;
      fout << "Case #" << CI << ": " << res << endl;
    }
  }
  fin.close();
  fout.close();
}

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;



int T;
int n;



long long  v1[1000];
long long  v2[1000];	  

int main() {
  string name;
  cin >> name;
  ifstream fin(name.c_str());
  ofstream fout("result.txt");
  fin >> T;
  for (int i = 0; i < T; i++) {
    fout << "Case #" << i + 1 << ": ";
    // cout << "Case #" << i + 1 << ": ";
    fin >> n;
    cout << n << endl;
    for (int j = 0; j < n; j++)
      fin >> v1[j];
    for (int j = 0; j < n; j++)
      fin >> v2[j];

    sort(v1,v1+n);
    sort(v2,v2+n);
    long long  result = 0;
    for (int j = 0; j < n; j++)
      result += v1[j] * v2[n-j - 1];
    fout << result << endl;
  }
  return 0;
}

#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<queue>
#include<set>
#include<map>
#include<list>
#include<algorithm>
#include<cmath>
#include<cstdio>
#include<functional>
using namespace std;
typedef long long LLI;
typedef long double LD;


int main() {
  int NT;
  cin >> NT;
  for (int test=1;test<=NT;test++) {
    int n,m;
    cin >> n >> m;
    vector<vector<char> > A(n, vector<char>(m));
    for (int i=0;i<n;i++) {
      for (int j=0;j<m;j++) {
	cin >> A[i][j];
      }
    }
    for (int i=0;i<n-1;i++) {
      for (int j=0;j<m-1;j++) {
	if (A[i][j] == '#') {
	  A[i][j]+='/' - '#';
	  A[i+1][j]+='\\' - '#';
          A[i][j+1]+='\\' - '#';
	  A[i+1][j+1]+='/' - '#';
	}
      }
    }
    bool is_impos = false;
    for (int i=0;i<n;i++)
      for (int j=0;j<m;j++) 
	if (A[i][j] != '.' && A[i][j] !='/' && A[i][j] != '\\')
	  is_impos = true;
    cout << "Case #" << test << ":" << endl;
    if (is_impos) {
      cout << "Impossible" << endl;
      continue;
    }
    for (int i=0;i<n;i++) {
      for (int j=0;j<m;j++) {
	cout << A[i][j];
      }
      cout << endl;
    }
  }
  return 0;
}

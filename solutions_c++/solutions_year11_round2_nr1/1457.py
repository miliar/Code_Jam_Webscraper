#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <string> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <ctime> 
 
using namespace std; 
 
int main () { 
  int t, T; 

  cin >> T; 
  for (t = 1; t <= T; t++) {
    int N; cin >> N;
    int a[N][N];
    for (int i = 0; i < N; i++)
      for (int j = 0; j < N; j++) {
	char c; cin >> c;
	a[i][j] = c - '0';
      }
    double RPI[N], WP[N], OWP[N], OOWP[N];
    for (int i = 0; i < N; i++) {
      double c = 0; int n = 0;
      for (int j = 0; j < N; j++) {
	if (a[i][j] == 1) c++;
	if (a[i][j] == 0 || a[i][j] == 1) n++;
      }
      WP[i] = c/n;
    }
    for (int i = 0; i < N; i++) {
      double c = 0; int nn = 0;
      for (int j = 0; j < N; j++) {
	if (i == j || (a[i][j] != 0 && a[i][j] != 1)) { nn++; continue; }
	double s = 0; int n = 0;
	for (int k = 0; k < N; k++) {
	  if (k != i && a[j][k] == 1) s++;
	  if (k!= i && (a[j][k] == 1 || a[j][k] == 0)) n++;
	}
	s /= n;
	c += s;
      }
      OWP[i] = c/(N-nn);
    }
    for (int i = 0; i < N; i++) {
      double s = 0; int nn = 0;
      for (int j = 0; j < N; j++)
	if (a[i][j] == 0 || a[i][j] == 1) { s += OWP[j]; nn++; }
      OOWP[i] = s/nn;
    }
    cout << "Case #" << t << ":" << endl;
    for (int i = 0; i < N; i++) {
      RPI[i] = 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i];
      cout << RPI[i] << endl;
    }
  }
  return 0; 
}

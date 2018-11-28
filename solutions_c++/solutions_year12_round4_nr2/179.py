/*
ID: Plagapong
LANG: C++
TASK: aerobics
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<cmath>
#define INF 999999999

using namespace std;
int garbage;
int n;
double w,h;
double diag;
int r[1005];
double loc[1005][2];
int ind[1005];

void preprocess() {
  // Preprocess
  
}

void clearVars() {
  // Clear variables
  
}

bool comparez (int i,int j) {
  return (r[i] < r[j]);
}

void process() {
  // Code here!
  garbage = scanf("%d %lf %lf", &n, &w, &h);
  diag = sqrt(w*w+h*h);
  for (int i = 0; i < n; i++) {
    garbage = scanf("%d", &r[i]);
    ind[i] = i;
  }
  sort(ind, ind+n, comparez);
  int sumr = 0;
  loc[ind[0]][0] = loc[ind[0]][1] = 0;
  for (int i = 1; i < n; i++) {
    sumr = sumr + r[ind[i-1]] + r[ind[i]];
    loc[ind[i]][0] = w * sumr / diag + 0.0001 * i;
    loc[ind[i]][1] = h * sumr / diag + 0.0001 * i;
    if(loc[ind[i]][0] > w || loc[ind[i]][1] > h) {
      loc[ind[i]][0] = 0;
      loc[ind[i]][1] = h - 0.0001;
    }
  }
  for (int i = 0; i < n; i++) {
    printf("%lf %lf", loc[i][0], loc[i][1]);
    if (i != n-1) printf(" ");
  }
}

int main() {
  preprocess();
  int times;
  cin >> times;
  for (int i = 1; i <= times; i++) {
	cout << "Case #" << i << ": ";
	clearVars();
	process();
	cout << endl;
  }
  return 0;
}

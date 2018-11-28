/*
ID: Plagapong
LANG: C++
TASK: A
*/

#include<iostream>
#include<fstream>
#include<algorithm>
#define INF 999999999

using namespace std;
ifstream fin;
ofstream fout;

int x, s, r, n;
double t;
struct Runway {
  int l, w;
  double g, lim;
} a[1004];

bool comparez(const Runway &x, const Runway &y) {
  return x.g > y.g;
}

void clearVars() {
  // Clear variables
  
}

void process() {
  // Code here!
  int bb, ee;
  fin >> x >> s >> r >> t >> n;
  a[n].l = x; a[n].w = 0;
  for (int i = 0; i < n; i++) {
	fin >> bb >> ee >> a[i].w;
	a[i].l = ee - bb;
	a[n].l -= a[i].l;
  }
  n++;
  for (int i = 0; i < n; i++) {
	a[i].g = (double) (r + a[i].w) / (double) (s + a[i].w);
	a[i].lim = (double) a[i].l / (double) (r + a[i].w);
  }
  sort(a, a + n, comparez);
  double ans = 0;
  for (int i = 0; i < n; i++) {
	double hr, hw;
	if (t >= a[i].lim) {
	  hr = a[i].lim; hw = 0; t -= a[i].lim;
	} else {
	  hr = t; hw = (double) (a[i].l - t * (r + a[i].w)) / (s + a[i].w);
	  t = 0;
	}
	ans += (hr + hw);
  }
  cout.precision(9);
  fout << fixed << ans;
}

int main(int argc, const char* argv[]) {
  if (argc != 3) {
	cout << "Please indicate input and output" << endl;
	exit(0);
  }
  fin.open(argv[1]);
  fout.open(argv[2]);
  int times;
  fin >> times;
  for (int i = 1; i <= times; i++) {
	fout << "Case #" << i << ": ";
	clearVars();
	process();
	fout << endl;
  }
  fin.close();
  fout.close();
  return 0;
}

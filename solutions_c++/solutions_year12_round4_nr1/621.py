#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <map>
#include <list>
using namespace std;

ifstream fin ("A-large.in");
ofstream fout ("A-large.out");

void solve() {
   int n, x;
   fin >> n;
   vector<int> d(n), l(n), lm(n);
   for(int i=0; i<n; i++) {
      fin >> d[i] >> l[i];
      lm[i] = -1;
   }
   fin >> x;
   lm[0] = min(l[0], d[0]);
   for(int i=0; i<n; i++) {
      if( d[i]+lm[i]>=x ) {
         fout << "YES" << endl;
         return;
      }

      int j = i+1;
      while( j<n && d[i]+lm[i]>=d[j] ) {
         lm[j] = max(lm[j], min(l[j], min(d[j]-d[i], l[i])));
         j++;
      }
   }
   fout << "NO" << endl;
}

int main() {
   int N, N2 = 1;
	fin >> N;
	while( N2<=N ) {
      fout << "Case #" << N2++ << ": ";
      solve();
      cout << N2 << endl;
   }

	return 0;
}
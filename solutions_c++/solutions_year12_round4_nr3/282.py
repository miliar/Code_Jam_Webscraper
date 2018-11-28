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

ifstream fin ("C-small-attempt2.in");
ofstream fout ("C-small-attempt2.out");
int x[2048], l[2048];

void solve() {
   int n;
   fin >> n;
   memset(x, 0, sizeof(x));
   memset(l, 0, sizeof(l));
   for(int i=0; i<n-1; i++) {
      fin >> x[i];
      x[i]--;
   }
   
   // check imp
   bool imp = 0;
   for(int i=0; !imp && i<n-1; i++){
      for(int j=i+1; !imp && j<x[i]; j++)
         if( x[j]>x[i] ) imp = 1;
   }

   if( imp ) {
      fout << "Impossible\n";
      return;
   }

   l[n-1] = 1000000000;
   l[n] = l[n-1] + 1;
   x[n-1] = n;
   for(int i=n-1; i>=0; i--) {
      int j=0;
      while( j<i && x[j]!=i )
         j++;
      //int len = l[i] - (i-j);
      //int len = (i-j) * (l[x[i]] - l[i]) / (x[i]-i);
      int diff = i-j;
      if( l[x[i]]!=l[i] ) diff *= (l[x[i]] - l[i]);
      diff = ceil(double(diff) / double (x[i]-i));
      for(;j<i; j++)
         if( x[j]==i )
            l[j] = l[i] - diff;
   }

   for(int i=0; i<n; i++)
      fout << l[i] << " ";
   fout << endl;
}

int main() {
   int N, N2 = 1;
	fin >> N;
	while( N2<=N ) {
      fout << "Case #" << N2++ << ": ";
      solve();
   }

	return 0;
}
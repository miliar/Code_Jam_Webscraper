#include <cstdio>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <algorithm>
using namespace std;

int n;
vector<string> x;

int gcd(int a, int b) { return !b ? a : gcd(b, a%b); }

int small() {
   vector<int> v;

   for(int i = 0; i < (int)x.size(); ++i) 
      v.push_back(atoi(x[i].c_str()));
   
   sort(v.begin(), v.end());
   int mali = v[0];

   for(int i = 0; i < (int)v.size(); ++i) 
      v[i] -= mali;

   int g = v.back();
   if(!g) return 0;

   for(int i = 1; i < n-1; ++i) 
      if(v[i]) 
         g = gcd(g, v[i]);   

   int r = (-mali)%g; 
   return r < 0 ? r+g : r;
}

int main() {
   int T;

   scanf("%d", &T);
   for(int t = 0; t < T; ++t) {
      scanf("%d", &n);
      x.clear();
      for(int i = 0; i < n; ++i) {
         string sv;
         cin >> sv;
         x.push_back(sv);
      }
      
      printf("Case #%d: %d\n", t+1, small());
   }

   

   return 0;
}

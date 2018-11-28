#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
       
    long long t, r, k, n, *A, *Z, *S;
    cin >> t;
    for(long long q=0; q<t; ++q) {
            
      cin >> r >> k >> n;
      A = new long long[n];
      Z = new long long[n];
      S = new long long[n];
      for(long long i=0; i<n; ++i)
        cin >> A[i];
      long long first = 0, kol = 0;
	  long long res = 0;
      Z[kol] = 0;
      S[kol] = 0;
      bool cycle = false;
      long long from = r;
      
      while(kol<r && !cycle) {
        long long now = 0;
        long long last = first;
        while(now+A[last] <= k) {
          now += A[last];
          last = (last+1)%n;
          if(last == first) break;
        }
        first = last;
        kol++;
        S[kol] = now;
        Z[kol] = first;
        for(long long i=kol-1; i>=0; --i)
          if(Z[kol] == Z[i] && kol!=r) {
            from = i;
            cycle = true;
          }
      }
      
	  for(long long i=1; i<=from; ++i) 
        res += S[i];
	  if(kol<r) {
        long long cycleres = 0;
        for(long long i=from+1; i<=kol; ++i)
          cycleres += S[i];
        
        r -= from;
        res += cycleres*(r/(kol-from));
        r %= kol-from;
        for(long long i=1; i<=r; ++i) res += S[from + i];
      }
      printf("Case #%I64d: %I64d\n", q+1, res);
    }
    return EXIT_SUCCESS;
}

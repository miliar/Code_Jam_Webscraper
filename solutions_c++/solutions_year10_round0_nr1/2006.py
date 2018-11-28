#include <cstdlib>
#include <iostream>

using namespace std;

int pow(int a, int b) {
  if(b == 1) return a;
  if(b%2 == 0) return pow(a, b/2)*pow(a, b/2);
  else return pow(a, (b-1)/2)*pow(a, (b-1)/2)*a;
}

int main(int argc, char *argv[])
{
    freopen("A-small.in", "r", stdin);
    freopen("A-small.out", "w", stdout);
    
    int T, n, k;
    cin >> T;
    for(int i=0; i<T; ++i) {
      cin >> n >> k;
      k++;
      if(k % pow(2, n) == 0) printf("Case #%d: ON\n", i+1);
      else printf("Case #%d: OFF\n", i+1);   
    }
    return EXIT_SUCCESS;
}

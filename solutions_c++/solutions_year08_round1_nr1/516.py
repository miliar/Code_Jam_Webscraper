#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char *argv[]){

  int t, c = 1, n;
  
  scanf("%d",&t);
  
  while(t--)
    {
      scanf("%d",&n);
      
      vector <long long> x, y;
      x.resize(n);
      y.resize(n);

      for(int i = 0; i < n; i++) scanf("%lld",&x[i]);
      for(int i = 0; i < n; i++) scanf("%lld",&y[i]);

      sort(x.begin(), x.end());
      sort(y.begin(), y.end());

      long long m = 0;
      
      for(int i = 0; i < n; i++)
	m += (x[i]*y[n-i-1]);
      
      printf("Case #%d: %lld\n",c++, m);
    }

  return 0;
}

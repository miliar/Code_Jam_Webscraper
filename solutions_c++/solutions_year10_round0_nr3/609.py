#include <iostream>

int main()
{
  int T;
  std::cin >> T;
  for(int t=0; t<T; ++t)
  {
    // read in test case (observe that given the data specifications we can use integers and a fixed-size array -- this is not quite defensive programming, though...)
    int R, k, N, g[1000];
    std::cin >> R >> k >> N;
    for(int n=0; n<N; ++n)
      std::cin >> g[n];
    
    // precompute next group index (=current + number of groups taken for ride) and earns (=number of participants taken for ride) if we start ride with group index n in [0,N)
    int next[1000], E[1000];
    for(int n=0; n<N; ++n)
    {
      int s=0, e=0;
      while(s<N && e+g[(n+s)%N]<=k)
      {
        e+=g[(n+s)%N];
        s++;
      }
      next[n]=(n+s)%N;
      E[n]=e;
    }
    
    // perform runs
    int64_t e=0;
    int n=0;
    for(int r=0; r<R; ++r)
    {
      e+=E[n];
      n=next[n];
    }  
    std::cout << "Case #" << t+1 << ": " << e << std::endl;
  }
}
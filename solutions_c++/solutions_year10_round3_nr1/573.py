
#include <iostream>
#include <vector>
#include <utility>

int main(int,char**)
{

  int T;
  std::cin >> T;
  for(int t=0;t<T;++t){
    int N;
    std::cin >> N;

    std::vector<std::pair<int,int> > W(N);
    for(int n=0;n<N;++n)
      std::cin >> W[n].first >> W[n].second;

    int cross = 0;
    for(int m=0;m<N;++m)
      for(int n=m+1;n<N;++n)
        if((W[n].first-W[m].first)*(W[n].second-W[m].second)<0)
          ++cross;

    std::cout << "Case #" << (t+1) << ": " << cross << '\n';
  }

  return 0;
}

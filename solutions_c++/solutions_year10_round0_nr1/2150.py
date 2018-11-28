
#include <iostream>

int main(int,char**)
{
  int T;
  std::cin >> T;
  for(int i=0;i<T;++i){
    int N,K;
    std::cin >> N >> K;

    int goal = (1<<N)-1;
    std::cout << "Case #" << (i+1) << ": " << ((K&goal)==goal?"ON":"OFF") << std::endl;
  }
  return 0;
}

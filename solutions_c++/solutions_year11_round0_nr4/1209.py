#include <iostream>
#include <vector>

std::vector<int> v;

int inPlaceCount() {
  int count = 0;
  for(int i=0;i<v.size();i++) {
    if(v[i] == i + 1)
      count++;
  }
  return count;
}

int main()
{
  int T;
  std::cin >> T;
  for(int c=1;c<=T;c++) {
    int N;
    std::cin >> N;
    v.clear();
    v.reserve(N);
    for(int i=0;i<N;i++) {
      int x;
      std::cin >> x;
      v.push_back(x);
    }

    int count = inPlaceCount();
    int tries = N - count;
    std::cout << "Case #" << c << ": " << tries << ".000000\n";
  }

  return 0;
}

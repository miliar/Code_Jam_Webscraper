#include <fstream>
#include <iostream>
#include <cassert>
#include <cmath>
#include <stdexcept>
#include <string>
#include <map>
#include <vector>
#include <list>
#include <cctype>
#include <algorithm>

using namespace std;

typedef unsigned long long Ullong;

struct sort_first {
  bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
    return left.first < right.first;
  }
};

struct sort_second {
  bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
    return left.second < right.second;
  }
};

int main()
{

  int T,N,a,b;
  cin >> T;

  for (int t = 0; t < T; t++)
  {
    cin >> N;
    long int y = 0;

    std::vector<std::pair<int,int> > A;

    for (int n = 0; n < N; n++)
    {
      cin >> a >> b;
      A.push_back(std::pair<int,int>(a,b) );
    }

    std::sort(A.begin(),A.end(),sort_first());

    for (int i = 0; i < A.size(); i++)
      A[i].first = i;

    std::sort(A.begin(),A.end(),sort_second());
    for (int i = 0; i < A.size(); i++)
      A[i].second = i;

    for (int i = 0; i < A.size(); i++)
    {
      if (A[i].second > A[i].first)
        y += A[i].second - A[i].first;
    }

    cout << "Case #" << t+1 << ": " << y << endl;

  }

  return 0;
}


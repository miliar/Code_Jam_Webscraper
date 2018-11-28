#include <iostream>
#include <cstdio>

using namespace std;

const int line_max=1000;

int left_win[line_max];
int right_win[line_max];

int solve(void)
{
  int N;
  int count=0;

  cin >> N;

  for(int i=0; i<N; i++){
    cin >> left_win[i] >> right_win[i];
  }

  for(int i=0; i<N; i++){
    for(int j=i+1; j<N; j++){
      if((left_win[i] - left_win[j])*(right_win[i] - right_win[j]) < 0)++count;
    }
  }

  return count;
}

int main()
{
  int T;

  cin >> T;

  for(int i=0; i<T; i++){
    printf("Case #%d: %d\n", i+1, solve());
  }
}

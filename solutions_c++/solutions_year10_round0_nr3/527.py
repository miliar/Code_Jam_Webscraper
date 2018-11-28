#include <iostream>
#include <vector>

using namespace std;

const int maxN=1000;

struct CGroup
{
public:
  int size;
  long long int income;
  long long int prev_round;
};

struct CGroup group[maxN];

void init(void)
{
  for(int i=0; i<maxN; ++i){
    group[i].size = 0;
    group[i].income = -1;
    group[i].prev_round = -1;
  }
}

void solve(void)
{
  int R; // round
  int k; // coaster size
  int N; // group number
  long long int income = 0;
  int current_group = 0;

  init();

  cin >> R >> k >> N;

  for(int i=0; i<N; ++i){
    cin >> group[i].size;
  }

  for(int current_round = 0; current_round < R;){
    int rider=0;
    int initial_group = current_group;

    if(group[initial_group].prev_round >= 0){
#if 1
      // special shortcut
      long long int round_diff = current_round - group[initial_group].prev_round;
      long long int income_diff = income - group[initial_group].income;
      long long int meta_round = (R - 1 - current_round)/round_diff;

      if(meta_round > 0){
	income += meta_round * income_diff;
	current_round += meta_round * round_diff;
      }
#endif
    }
    group[initial_group].prev_round = current_round;
    group[initial_group].income = income;

    while(rider + group[current_group].size <= k
	  && !(rider > 0 && current_group == initial_group)){
      rider += group[current_group].size;
      current_group = (current_group + 1) % N;
    }

    income += rider;

    ++current_round;
  }

  cout << income << "\n";
}

int main()
{
  int T;

  cin >> T;

  for(int i=0; i<T; ++i){
    cout << "Case #" << (i+1) << ": ";
    solve();
  }
}

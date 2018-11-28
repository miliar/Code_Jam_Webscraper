#include <iostream>
#include <list>
#include <vector>

using namespace std;

const int TMAX = 30;


unsigned int cycle[TMAX];

int calc_cycle(int N)
{
  int rval;

  if(cycle[N]>0)return cycle[N];

  if(N>0){
    rval = calc_cycle(N-1) * 2 + 1;
  }
  else{
    // N==1
    rval = 1;
  }
  
  cycle[N]=rval;
  return rval;
}

void solve(void)
{
  int N;
  int K;
  int c;

  cin >> N >> K;

  c = calc_cycle(N-1);
  
  if(((K + 1)% (c+1)) == 0){
    cout << "ON\n";
  }
  else{
    cout << "OFF\n";
  }
}

// c c+1 c+1

int main()
{
  int T;

  for(int i=0; i<TMAX+1; i++)cycle[i]=0;

  cin >> T;

  for(int i=0; i<T; i++){
    cout << "Case #" << (i+1) << ": ";
    solve();
  }
}

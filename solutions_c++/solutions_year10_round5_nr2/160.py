#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

#define MAX_N 105
#define MAX_S 100005
#define INF 1000000005

typedef __int64 LL;

void input(void);
void solve(void);

int n;
LL sum;
int B[MAX_N];
int F[MAX_S];
int case_cnt = 1;

int main(void)
{
  int t;
  cin >> t;
  while(t--) {
    input();
    solve();
  }
    
  return 0;
}

void input(void)
{
  cin >> sum >> n;
  for(int i = 0; i < n; i++) cin >> B[i];
}

void solve(void)
{
  sort(B, B + n);
     
  LL k = 0;
  if(sum > MAX_S) {
    k = sum / B[n - 1];
    sum -= k * B[n - 1];
  }
  while(sum + B[n - 1] < MAX_S && k > 0) {
    sum += B[n - 1];
    k--;
  }
  
  //cout << "sum = " << sum << " k = " << k << endl;
  
  F[0] = 0;
  for(int i = 1; i <= sum; i++) {
    F[i] = INF;
    for(int j = 0; j < n; j++) if(i >= B[j] && F[i] > F[i - B[j]] + 1) F[i] = F[i - B[j]] + 1;
  }
  
  if(F[sum] == INF) {
    cout << "Case #" << case_cnt++ << ": IMPOSSIBLE" << endl;
  }
  else {
    cout << "Case #" << case_cnt++ << ": " << (k + F[sum]) << endl;
  }
  
}


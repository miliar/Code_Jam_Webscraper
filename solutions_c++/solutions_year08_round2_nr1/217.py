#include <iostream>
#include <vector>
#include <set>

using namespace std;

typedef __int64 LL;

void gen(LL n, LL A, LL B, LL C, LL D, LL x0, LL y0, LL M);

vector <pair <LL, LL> > P;

int main(void)
{
  int t;
  cin >> t;
  for(int case_cnt = 1; case_cnt <= t; case_cnt++) {
    LL n, A, B, C, D, x0, y0, M;
    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    gen(n, A, B, C, D, x0, y0, M);
    //for(int i = 0; i < P.size(); i++) 
    //  cout << " (" << P[i].first << ", " << P[i].second << ")";
    //cout << endl;
    LL ans = 0;
    for(int i = 0; i < P.size(); i++)
      for(int j = 0; j < i; j++)
        for(int k = 0; k < j; k++) {
          LL x = P[i].first  + P[j].first  + P[k].first;
          LL y = P[i].second + P[j].second + P[k].second;
          if(x % 3 != 0 || y % 3 != 0) continue;
          ans++;
        }
    cout << "Case #" << case_cnt << ": " << ans << endl;
  }   
    
  return 0;
}

/*
X = x0, Y = y0
print X, Y
for i = 1 to n-1
  X = (A * X + B) mod M
  Y = (C * Y + D) mod M
  print X, Y
  */


void gen(LL n, LL A, LL B, LL C, LL D, LL x0, LL y0, LL M)
{
  P.resize(n);
  LL X = x0;
  LL Y = y0;
  P[0].first  = X;
  P[0].second = Y;
  for(int i = 1; i < n; i++) {
    X = (A * X + B) % M;
    Y = (C * Y + D) % M;
    P[i].first  = X;
    P[i].second = Y;
  }
}



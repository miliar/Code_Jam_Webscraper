#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define FOR(i, N) for(int i = 0, _n = N ; i < _n ; ++i )

int main()
{
  int T;
  scanf("%d", &T);

  FOR(t, T) {
    vector <int> v1, v2;
    long long sum = 0;
    int N;
    
    scanf("%d", &N);
    v1.resize(N); v2.resize(N);
    FOR(i, N) scanf("%d", &v1[i]);
    FOR(i, N) scanf("%d", &v2[i]);
    
    sort(v1.begin(), v1.end());
    sort(v2.begin(), v2.end());
    reverse(v2.begin(), v2.end());
    
    FOR(i, N) sum += (long long) (v1[i]) * (long long ) (v2[i]);
    
    printf("Case #%d: %Ld\n", t+1, sum);
  }
}


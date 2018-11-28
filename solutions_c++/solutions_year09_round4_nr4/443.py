#include<cstdio>
#include<iostream>
#include<vector>
#include<cstring>
#include<string>
#include<algorithm>
#include<set>
#include<map>
#include<cstring>
#include<bitset>
#include<sstream>
#include<queue>
#include<cmath>
#include<cstdlib>
#include<numeric>
#include<complex>
#include<utility>
#include<ext/numeric>
#include<iomanip>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

const int MAX_N = 40;
double X[MAX_N], Y[MAX_N], R[MAX_N];

int main()
{
  int T;
  cin >> T; cin.ignore();
  for(int t = 1; t <= T; t++)
    {
      cout << "Case #" << t << ": ";
      int N;
      cin >> N;
      for(int n = 0; n < N; n++)
        cin >> X[n] >> Y[n] >> R[n];
      if(N <= 2)
        printf("%.10lf\n", max(R[0],R[N-1]));
      if(N == 3)
        {
          double mini = 1e50;
          for(int i = 0; i < 3; i++)
            {
              int j = !i, k = 3-i-j;
              mini = min(mini,
                         max(R[i], .5*(R[k]+R[j]+hypot(X[j]-X[k], Y[j]-Y[k]))));
            }
          printf("%.10lf\n", mini);
        }
    }
}

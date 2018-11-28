#include <fstream>
using namespace std;
int T, r, k, n, i, a[1000], next[1000], Sum[1000];

ifstream fin( "a.in" );
ofstream fout( "a.out" );

int main()
{
    fin >> T;
    int t = T;
    while ( T-- )
    {
          int S = 0;
          fin  >> r >> k >> n;
          for ( i = 0; i < n; ++i )
          {
              fin >> a[i];
              S += a[i];
          }
          
          for ( i = 0 ; i < n; ++i )
          {
              int p = i, sum = 0;
              while ( sum+a[p] <= k && sum < S )
              {
                    sum += a[p];
                    p = (p+1)%n;
              }
              next[i] = p;
              Sum[i] = sum;
          }
          long long ans = 0;
          int p = 0;
          for ( i = 0; i < r; ++i )
          {
              ans += Sum[p];
              p = next[p];
          }                
              
          fout << "Case #"<<t-T<<": " <<  ans <<endl ;
    }
    system( "pause");
}

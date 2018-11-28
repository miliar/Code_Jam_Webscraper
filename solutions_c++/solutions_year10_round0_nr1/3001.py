#include <fstream>
using namespace std;
int T, t, n, k, j;
int a[100];
ifstream cin("a.in");
ofstream cout("a.out");
int main()
{
    cin >> T;
    t = T;
    while ( T-- )
    {
          memset( a, 0, sizeof(a) );
          cin >> n >> k;
          int i = -1;
          while ( k >= 1 )
          {
                a[++i] = k %2;
                k /= 2;
          }
          bool bl = true;
          for ( j = 0; j < n; ++j )
              if ( a[j] != 1 )
                 bl = false;
          cout << "Case #" << t-T << ": ";
          if ( !bl )
             cout << "OFF"<<endl;
          else cout << "ON" <<endl;
    }
}

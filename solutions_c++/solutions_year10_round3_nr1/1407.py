#include <fstream>
using namespace std;
ifstream fin("1.in");
ofstream fout( "1.out" );
int ans;
int TT,T,n,i,j;
int a[10000], b[10000];
int main()
{
    fin >> T;
    int TT = T;
    while ( T-- )
    {
          ans = 0;
          fin >> n;
          for ( i = 0; i < n; ++i )
          {
              fin >> a[i] >> b[i];
              for ( j = 0; j < i; ++j )
                  if ( (a[i] > a[j] && b[i] < b[j]) || (a[i] < a[j] && b[i] > b[j]) )
                     ++ans;
          }
          
          fout << "Case #" << TT-T << ": "<<ans<<endl;
    }
}
          

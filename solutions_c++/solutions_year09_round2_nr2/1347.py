#include <fstream>
#include <algorithm>
#include <vector>

using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");

int tst;

void solve()
{
     ++tst;

     long long nr;
     
     fin >> nr;
     
     vector <int> a;
     
     while (nr > 0)
     {
          a.push_back(nr%10);
          nr /= 10;
     }
     while (a.size() < 100)
          a.push_back(0);
          
     reverse(a.begin(),a.end());
     
     next_permutation(a.begin(),a.end());

     int i=0;
     
     while (a[i] == 0) ++i;

     fout << "Case #" << tst << ": ";

     while (i<(int)a.size())
          fout << a[i++];
     fout << "\n";
}

int main()
{
     int t;
     
     fin >> t;
     
     while (t--)
          solve();
          
     return 0;
}

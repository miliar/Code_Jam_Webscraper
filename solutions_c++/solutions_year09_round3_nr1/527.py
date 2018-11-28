#include <fstream>
#include <string>

using namespace std;

int a[512];

ifstream fin("a.in");
ofstream fout("a.out");

int tst;

void solve()
{
     ++tst;

     for (int i=0;i<=128;++i)
          a[i] = -1;
          
     int baza = 0;
     
     string nr;
     
     fin >> nr;
     
     for (int i=0;i<(int)nr.length();++i)
          if (a[(int)nr[i]] == -1)
          {
               if (baza == 0)
                    a[(int)nr[i]] = ++baza;
               else if (baza == 1)
                    ++baza,
                    a[(int)nr[i]] = 0 ;
               else 
                    a[(int)nr[i]] = baza++;
          }

     if (baza == 1)
          ++baza;
               
     long long ret = 0;
     
     for (int i=0;i<(int)nr.length();++i)
          ret = ret*baza + a[(int)nr[i]];
          
          
     fout << "Case #" << tst << ": " << ret << "\n";
}

int main()
{
     int t;
     
     fin >> t;
     
     while (t--)
          solve();
          
     return 0;
}

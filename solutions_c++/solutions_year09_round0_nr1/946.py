#include <fstream>
#include <string>

using namespace std;

string a[5100];

int x[16][32];

ifstream fin("alien.in");
ofstream fout("alien.out");

int test_case, n,l,d;

void fax(string model)
{
     for (int i=0;i<l;++i)
     for (int j=0;j<26;++j)
          x[i][j] = 0;
     
     int poz = 0;
     int ind = 0;
     
     while (poz < l)
     {
          if (model[ind] == '(')
          {
               ++ind;
               for (;model[ind]!=')';++ind)
                    x[poz][model[ind]-'a'] = 1;
          }     
               else
          x[poz][model[ind]-'a'] = 1;
          ++ind; ++poz;
     }     
}

void solve()
{
     ++test_case;
     
     string model;
     
     fin >> model;
     
     fax(model);
 
     int ret = 0;

     for (int i=1;i<=d;++i)
     {
          int ok = 1;
          for (int j=0;j<l;++j)
               if (x[j][a[i][j]-'a'] == 0)
                    ok = 0;
          if (ok == 1)
               ++ret;                        
     }     
     
     fout << "Case #" << test_case << ": " << ret << "\n";
}

int main()
{
     fin >> l >> d >> n;
     
     for (int i=1;i<=d;++i)
          fin >> a[i];
          
     for (int i=1;i<=n;++i)
          solve();          
          
     return 0;               
}

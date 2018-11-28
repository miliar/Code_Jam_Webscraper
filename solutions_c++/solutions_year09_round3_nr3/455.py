#include <fstream>
#include <string>

using namespace std;

ifstream fin("c.in");
ofstream fout("c.out");

#define Nmax 128

int tst, a[Nmax], x[Nmax], ret, N, P;

void back(int lev,int sum)
{
     if (lev > N)
     {
          if (ret > sum)
               ret = sum;
     }
          else
     {
          for (int i=1;i<=N;++i)
               if (x[a[i]] == 0)
               {
                    x[a[i]] = 1;
                    
                    int tmp = 0;
                    
                    for (int j=a[i]-1;j>=1;--j)
                    {
                         if (x[j] == 1)
                              break;
                         ++tmp;
                    }

                    for (int j=a[i]+1;j<=P;++j)
                    {
                         if (x[j] == 1)
                              break;
                         ++tmp;
                    }


                    back(lev+1,sum+tmp);

                    x[a[i]] = 0;
               }
     }
}

void solve()
{
     fout << "Case #" << ++tst << ": ";
     
     fin >> P >> N;
     
     for (int i=1;i<=N;++i)
          fin >> a[i];
     
     ret = 1234567890;
     
     back(1,0);
     
     fout << ret << "\n";
}

int main()
{
     int t;
     
     fin >> t;
     
     while (t--)
          solve();
          
     return 0;
}

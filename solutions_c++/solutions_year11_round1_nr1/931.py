#include <iostream>
using namespace std;
long long n;
int pd, pg;
bool init()
{
     cin >> n >> pd >> pg;
     if (pg == 100 && pd != 100) return false;
     if (pg == 0 && pd != 0) return false;
     return true;
}
bool calc()
{
     if (n >= 100) return true;
     for (int i=1; i<=n; i++)
     {
          if (i * pd % 100 == 0)
               return true;
     }
     return false;
}
int main(int argc, char *argv[])
{
     int T;
     cin >> T;
     for (int t=1; t<=T; t++)
     {
          cout << "Case #" << t << ": ";
          if (init() && calc())
               cout << "Possible" << endl;
          else
               cout << "Broken" << endl;
     }
     return 0;
}

#include <iostream>
using namespace std;
int n, k;
bool calc()
{
     for (int i=0; i<n; i++)
     {
          if (!(k & 1))
          {
               return false;
          }
          k >>= 1;
     }
     return true;
}
int main(int argc, char *argv[])
{
     int t;
     cin >> t;
     for (int i=0; i<t; i++)
     {
          cin >> n >> k;
          cout << "Case #" << i+1 << ": ";
          if (calc())
               cout << "ON" << endl;
          else
               cout << "OFF" << endl;
     }
     return 0;
}

#include <iostream>
#include <vector>

using namespace std;

int pp(int k)
{
   if (k == 0) return 1;
   else return 2*pp(k-1);
}

int main()
{
  int cases;
  cin >> cases;
  int c = 1;
  while(cases-- > 0)
  {
     int a, b;
     cin >> a >> b;
     cout << "Case #" << c++ << ": ";
     if (((pp(a)-1)&b)==(pp(a)-1))
        cout << "ON";
     else
        cout << "OFF";
     cout << endl;
  }
}

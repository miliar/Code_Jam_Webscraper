#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++)

long long n;
long double base = 3 + sqrt(5);

void elevo()
{
     static int pepe[31] = 
     {0,0,27,143,751,935,607,903,991,335,47,943,471,55,447,463,991,95,607,263,151,855,
      527,743,351,135,407,903,791,135,647};
     int k = pepe[n];
     cout << (k/100) % 10;
     cout << (k/10) % 10;
     cout << k % 10;
     cout << endl;
}

int main()
{
    int T;
    cin >> T;
    forn(caso,T)
    {
      cin >> n;
      cout << "Case #" << caso+1 << ": ";
      elevo();
    }
    return 0;
}

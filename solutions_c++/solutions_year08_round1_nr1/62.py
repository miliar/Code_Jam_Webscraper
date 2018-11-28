#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++)

int main()
{
    int T;
    cin >> T;
    forn(caso,T)
    {
      int n;
      cin >> n;
      vector <long long> v1(n),v2(n);
      forn(i,n)
        cin >> v1[i];
      forn(i,n)
        cin >> v2[i];
      long long cuenta = 0;
      sort(v1.begin(),v1.end());
      sort(v2.begin(),v2.end());      
      forn(i,n)
        cuenta += v1[i] * v2[n-1-i];
      cout << "Case #" << caso+1<<": " << cuenta << endl;
    }
    return 0;
}

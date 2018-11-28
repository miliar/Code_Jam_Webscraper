#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;
#define For(i,a,n) for (int i=a; i<n; ++i)
#define Fori(n) For(i,0,n)

int main()
{
  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  { int n, teraz=0, czas[2]={0, 0}, poz[2]={1, 1};
    cin>>n;
    Fori(n)
    { char c;
      int a;
      cin>>c>>a;
      bool r=c=='O';
      teraz=max(teraz, czas[r]+abs(a-poz[r]))+1;
      poz[r]=a;
      czas[r]=teraz;
    }  
    cout<<"Case #"<<ca<<": "<<teraz<<endl;
  }
  return 0;
}

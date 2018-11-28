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

int t[100]={0, 1};
int ile(int n)
{ if (t[n]) return t[n];
  return t[n]=2*ile(n-1)+1;
}

int main()
{
 // ile(30);
 // Fori(32) cout<<t[i]<<endl;

  int NNN;
  cin>>NNN;
  for (int ca=1; ca<=NNN; ++ca)
  {
    int n, k;
    cin>>n>>k;
    
    cout<<"Case #"<<ca<<": "<<((k%(ile(n)+1)==ile(n)) ? "ON":"OFF")<<endl;

  }

  char ccccc;
  cin>>ccccc;

  return 0;
}

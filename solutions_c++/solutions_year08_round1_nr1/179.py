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
  int n, t;
  long long t1[1000], t2[1000];
  cin>>n;
  for (int ca=1; ca<=n; ++ca)
  {
    cin>>t;
    Fori(t) cin>>t1[i];
    Fori(t) cin>>t2[i];
    sort(t1, t1+t);
    sort(t2, t2+t);
    long long wyn=0;
    Fori(t) wyn+=t1[i]*t2[t-i-1];
  
  
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
    



  }

  char ccccc;
  cin>>ccccc;

  return 0;
}

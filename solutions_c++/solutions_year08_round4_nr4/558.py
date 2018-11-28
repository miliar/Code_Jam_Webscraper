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

int wyn, k;
int kolej[5]={0, 1, 2, 3, 4};
string s;

void spr()
{ string s1=s;
  int poz=0;
  while (poz<s.size())
  { Fori(k)
      s1[poz+i]=s[poz+kolej[i]];
    poz+=k;  
  }
  int w=1;
  for (int i=1; i<s.size(); ++i)
    if (s1[i]!=s1[i-1]) ++w;
  wyn=min(wyn, w);
}

int main()
{
  int n;
  cin>>n;
  for (int ca=1; ca<=n; ++ca)
  {
    
    cin>>k>>s;
    wyn=10000000;
    Fori(k) kolej[i]=i;
    do 
    {
      spr();
    } while (next_permutation(kolej, kolej+k));
    
    cout<<endl<<"Case #"<<ca<<": "<<wyn<<endl;
  }

  char ccccc;
  cin>>ccccc;

  return 0;
}

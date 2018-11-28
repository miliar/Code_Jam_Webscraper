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
    
	int l, d, n;
	cin>>l>>d>>n;
	string slowa[5000];
	Fori(d)
	    cin>>slowa[i];
	for (int ca=1; ca<=n; ++ca)
	{
	  int wyn=0;
	  string s;
	  cin>>s;
	  bool jest[15][250];
	  memset(jest, 0, sizeof(jest));
	  for (int i=0, poz=0; i<l; ++i)
	    if (s[poz]=='(')
	    { for (++poz; s[poz]!=')'; ++poz)
	        jest[i][s[poz]]=true;
	      ++poz;
	    }
	    else jest[i][s[poz++]]=true;
  
    Fori(d)
    { bool ok=true;
      for (int j=0; j<l && ok; ++j)
        if (!jest[j][slowa[i][j]]) ok=false;
      if (ok) ++wyn;    
    }
    cout<<"Case #"<<ca<<": "<<wyn<<endl;
  }



  return 0;
}

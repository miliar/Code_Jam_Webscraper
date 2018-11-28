#include <algorithm>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <iomanip>

using namespace std;

const int MaxInt=numeric_limits<int>::max();
typedef vector<int> VI;
typedef vector<string> VS;
#define For(i,a,n) for (int i=a; i<n; ++i)
#define Fori(n) For(i,0,n)

struct Wezel
{ double d;
  string s;
  Wezel *tak, *nie;
};

Wezel *buduj(string &s, int &poz)
{ while (s[poz]!='(') ++poz;
  ++poz;
  while (isspace(s[poz])) ++poz;
  int pocz=poz;
  while (isdigit(s[poz]) || s[poz]=='.') ++poz;
  stringstream ss(s.substr(pocz, poz-pocz));
  Wezel *w=new Wezel();
  ss>>w->d;
  while (isspace(s[poz])) ++poz;
  if (s[poz]==')')
  { ++poz;
    w->tak=w->nie=0;
    return w;
  }
  pocz=poz;
  while (!isspace(s[poz])) ++poz;
  w->s=s.substr(pocz, poz-pocz);
  w->tak=buduj(s, poz);
  w->nie=buduj(s, poz);
  while (s[poz]!=')') ++poz;
  ++poz;
  return w;
}

int main()
{
  int NNN;
  cin>>NNN;
  cout<<fixed;
  for (int ca=1; ca<=NNN; ++ca)
  { int l;
    cin>>l;
    string s, d;
    getline(cin, s);
    Fori(l)
    { getline(cin, s);
      d+=s;
    }
    int poz=0;
    Wezel *w=buduj(d, poz);
    while (poz<d.size() && isspace(d[poz])) ++poz;
    if (poz!=d.size()) throw "blad";
    
    cout<<"Case #"<<ca<<":"<<endl;
    
    int a;
    cin>>a;
    Fori(a)
    { cin>>s;
      set<string> cechy;
      int n;
      cin>>n;
      for (int j=0; j<n; ++j)
      { cin>>s;
        cechy.insert(s);
      }
      double dd=1;
      Wezel *ww=w;
      while (ww)
      { dd*=ww->d;
        if (cechy.find(ww->s)==cechy.end()) ww=ww->nie;
        else ww=ww->tak;
      }
      cout<<setprecision(7)<<dd<<endl;
    }
  }


  return 0;
}

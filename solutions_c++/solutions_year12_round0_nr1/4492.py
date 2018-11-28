#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <queue>

#define fii(x,y) for(int i=x;i<y;i++)
#define fjj(x,y) for(int j=x;j<y;j++)
#define fkk(x,y) for(int k=x;k<y;k++)
#define fi(x) fii(0,x)
#define fj(x) fjj(0,x)
#define fk(x) fkk(0,x)
#define eps 0.0000000001
#define inf 1<<28

using namespace std;

typedef long long ll;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <VVI> VVVI;
typedef vector <ll> VL;
typedef vector <VL> VVL;
typedef vector <double> VD;
typedef vector <VD> VVD;
typedef vector <bool> VB;
typedef vector <VB> VVB;
typedef queue <int> QI;
typedef pair<int,int> PI;
typedef pair<int,PI> PT;
typedef queue<PI> QPI;
typedef priority_queue<PT> QPT;
typedef pair<double,double> PD;
typedef vector<string> VS;

int main()
{
  VS s, t;
  s = t = VS(4);
  s[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  s[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  s[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  s[3] = "y qee";
  t[0] = "our language is impossible to understand";
  t[1] = "there are twenty six factorial possibilities";
  t[2] = "so it is okay if you want to just give up";
  t[3] = "a zoo";
  string trans (26, '*');
  fi (4) fj (s[i].size())
  {
    if (s[i][j] == ' ') continue;
    trans[s[i][j]-'a']=t[i][j];
  }
  VB todas (26, false);
  fi (25) todas[trans[i]-'a'] = true;
  fi (26) if (not todas[i]) trans[25] = i+'a';
//   cout << trans << endl;
  int T;
  cin >> T;
  string ln;
  getline(cin,ln);
  for (int caso = 1; caso <= T; caso++)
  {
    cout << "Case #" << caso << ": ";
    getline(cin,ln);
    fi (ln.size())
    {
      if (ln[i] == ' ') cout << ' ';
      else cout << trans[ln[i]-'a'];
    }
    cout << endl;
  }
}
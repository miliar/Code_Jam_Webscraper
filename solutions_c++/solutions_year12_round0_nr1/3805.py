#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// typedef long long          ll;
// typedef vector<int>        vi;
// typedef pair<int, int>     ii;
// typedef vector<ii>         vii;
// typedef set<int>           si;
// typedef map<string, int>   msi;

// #define for(i, a, b) \
//   for(int i = int(a); i <= int(b); i++)
// #define Rvi(c, it) \
//   for(vi::iterator it = (c).begin(); it != (c).end(); it++)
// #define Rvii(c, it) \
//   for(vii::iterator it = (c).begin(); it != (c).end(); it++)
// #define Rmsi(c, it) \
//   for(msi::iterator it = (c).begin(); it != (c).end(); it++)

int main() {
  int t, tc=0;
  scanf("%d", &t);
  string lol;
  getline(cin, lol);

  string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  string b = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
  string c = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
  string ga = "our language is impossible to understand";
  string gb = "there are twenty six factorial possibilities";
  string gc = "so it is okay if you want to just give up";
  string d = "y qee";
  string gd = "a zoo";

  map<char,char> gog;

  for(int i=0; i<a.length(); i++)
    gog[a[i]] = ga[i];

  for(int i=0; i<b.length(); i++)
    gog[b[i]] = gb[i];

  for(int i=0; i<c.length(); i++)
    gog[c[i]] = gc[i];

  for(int i=0; i<d.length(); i++)
    gog[d[i]] = gd[i];

  gog['z'] = 'q';

    // map<char, char>::iterator it;
    // for(it = gog.begin(); it != gog.end(); it++) {
    //    cout << "m[\'" << it->first << "\'] = \'" << it->second << "\';" << endl;
    // }

  // int alp[255];

  // // for(i, 'a', 'z')
  // //   alp[i] = i;

  // alp['y'] = 'a';
  // alp['e'] = 'o';
  // alp['q'] = 'z';

  // for(i, 0, a.length()-1)
  //   alp[a[i]] = ga[i];

  // // for(i, 'a', 'z')
  // //   cout << (char)i << " -> " << (char)alp[i] << endl;

  // for(i, 0, b.length()-1)
  //   alp[b[i]] = gb[i];

  // // for(i, 'a', 'z')
  // //   cout << (char)i << " -> " << (char)alp[i] << endl;

  // for(i, 0, c.length()-1)
  //   alp[c[i]] = gc[i];

  // // for(i, 'a', 'z')
  // //   cout << (char)i << " -> " << (char)alp[i] << endl;

  //  for(i, 'a', 'z')
  //    cout << (char)i;
  //  cout << endl;
  //  for(i, 'a', 'z')
  //    cout << (char)alp[i];
  //  cout << endl;

    while(t--) {
      tc++;
      string s;
      getline(cin, s);
      cout << "Case #" << tc << ": ";
      // for(i, 0, s.length()-1) {
      for(int i=0; i<s.length(); i++)
	cout << gog[s[i]];
   //     cout << (char)alp[s[i]];
      cout << endl;
      }

      cout << endl;
    // }

  return 0;
}

#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;





int main() {
  freopen("A-small-attempt1.in","r",stdin);
  freopen("out.txt","w",stdout);

    string a,b,c;
    map<char,char> m;

    a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
    b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
    forn(i,si(a)) m[a[i]]=b[i];
    m['q']='z';
    m['z']='q';

    //cout<<m.size()<<endl;
   // forall(it,m) cout<<it->first<<" "<<it->second<<endl;


    int t;
    string tt; getline(cin,tt);
    t = atoi(tt.c_str());
  for (int cas = 1;cas<=t;cas++) {

    string res;
    getline(cin,res);

    forn(i,si(res)) res[i]=m[res[i]];

    cout << "Case #" << cas << ": " << res << endl;
  }


  return 0;
}

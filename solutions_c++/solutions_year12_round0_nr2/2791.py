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
  freopen("B-large.in","r",stdin);
  freopen("out.txt","w",stdout);
    int t; cin>>t;

  for (int cas = 1;cas<=t;cas++) {
        int n,s,p;
        cin>>n>>s>>p;
        vi v(n);
        forn(i,n) cin>>v[i];
        //forn(i,n) cout<<v[i]<<" "; cout<<endl;

        sort(rall(v));
        //forn(i,n) cout<<v[i]<<" "; cout<<endl;

        int res = 0;

        forn(i,n) {
            if (v[i]>=3*p-2) res++;
            else if ((v[i]>=3*p-4 && v[i]>0) && s>0) {
                s--; res++;
            }
        }



    cout << "Case #" << cas << ": " << res << endl;
  }


  return 0;
}

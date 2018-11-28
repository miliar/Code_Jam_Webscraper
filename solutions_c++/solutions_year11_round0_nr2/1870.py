#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
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

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef set<int> se;
typedef pair<int,int> pii;
typedef long long int tint;

#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define all(c) (c).begin(), (c).end()
#define D(a) << #a << "=" << a << " "


#define si(a) int((a).size())
#define pb push_back
#define mp make_pair

vector<char> v;
set<pair<char,char> > O;
map<pair<char,char>,char> C;

void combine() {
    int n = si(v)-1;
    if(C.find(mp(v[n],v[n-1])) != C.end()) {
        char c = C[mp(v[n],v[n-1])];
        v.pop_back();v.pop_back();
        v.pb(c);
    }
}
void opp() {
    int n = si(v)-1;
    forn(i,si(v))
        if(O.find(mp(v[n],v[i])) != O.end())
            v.clear();

}


int main () {
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
        int t;
        cin>>t;
        forn(o,t) {
            int c; cin>>c;
            string aux;
            O.clear();
            C.clear();
            forn(i,c) {
                cin>>aux;
                C[mp(aux[0],aux[1])]=aux[2];
                C[mp(aux[1],aux[0])]=aux[2];
            }
            int d; cin>>d;
            forn(i,d) {
                cin>>aux;
                O.insert(mp(aux[0],aux[1]));
                O.insert(mp(aux[1],aux[0]));
            }
            int n; cin>>n;
            string s; cin>>s;


            v.clear();
            forn(i,n) {
                v.pb(s[i]);
                combine();
                opp();
            }

            string res = "[";
            string sep = "";
            forn(i,si(v)) {res += sep + v[i]; sep = ", ";}
            res += "]";
            cout<<"Case #"<<o+1<<": "<<res<<endl;




        }

  return 0;

}



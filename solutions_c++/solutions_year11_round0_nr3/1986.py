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


#define sz(a) int((a).size())
#define pb push_back



int main () {
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
        int t;
        cin>>t;
        forn(o,t) {
            int n;
            cin>>n;
            vi c(n);
            forn(i,n) cin>>c[i];
            sort(all(c));
            int suma=0; int suma2=0;
            forn(i,n) {suma^=c[i]; suma2+=c[i];}
            string res;
            cout<<"Case #"<<o+1<<": ";
            if (suma!=0) cout<<"NO"<<endl;
            else cout<<(suma2-c[0])<<endl;




        }

  return 0;

}



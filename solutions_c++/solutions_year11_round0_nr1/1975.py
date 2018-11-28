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


vector<pair<string,int> > B;


int dest(string a,int k) {
    forsn(i,k,si(B)) if (B[i].first==a) return B[i].second;
    return 1;
}

//i es O y j es B
int paso(int i,int j,int k) {
    if (k==si(B)) return 0;
    //forn(t,si(B)) cout<<B[t].first<<" "<<B[t].second<<endl;
 //   cout<<"paso "<<i<<" "<<j<<endl;
    int p,di=dest("O",k),dj=dest("B",k);
    if (B[k].first=="O") p = abs(di-i)+1; else p = abs(dj-j)+1;
 //   cout D(di) D(dj) D(p);
    int aux;
    if (B[k].first=="O") {
        i = di;
        aux = dj-j;
        if (abs(aux)<=p) j = dj;
        else j = j+ p* (aux / (abs(aux)));
    }
    else {
        j = dj;
        aux = di-i;
        if (abs(aux)<=p) i = di;
        else i = i+ p* (aux / (abs(aux)));
    }
  //  cout D(i) D(j); cout<<endl;


    return p+paso(i,j,k+1);
}



int main () {
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
        int t;
        cin>>t;
        forn(o,t) {
            int n;
            cin>>n;
            B.clear();
            string aa; int aa2;
            forn(i,n) {cin>>aa>>aa2; B.pb(mp(aa,aa2));}
            int res = paso(1,1,0);


            cout<<"Case #"<<o+1<<": "<<res<<endl;




        }

  return 0;

}



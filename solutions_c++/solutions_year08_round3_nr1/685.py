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
	freopen("entrada.in","r",stdin);
	freopen("out.txt","w",stdout);

  int n;
  cin>>n;
  int aux;

  forn(kk,n) {
    int p,k,l;
    vi key;
    vi key2;
    cin>>p>>k>>l;
    forn(i,l) {
      cin>>aux;
      key.pb(aux);
    }

    sort(all(key));
    forn(i,l) if (key[i]>0) key2.pb(key[i]);

    //forn(i,sz(key2)) cout<<key2[i]<<" ";cout<<endl;
    //cout<<p<<" "<<k<<" "<<l<<endl;
    
    if (sz(key2)>k*p) cout<<"Case #"<<kk+1<<": Impossible"<<endl;
    else {
      int suma=0;
      int ac=1;
      int r=k;
      for(int pp=sz(key2)-1;pp>=0;pp--) {
        suma+=ac*key2[pp];
        //cout<<"suma: "<<suma<<endl;
        r--;
        if (r==0) {r=k;ac++;}
      }


     cout<<"Case #"<<kk+1<<": "<<suma<<endl;
    }
    

    

  }


  return 0;

}



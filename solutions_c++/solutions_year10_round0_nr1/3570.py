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



void init() {

}

int main () {
	freopen("A-large.in","r",stdin);
	//freopen("B-large.in","r",stdin);
	freopen("out2.txt","w",stdout);

    int n,k;

    int tt;
    cin>>tt;
    string res;

    forn(ii,tt) {
        cin>>n>>k;

        init();
        //int pot = 1<<n;
        res = (k+1) % (1<<n) ? "OFF"  : "ON";
       // cout<<k+1<<" "<<(1<<n)<<" " <<(k+1) % (1<<n)<<endl;

        cout<<"Case #"<<ii+1<<": "<<res<<endl;
    }


  return 0;

}



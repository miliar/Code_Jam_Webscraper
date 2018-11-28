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

int const MAX = 300;


int main () {
	//freopen("A-large.in","r",stdin);
	freopen("A-small.in","r",stdin);
	freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    forn(ii,t) {

        string s;
        cin>>s;
        int v[MAX]; forn(i,MAX) v[i]=-1;
        int current = 1;

        forn(i,sz(s)) {
            int ord = (int)s[i];
            if (v[ord]==-1) {
                v[ord]=current;
                if (current==1) current = 0;
                else if (current==0) current = 2;
                else current++;
            }
        }

        tint res=0;
        tint base = max(2,current);
        tint exp = 1;
        dforsn(i,0,sz(s)) {
            res = res + exp*v[(int)s[i]];
            //cout<<"valor "<<v[(int)s[i]]<<"  expo "<<exp<<endl;
            exp*=base;
        }


        cout<<"Case #"<<ii+1<<": "<<res<<endl;
    }

  return 0;

}



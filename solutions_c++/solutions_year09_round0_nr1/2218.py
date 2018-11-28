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

vector<vector<char> > pal;
vector<string> words;

int l,d,n;

void pattern(string s) {
    pal.clear();
    vector<char> aux; char c; int pos=0;
    forn(i,l) {
        aux.clear();
        if (s[pos]!='(') { aux.pb(s[pos++]);}
        else {
            pos++;
            while(s[pos]!=')') aux.pb(s[pos++]);
            pos++;
        }
        pal.pb(aux);
    }
    /*cout<<"PATRON   ";
    forn(i,sz(pal)) { forn(j,sz(pal[i])) cout<<pal[i][j]<<"-"; cout<<" || "; }
    cout<<endl;*/

}

bool match(string s) {
    forn(i,sz(pal)) {
        bool aux = false;
        forn(j,sz(pal[i])) aux= aux | (pal[i][j]==s[i]);
        if (!aux) return false;
    }
    return true;
}

int solve() {
    int res=0;
    forn(i,sz(words)) {
        if (match(words[i])) res++;
    }

    return res;
}

int main () {
	//freopen("A-small.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);


    string aux;

    cin>>l>>d>>n;

    forn(i,d) { cin>>aux; words.pb(aux); }
    forn(i,n) {
        string aux;
        cin>>aux;
        pattern(aux);
        cout<<"Case #"<<i+1<<": "<<solve()<<endl;
    }



  return 0;

}



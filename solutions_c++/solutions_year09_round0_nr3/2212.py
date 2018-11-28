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
	//freopen("A-small.in","r",stdin);
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);

    int n;string nn;
    getline(cin,nn);
    stringstream(nn) >> n;
    string s = "welcome to code jam";
    int l = sz(s);
    forn(kk,n) {
        string t;
        getline(cin,t);
        //cout<<"palabra "<<t<<endl;
        int M[l+1];
        M[0]=1; forn(i,l) M[i+1]=0;

        forn(i,sz(t))
            forn(j,l)
                if (t[i]==s[j])
                    //M[j+1]+=M[j];
                    M[j+1]=(M[j+1]+M[j])%10000;


        cout<<"Case #"<<kk+1<<": ";
        for(int a=1000;a>1;a/=10) if(M[l]<a) cout<<"0";
        cout<<M[l]<<endl;
    }




  return 0;

}




#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef pair<string, string> pss;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;


int main() {
    freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small-attempt0.out","wt",stdout);

    int tcnr=0;
    vector<pss> table;

    table.pb({"a","y"});
    table.pb({"b","h"});
    table.pb({"c","e"});
    table.pb({"d","s"});
    table.pb({"e","o"});
    table.pb({"f","c"});
    table.pb({"g","v"});
    table.pb({"h","x"});
    table.pb({"i","d"});
    table.pb({"j","u"});
    table.pb({"k","i"});
    table.pb({"l","g"});
    table.pb({"m","l"});
    table.pb({"n","b"});
    table.pb({"o","k"});
    table.pb({"p","r"});
    table.pb({"q","z"});
    table.pb({"r","t"});
    table.pb({"s","n"});
    table.pb({"t","w"});
    table.pb({"u","j"});
    table.pb({"v","p"});
    table.pb({"w","f"});
    table.pb({"x","m"});
    table.pb({"y","a"});
    table.pb({"z","q"});
    table.pb({" "," "});

    cin>>tcnr;

    string line;
    getline(cin, line);

    rep(nr,tcnr){

        getline(cin, line);

        string output="";

        rep(i,line.size()){
            string s(1, line[i]);
            rep(j,table.size()){
                if(s.compare(table[j].first)==0){
                    string temp1(1, output[output.size()-1]);
//                    string temp2(1, table[j].second[table[j].second.size()-1]);
  //                  if(temp2.compare(temp1)==0)
    //                    output += " ";
                    output += table[j].second;
                    break;
                }
            }
        }

        cout<<"Case #"<<(nr+1)<<": "<<output;
        if ((nr+1)<tcnr)
            cout<<endl;
    }
}

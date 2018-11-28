#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <cmath>
#include <sstream>
#include <utility>
#include <cctype>
#include <numeric>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <limits>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <functional>
#include <inttypes.h>
#include <fstream>
using namespace std;

#define vset(c)			 cout<<#c << " :  ";for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)cout<<*it<<" | ";cout << endl;
#define vmap(c)			 cout<<#c << " :  ";for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)cout<<" ("<<it->first<<","<<it->second<<") |";cout << endl;
#define vap(c)           cout<<#c << " :  ";for(int JJ=0;JJ<(c).size();++JJ)cout<<(JJ==0?"[":"")<<c[JJ].first<<","<<c[JJ].second<<(JJ==(c).size()-1?"]\n":" | ");
#define va(c)            cout<<#c << " :  ";for(int JJ=0;JJ<(c).size();++JJ)cout<<(JJ==0?"[":"")<<c[JJ]<<(JJ==(c).size()-1?"]\n":"|");
#define vat(a,t)         cout<<#a << " :  ";for(int JJ=0;JJ<t;++JJ)cout<<(JJ==0?"[":"")<<a[JJ]<<(JJ==t-1?"]\n":",");
#define vaa(c)           cout<<#c << " :  "<<endl;for(int II=0;II<(c).size();++II)for(int JJ=0;JJ<(c[II]).size();++JJ)cout<<(JJ==0?"\t[":"")<<c[II][JJ]<<(JJ==(c[II]).size()-1?"]\n":"|");
#define vaat(c,F,C)      cout<<#c << " :  "<<endl;for(int II=0;II<F;++II)for(int JJ=0;JJ<C;++JJ)cout<<(JJ==0?"\t[":"")<<c[II][JJ]<<(JJ==C-1?"]\n":"|");
#define vx(x)            cout<<"{ " << #x << " = "<<x<<" }"<<endl;
#define vx2(x,y)         cout<<"{ " << #x << " = "<<x<<", " << #y << " = "<<y<<" }"<<endl;
#define vx3(x,y,z)       cout<<"{ " << #x << " = "<<x<<", " << #y << " = "<<y<<", " << #z << " = "<<z<<" }"<<endl;
#define vx4(x,y,z,w)     cout<<"{ " << #x << " = "<<x<<", " << #y << " = "<<y<<", " << #z << " = "<<z<<", " << #w << " = "<<w<<" }"<<endl;
#define vx5(x,y,z,w,q)   cout<<"{ " << #x << " = "<<x<<", " << #y << " = "<<y<<", " << #z << " = "<<z<<", " << #w << " = "<<w<<", " << #q << " = "<<q<<" }"<<endl;
#define vx6(x,y,z,w,q,p) cout<<"{ " << #x << " = "<<x<<", " << #y << " = "<<y<<", " << #z << "
template<class T> string tostring(T x) {ostringstream sout;sout<<x;return sout.str();}
template<class T> int toint( T s ) {int v;istringstream sin( tostring(s) );sin>>v;return v;}

void solve( const int& test, const int& a , const int& b )
{
    set<pair<int,int> > all;
    int ans = 0;
    string s, ss, fs , sn;
    for( int n = a; n <= b; ++ n )
    {
        s = tostring(n);
        //vx2(s,n)
        for( int i = 0; i < s.size()-1; ++ i )
        {
            fs = s.substr(0,i+1);
            sn = s.substr(i+1);
            ss = sn+fs;
            int other = toint(ss);
            if( other != n && a <= other && other <= b )
                all.insert( make_pair(min(n,other),max(n,other)  ) );
            //vx3(fs,sn,other)
        }
    }
    //vmap(all)
    cout << "Case #"<<test<< ": "<< all.size() <<endl;
}
int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int n;
    cin >> n;
    for( int i = 0; i < n; ++ i )
    {
        int a , b;
        cin >> a >> b;
        solve(i+1,a,b);
    }
    return 0;
}






#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define ll long long
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define sz size()
#define pb push_back
#define mp make_pair
#define mem(x,i) memset(x,i,sizeof(x))
#define cpresent(V,e) (find(all(V),(e))!=(V).end())
#define foreach(c,it) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define f(i,a,n) for(int (i)=(int)(a);i<(int)(n);++(i))
#define fr(i,a,n) for(int (i)=(int)(a);i>(int)(n);--(i))

using namespace std;

long long toi(string s){istringstream is(s);long long x;is>>x;return x;}
string tos(long long t){stringstream st; st<<t;return st.str();}
long long gcd(long long a, long long b){return __gcd(a,b);}
long long lcm(long long a,long long b){return a*(b/gcd(a,b));}
long long bits(long long a){return a?1+bits(a&(a-1)):0;};
long long pot(long long a,long long b){if(!b)return 1;if(b&1)return a*pot(a*a,b>>1); else return pot(a*a,b>>1);}

map <char,char> M;

int main(){
   freopen("rat.txt","r",stdin);
   freopen("sal.txt","w",stdout);
   M['a'] = 'y' ; M['b'] = 'h' ; M['c'] = 'e' ; M['d'] = 's' ; M['e'] = 'o' ; M['f'] = 'c' ;
   M['g'] = 'v' ; M['h'] = 'x' ; M['i'] = 'd' ; M['j'] = 'u' ; M['k'] = 'i' ; M['l'] = 'g' ;
   M['m'] = 'l' ; M['n'] = 'b' ; M['o'] = 'k' ; M['p'] = 'r' ; M['q'] = 'z' ; M['r'] = 't' ;
   M['s'] = 'n' ; M['t'] = 'w' ; M['u'] = 'j' ; M['v'] = 'p' ; M['w'] = 'f' ; M['x'] = 'm' ;
   M['y'] = 'a' ; M['z'] = 'q' ; M[' '] = ' ' ;
   int tc ;
   cin >> tc;
   string line;
    getline(cin,line);
   for(int i = 1 ; i <= tc ; ++i)
   {
     cout <<"Case #"<<i<<": ";
      getline(cin,line);
     foreach(line,it)
       cout << M[*it];
     cout << endl;        
   } 
}





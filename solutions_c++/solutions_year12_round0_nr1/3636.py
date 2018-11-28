#include<queue>
#include<set>
#include<deque>
#include<stack>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<map>
#include<fstream>
using namespace std;
#define dbg(x) cout << #x << " -> " << (x) << "\t";
#define rep(i,n) for(int i=0;i<n;i++)
#define pb push_back
#define sz size()
#define psi pair<string,int>
#define all(x) x.begin(),x.end()
#define GI ({int t;scanf("%d",&t); t;})
#define flush(x) memset(x,0,sizeof(x))
#define ll long long
#define mod 1000000007
#define maxn 1000010
#define GLI ({ll t;scanf("%lld",&t); t;})
#define tr(i,a) for( typeof(a.begin()) i=a.begin();i!=a.end();i++)
int main() {
  map<char,char> mp;
  mp['a'] = 'y';
  mp['b'] = 'h';
  mp['c'] = 'e';
  mp['d'] = 's';
  mp['e'] = 'o';
  mp['f'] = 'c';
  mp['g'] = 'v';
  mp['h'] = 'x';
  mp['i'] = 'd';
  mp['j'] = 'u';
  mp['k'] = 'i';
  mp['l'] = 'g';
  mp['m'] = 'l';
  mp['n'] = 'b';
  mp['o'] = 'k';
  mp['p'] = 'r';
  mp['q'] = 'z';
  mp['r'] = 't';
  mp['s'] = 'n';
  mp['t'] = 'w';
  mp['u'] = 'j';
  mp['v'] = 'p';
  mp['w'] = 'f';
  mp['x'] = 'm';
  mp['y'] = 'a';
  mp['z'] = 'q';
  mp[' '] = ' ';
  int t = GI, T, kase = 1;
  T = t;
  while(t--) {
    cout<<"Case #"<<kase<<": ";
    string a;
    her:
    getline(cin,a);
    if(a=="") goto her;
    int z = a.sz;
    rep(i,z)   cout<<mp[a[i]];
    if(kase != T) cout<<endl;
    kase++;
  }
}
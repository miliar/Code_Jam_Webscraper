#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <queue>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <list>
#include <stack>
#include <numeric>
#include <bitset>
#include <list>
using namespace std;
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define ST first
#define ND second
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define FORE(i,x) for(__typeof((x).begin()) i=(x).begin();i != (x).end();++i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define VAR(v,n) __typeof(n) v = n
#define sgn(x) (x > 0) ? 1 : ((x < 0) ? -1 : 0)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define SZ(x) int((x).size()) 
#define SIZE(x) (int)x.size()
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,w) memset((x),w,sizeof (x))
// string -> char* : string a; a.c_str();
// char* -> string : char a[N]; string(a);
// int -> char* : int a; char b[N]; sprintf(b, "%d", a);
// char* -> int : int a; char b[N]; sscanf(b, "%d", &a);
// char* -> int podstawa base : char a[N]; strtol(a, NULL, base)
// porowananie char* : strcmp(char*,char*) np return strcmp(&c[a],&c[b])<0;
// bitset: cout << bitset<20> (100000) << endl;
// iostream: cin, getline(cin, string); stdio: scanf, gets(char *), getchar()
// sort(ALL(v),less<int>()) rosnaca, sort(ALL(v),greater<int>()) malejaca
// struct T {string name; lli X,Y;};
// bool operator<(T a,T b){return a.X*a.X+b.Y*b.Y < a.X*a.X+b.Y*b.Y;}
typedef vector<int> vi, VI;
typedef pair<int, int> pii, PII;
typedef pair<pii, int> piii;
typedef vector<pii> vii;
typedef long long int lli, LL;
typedef vector<lli> vl;
typedef pair<lli, lli> pll;
typedef vector<pll> vll;
#define MAXN 105  

char m[256];
char s1[120], s2[120];
int n;

int main(){

m['a'] = 'y';
m['b'] = 'h';
m['c'] = 'e';
m['d'] = 's';
m['e'] = 'o';
m['f'] = 'c';
m['g'] = 'v';
m['h'] = 'x';
m['i'] = 'd';
m['j'] = 'u';
m['k'] = 'i';
m['l'] = 'g';
m['m'] = 'l';
m['n'] = 'b';
m['o'] = 'k';
m['p'] = 'r';
m['q'] = 'z';
m['r'] = 't';
m['s'] = 'n';
m['t'] = 'w';
m['u'] = 'j';
m['v'] = 'p';
m['w'] = 'f';
m['x'] = 'm';
m['y'] = 'a';
m['z'] = 'q';
    
    cin >> n;
    gets(s1);
    REP(i,n){
        gets(s1);
        cout << "Case #" << i + 1 << ": "; 
        for(int j = 0; s1[j] != 0; j++)
            if(s1[j] >= 'a' && s1[j] <= 'z')
                cout << m[s1[j]];
            else
                cout << s1[j];
        cout << endl;
    }

    return 0;
}













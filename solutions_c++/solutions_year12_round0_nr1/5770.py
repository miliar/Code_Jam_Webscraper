#include <algorithm>
#include <iostream>
#include <sstream>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <complex>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <vector>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
const double eps = 1e-11;
const double pi = acos(-1.0);
const double inf = 1e17;
#define swap(a,b) {a^=b;b^a=;a^=b;}
#define two(X) (1<<(X))
#define pair <int,int> pii
#define SZ(x) ((int)x.size())
template<class T> T gcd(const T &a,const T &b) {return (b==0)?a:gcd(b,a%b);}
template<class T> T lcm(const T &a,const T &b) {return a*(b/gcd(a,b));}
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
int main(){
    int T;
    string s;
    string map = "yhesocvxduiglbkrztnwjpfmaq";
    cin >> T;
    getchar();
    for (int i = 0; i < T; i ++){
        getline(cin, s);
        for (int j = 0; j < SZ(s); j ++){
            if (s[j] == ' ') continue;
            s[j] = map[s[j] - 'a'];    
        }
        cout << "Case #" << i + 1 << ": " << s << endl;
        // printf("Case #%d: %s\n",i+1, s);
    }
    // system("pause");
    return 0;
}


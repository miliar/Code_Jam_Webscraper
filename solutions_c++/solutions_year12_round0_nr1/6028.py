#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <utility>
#include <numeric>
#include <functional>
using namespace std;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define fori(i, n) for(int i = 0; i < n; i++)
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vi> vvi;
typedef pair<int,int> ii;

using namespace std;

int main(){
    string IN  = "entrada.in";
    string OUT  = "A-small-attempt2.out";
    ifstream ARC( IN.c_str() );
    bool FLAG = ARC.fail();
    if( ! FLAG ){
       freopen( IN.c_str() ,"r",stdin );
       freopen( OUT.c_str() ,"w",stdout );
    }
    map<char, char>m;
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
    m[' '] = ' ';
    int T;
    scanf("%d\n", &T);
    string G;
    for(int t = 1; t <= T; ++t){
        printf("Case #%d: ", t);
        getline(cin, G);
        fori(i, (int)G.length()){
            putchar(m[G[i]]);
        }
        printf("\n");
    }
    return EXIT_SUCCESS;
}

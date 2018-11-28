#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <climits>
#include <cfloat>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <numeric>
#include <complex>
#include <utility>
#include <memory>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <sstream>
#include <assert.h>
using namespace std;

const double EPS = 1e-9;
const int INF = 100000000;
const int MOD = 1000000007;

typedef vector<int> vint;
typedef vector<vint> vvint;
typedef vector<string> vst;
typedef pair<int,int> pint;
typedef long long ll;

template<class T1, class T2> ostream& operator<<(ostream &s, pair<T1,T2> P){return s<<'<'<<P.first<<", "<<P.second<<'>';}
template<class T> ostream& operator<<(ostream &s, vector<T> P) {s<<"{ ";for(int i=0;i<P.size();++i){if(i>0)s<<", ";s<<P[i];}return s<<" }"<<endl;}
template<class T> ostream& operator<<(ostream &s, vector<vector<T> > P) {for(int i=0;i<P.size();++i){s<<i<<" : "<<P[i];}return s;}

map<char, char> M;

int main() {    
    freopen( "/Users/macuser/Downloads/A-small-attempt2.in", "r", stdin );
	freopen( "/Users/macuser/Downloads/a_output.txt", "w", stdout );
    M['y']='a'; M['n']='b'; M['f']='c'; M['i']='d'; M['c']='e'; M['w']='f'; M['l']='g'; M['b']='h'; M['k']='i';
    M['u']='j'; M['o']='k'; M['m']='l'; M['x']='m'; M['s']='n'; M['e']='o'; M['v']='p'; M['z']='q'; M['p']='r';
    M['d']='s'; M['r']='t'; M['j']='u'; M['g']='v'; M['t']='w'; M['h']='x'; M['a']='y'; M['q']='z'; M[' ']=' ';
    
    int T;
    char c[128] = {(char)0};
    
    scanf("%d", &T);
    cin.getline(c, 128);
    
    for (int i = 0; i < T; ++i) {
        for (int j = 0; j < 128; ++j) c[j] = (char)0;
        cin.getline(c, 128);
        
        printf("Case #%d: ", i+1);
        for (int j = 0; j < 128; ++j) {
            if (c[j] != (char)0) {
                printf("%c", M[c[j]]);
            }
        }
        printf("\n");
    }
    
	return 0;
}





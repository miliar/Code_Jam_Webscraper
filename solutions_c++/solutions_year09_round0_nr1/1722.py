#include <vector>
#include <list>
#include <map>
#include <set>
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

using namespace std;

#define S(X) ((int)(X).size())
#define FOR(I, N) for (int I=0; I<(int)N;++I)
#define FORI(N) FOR(i,N)
#define FORJ(N) FOR(j,N)
#define FORK(N) FOR(k,N)
#define LOOP(N) FOR(__i__, N)

typedef long long LL;
typedef unsigned long long ULL;

const double eps = 1e-11;
const double pi=acos(-1.0);

template<class T> T gcd(T a, T b){ if (a<0) return gcd(-a,b); if (b<0)return gcd(a, -b); return (b==0)?a:gcd(b, a%b);}
int countbit(int n){return (n==0)?0:(1+countbit(n&(n-1)));}
int lowbit(int n){return (n^(n-1))&n;}
template<class T> string toString(T integer) { ostringstream os; os << integer; return os.str();}

#define foreach(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define P(a,b) make_pair((a),(b))
template<typename T, typename U> U cast(T arg){
    ostringstream oss;
    oss << arg;
    istringstream iss(oss.str());
    U rv;
    iss >> rv;
    return rv;
}

vector <vector<char> > pattern;
int L, D, N;
vector<set<string> > dict;

int count(string prefix, int i){
    int total = 0;

    if (i == L)
        return 1;

    FORJ(pattern[i].size()){
        prefix += pattern[i][j]; 
        if (dict[i].find(prefix) != dict[i].end()){
            total += count(prefix, i + 1);
        }
        prefix.erase(prefix.size() - 1);
    }

    return total;
}

int main(int argc, char *argv[])
{
    freopen("A-small-attempt0.in", "r", stdin);
    cin >> L >> D >> N;
    dict.assign(L, set<string>());
    LOOP(D){
        string w;
        cin >> w;
        FORI(w.length()){
            string prefix = w.substr(0, i + 1);
            dict[i].insert(prefix);
        }
    }

    FORI(N){
        pattern.clear();
        FORJ(L){
            vector<char> options;
            char c;
            cin >> c;
            if (c == '('){
                while (cin >> c && c != ')')
                    options.push_back(c); 
            } else {
                options.push_back(c);
            }
            pattern.push_back(options);
        }
        vector<int> p(L, 0);

        printf("Case #%d: %d\n", (i+1), count("", 0));
    }

    

}

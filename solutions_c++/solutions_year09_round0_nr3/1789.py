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

const string obj = "welcome to code jam";
string text;

LL arr[500][500];

LL count(int end, int j){
    LL cnt = 0;
    if (j == -1)
        return 1;
    if (end < 0)
        return 0;
    if (arr[end][j] >= 0)
        return arr[end][j];

    if (text[end] == obj[j]){
        cnt += count(end - 1, j - 1) % 10000;
    }

    cnt += count(end - 1, j) % 10000;
    arr[end][j] = cnt;
    return cnt;
}

int main(int argc, char *argv[])
{
    int N;
    cin >> N;

    getline(cin, text);
    FORI(N){      
       getline(cin, text);
       FORJ(text.size())FORK(text.size())arr[j][k] = -1;
       printf("Case #%d: %04lld\n", i + 1, count(text.size() - 1, obj.size() - 1) % 10000);
        
    }
}


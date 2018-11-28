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
#include <queue>
#include <fstream>
#include <ctime>
using namespace std;
#define FOR(i,a,b) for(LL i = a; i < b; i++)
#define RFOR(i,a,b) for(LL i = a; i > b; i--)
#define FSI(a) FORSZ(i, 0, a.size())
#define FSJ(a) FORSZ(j, 0, a.size())
#define FSK(a) FORSZ(k, 0, a.size())
#define VI vector<LL>
#define VVI vector<VI>
#define VS vector<string>
#define VVS vector<VS>
#define LL long long
#define ALL(a) a.begin(), a.end()
#define SORT(a) sort(ALL(a))
#define REVERSE(a) reverse(ALL(a))
#define NPERM(a) (next_permutation(ALL(a)))
#define PB push_back
#define MP make_pair
#define STREAM(a, b) stringstream ss; ss << (a); string b; while(ss >> (b))
#define EQ(a,b) (abs(a-b) < 1e-11)
#define SQR(a) ((a)*(a))

template<class T> T gcd(T x, T y) { while ( y != 0 ){ T z = x % y; x = y; y = z; } return x; }
template<class T> string i2s(T s){ostringstream oss; oss << s; return oss.str();}
LL s2i(string s){ return atoi(s.c_str()); }
LL s2ll(string s){ return atol(s.c_str()); }
double s2f(string s){ return atof(s.c_str()); }


ifstream fin;
ofstream fout;

LL ans[500001];
LL A[500001];
LL AA[500001];
LL N;
const LL MOD = 1000000007;

LL solve(LL at)
{
    if(at >= N){        
        return 0;
    }
    LL &ret = ans[at];
    if(ret != -1LL){        
        return ret;
    }

    ret = 1;
    FOR(i,at+1,N){
        if(A[i] > A[at]) 
            ret = (ret + solve(i)) % MOD;
    }    
    return ret % MOD;

}


LL go()
{
    LL m, X, Y, Z;
    fin >> N >> m >> X >> Y >> Z;    
    FOR(i,0,m)
        fin >> AA[i];    
    FOR(i,0,N){        
        A[i] = AA[i % m];
        AA[i % m] = (X * AA[i % m] + Y * (i+1)) % Z;
    }
    FOR(i,0,500001)
        ans[i] = -1LL;
    LL ret = 0LL;    
    FOR(i,0,N)
        ret = (ret + solve(i)) % MOD;    
    return ret % MOD;
}




int main(){
	fin.open("in.txt");
	fout.open("out.txt");
    LL ncases;
    fin >> ncases;    
    FOR(tcase, 0, ncases){        
        LL ret = go();
        fout << "Case #" << tcase+1 << ": " << ret << endl;
    }    
    return 0;	
}		





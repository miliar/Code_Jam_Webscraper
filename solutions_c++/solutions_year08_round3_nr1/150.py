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
#define FOR(i,a,b) for(int i = a; i < b; i++)
#define RFOR(i,a,b) for(int i = a; i > b; i--)
#define FSI(a) FORSZ(i, 0, a.size())
#define FSJ(a) FORSZ(j, 0, a.size())
#define FSK(a) FORSZ(k, 0, a.size())
#define VI vector<int>
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
int s2i(string s){ return atoi(s.c_str()); }
LL s2ll(string s){ return atol(s.c_str()); }
double s2f(string s){ return atof(s.c_str()); }


ifstream fin;
ofstream fout;

LL solve()
{
    long long P, K, L, ret = 0;
    fin >> P >> K >> L;
    if (L > P*K) return -1;
    cout << P << " " << K << " " << L << endl;
    VI f(L);
    FOR(i,0,L) fin >> f[i];
    SORT(f);
    REVERSE(f);    
    LL presses = 0;
    FOR(i,0,f.size()){        
        if(i % K == 0) presses++;
        ret += f[i] * presses;
    }    
    return ret;
}




int main(){
	fin.open("in.txt");
	fout.open("out.txt");
    LL N;
    fin >> N;
    cout << "N = " << N << endl;
    FOR(tcase, 0, N){        
        LL ret = solve();
        fout << "Case #" << tcase+1 << ": " << ret << endl;
    }          
    return 0;	
}		




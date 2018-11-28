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
#include <fstream>
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define RFOR(i,a,b) for(int i = (a); i > (b);i--)
#define FORSZ(i,a,b) FOR(i,0,(b).size())
#define ALL(a) (a).begin(), (a).end()
#define SORT(a) sort(ALL(a))
#define FSI(a) FORSZ(i, 0, (a))
#define FSJ(a) FORSZ(j, 0, (a))
#define FSK(a) FORSZ(k, 0, (a))
#define shift(n) (1<<(n))
#define shiftL(n) ((ll)(1<<(n)))
#define SQR(a) ((a)*(a))

using namespace std;

ifstream fin;
ofstream fout;

int N;
int L;
map<string, int> M;
int seq[1001];
int ans[1001][1001];

int solve(int at, int prev)
{
    if (at == L) return 0;
    
    int &ret = ans[at][prev];
    if(ret != -1) return ret;    

    ret = INT_MAX;
    FOR(i,0,N){
        if(i == seq[at]) continue;
        if(i == prev || at == 0)
            ret = min(ret, solve(at+1, i));
        else
            ret = min(ret, 1 + solve(at+1, i));
    }    

    return ret;
}


void solveProblem()
{
    int nCases; fin >> nCases;
    FOR(tcase, 0, nCases){ 
        memset(seq, 0x00, sizeof(seq));
        memset(ans, 0xff, sizeof(ans));
        M.clear();

        fin >> N;
        fin.get();
        FOR(i,0,N){
            char s[1000];
            fin.getline(s, 1000);                        
            M[s] = i;
        }
        
        fin >> L;
        fin.get();        
        FOR(i,0,L){            
            char s[1000];
            fin.getline(s, 1000);            
            seq[i] = M[s];
        }

        int ret = INT_MAX;

        ret = solve(0, 0);
        cout << "Case #" << tcase+1 << ": " << ret << endl;
        fout << "Case #" << tcase+1 << ": " << ret << endl;

    }    
}




int main()
{
    fin.open("C:\\Users\\t-gregpa\\Documents\\Visual Studio 2008\\Projects\\GCJ\\in.txt");
    fout.open("C:\\Users\\t-gregpa\\Documents\\Visual Studio 2008\\Projects\\GCJ\\out.txt");
    solveProblem();
}






















